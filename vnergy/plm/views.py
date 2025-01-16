from django.shortcuts import render, redirect, get_object_or_404
from .models import Orders, Items, IsComposed, Stocked, Admins, Suppliers, IsSupplied, CustomerFeedbacks
from datetime import datetime
import json
import random
from collections import defaultdict

def logout(request):
    # set the cookie to expire
    response = redirect('home')
    response.delete_cookie('username')

    return response

def login(request):
    if 'login_submit' in request.POST:
        # do a get request to login
        username = request.POST.get('username')
        password = request.POST.get('password')

        # check if the username and password are correct
        user = Admins.objects.filter(username=username, password=password)
        if not user:
            return render(request, 'login.html', {'error': 'Wrong username or password'})
        else:
            # redirect to the home page
            response = redirect('home')

            response.set_cookie('username', username)
            return response

    return render(request, 'login.html')

def signup(request):
    if 'signup_submit' in request.POST:
        # do a post request to signup
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')

        # check if the username is already used
        user = Admins.objects.filter(username=username)
        if user:
            return render(request, 'signup.html', {'error': 'Username already used'})
        else:
            # create the user
            new_user = Admins(username=username, password=password, role=role)
            new_user.save()

            # redirect to the home page
            response = redirect('home')
                
            response.set_cookie('username', username)
            return response

    return render(request, 'signup.html')


def home(request):
    username = request.COOKIES.get('username', None)

    return render(request, 'home.html', {'username': username})


def dashboard(request):
    username = request.COOKIES.get('username', None)

    x = request.GET.get('x-axis')
    y = request.GET.get('y-axis')
    data_converted = []

    if not x and not y:
        return render(request, 'dashboard.html', {'username': username})
    elif x == 'time' and y == 'sales':
        orders = Orders.objects.all()

        # create a dictionnary for each month
        data = {}
        for order in orders:
            month = order.order_date.strftime('%Y-%m')
            if month in data:
                data[month].append(order.total_price)
            else:
                data[month] = [order.total_price]

        # do the mean for each month
        data_converted = [{'time': month, 'sales': float(sum(data[month])/len(data[month]))} for month in data]
    elif x == 'time' and y == 'commands':
        orders = Orders.objects.all()

        #create a dictionnary for each month
        data = {}
        for order in orders:
            month = order.order_date.strftime('%Y-%m')
            if month in data:
                data[month] += 1
            else:
                data[month] = 1

        data_converted = [{'time': month, 'commands': number} for month, number in data.items()]
    elif x == 'status' and y == 'number':
        orders = Orders.objects.all()
        data = {}
        for order in orders:
            status = order.status
            if status in data:
                data[status] += 1
            else:
                data[status] = 1

        data_converted = [{'status': status, 'number': number} for status, number in data.items()]
        
    return render(request, 'dashboard.html', {'username': username, 'data': json.dumps(data_converted), 'x_axis': x, 'y_axis': y})


def sale(request):
    username = request.COOKIES.get('username', None)
    orders = Orders.objects.all()
    
    # get the items for each order
    orders_with_items = []
    for order in orders:
        items = IsComposed.objects.filter(order_id=order).select_related('item_id')
        items_details = [
            {
                'name': item.item_id.name,
                'price': item.item_id.price,
                'quantity': item.quantity
            }
            for item in items
        ]
        orders_with_items.append({
            'order_id': order.order_id,
            'order_date': order.order_date,
            'email': order.email.email,
            'total_price': order.total_price,
            'items': items_details,
            'status': order.status
        })
    
    # group by status
    orders_by_status = defaultdict(list)
    for entry in orders_with_items:
        orders_by_status[entry['status']].append(entry)

    # re-convert the defaultdict to a dict
    orders_by_status = dict(orders_by_status)

    # re-organize the dict to have the status in this order: pending, confirmed, in transit, delivered, cancelled
    orders_by_status = sorted(orders_by_status.items(), key=lambda x: ['Pending', 'Confirmed', 'In Transit', 'Delivered', 'Cancelled'].index(x[0]))
    orders_by_status = dict(orders_by_status)

    return render(request, 'sale.html', {'username': username, 'orders_by_status': orders_by_status})

def get_random_warehouse_for_item(item):
    # get the specific warehouses that stock the item
    warehouses_with_item = Stocked.objects.filter(item_id=item.item_id)

    if warehouses_with_item.exists():
        # select a random warehouse that stocks the item
        random_warehouse = random.choice(warehouses_with_item)
        return random_warehouse
    else:
        return None

def sale_update_status(request, order_id):
    order = Orders.objects.get(order_id=order_id)

    if order.status != 'Delivered' and order.status != 'Cancelled':
        if order.status == 'Pending':
            # update the stock of the items
            items = IsComposed.objects.filter(order_id=order).select_related('item_id')
            for item in items:
                warehouse = get_random_warehouse_for_item(item)
                if warehouse:
                    stock = Stocked.objects.get(item_id=item.item_id, warehouse_id=warehouse.warehouse_id)
                    stock.quantity -= item.quantity
                    stock.save()
                else:
                    continue
        # update the status of the order
        statuses = ['Pending', 'Confirmed', 'In Transit', 'Delivered']
        current_index = statuses.index(order.status)
        order.status = statuses[current_index + 1]
        order.save()

    return redirect('sale')


def supplier(request):
    username = request.COOKIES.get('username', None)
    suppliers = Suppliers.objects.all()
    
    return render(request, 'supplier.html', {'username': username, 'suppliers': suppliers})

def supplier_add(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    address = request.POST.get('address')
    product_sold = request.POST.get('product_sold')

    supplier = Suppliers(name=name, email=email, phone=phone, address=address, product_sold=product_sold)
    supplier.save()

    return redirect('supplier')

def supplier_delete(request, supplier_id):
    supplier = get_object_or_404(Suppliers, supplier_id=supplier_id)
    supplier.delete()

    return redirect('supplier')


def manufacture(request):
    username = request.COOKIES.get('username', None)

    # get all the relations between suppliers and items
    supplies = IsSupplied.objects.select_related('supplier_id', 'item_id')

    supplies_with_infos = []
    for supply in supplies:
        supplier = supply.supplier_id
        item = supply.item_id

        supply = IsSupplied.objects.filter(supplier_id=supplier, item_id=item)

        # add the supply to the list
        supplies_with_infos.append({
            'product_name': supplier.product_sold,
            'item_id': item.item_id,
            'item_name': item.name,
            'supplier_id': supplier.supplier_id,
            'supplier_name': supplier.name,
            'quantity': supply[0].quantity or 0
        })

    items = Items.objects.all()

    cans = []
    for item in items:
        item_id = item.item_id
        name = item.name

        # get the ingredients of the item
        ingredients = IsSupplied.objects.filter(item_id=item_id)
        
        # get the names of the ingredients
        ingredients_with_names = Suppliers.objects.filter(supplier_id__in=[ingredient.supplier_id.supplier_id for ingredient in ingredients])
        product_names = ', '.join([ingredient.product_sold for ingredient in ingredients_with_names])

        # get the quantity of the cans
        can = Stocked.objects.filter(item_id=item_id)
        quantity = can[0].quantity if can else 0

        # add the can to the list
        cans.append({
            'item_id': item_id,
            'name': name,
            'ingredients': product_names,
            'quantity': quantity
        })

    return render(request, 'manufacture.html', {'username': username, 'supplies_with_infos': supplies_with_infos, 'cans': cans})

def supplier_order(request, supplier_id, item_id):
    # get the item supplied by the supplier
    supplied_item = IsSupplied.objects.get(supplier_id=supplier_id, item_id=item_id)

    supplied_item.quantity += 10
    supplied_item.save()

    return redirect('manufacture')

def manufacture_item(request, item_id):
    # get the supplies
    supplies = IsSupplied.objects.filter(item_id=item_id)

    for supply in supplies:
        supply.quantity -= 1
        supply.save()

    # get the can
    can = Stocked.objects.get(item_id=item_id)
    can.quantity += 1
    can.save()

    return redirect('manufacture')


def feedback(request):
    username = request.COOKIES.get('username', None)
    feedbacks = CustomerFeedbacks.objects.all()

    return render(request, 'feedback.html', {'username': username, 'feedbacks': feedbacks})

def feedback_answer(request, feedback_id):
    feedback = CustomerFeedbacks.objects.get(feedback_id=feedback_id)

    feedback.answer = request.POST.get('answer')
    feedback.answer_date = datetime.now()
    feedback.save()

    return redirect('feedback')