from django.shortcuts import render, redirect, get_object_or_404
from .models import Admins, Supplier, Orders
from django.http import JsonResponse
from .models import CustomerFeedback
from datetime import datetime
import json

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


def supplier(request):
    username = request.COOKIES.get('username', None)
    suppliers = Supplier.objects.all()
    
    return render(request, 'supplier.html', {'username': username, 'suppliers': suppliers})

def supplier_add(request):


    return redirect('supplier')

def supplier_edit(request, id):


    return redirect('supplier')

def supplier_delete(id):
    supplier = get_object_or_404(Supplier, pk=id)
    supplier.delete()

    return redirect('supplier')


def supplier_command(request):
    username = request.COOKIES.get('username', None)
    suppliers = Supplier.objects.all()

    return render(request, 'supplier_command.html', {'username': username, 'suppliers': suppliers})

def supplier_order(supplier_id):
    supplier = get_object_or_404(Supplier, pk=supplier_id)
    supplier.quantity_purchased += 1
    supplier.save()

    return JsonResponse({'quantity_purchased': supplier.quantity_purchased})
    

def feedback(request):
    username = request.COOKIES.get('username', None)
    feedbacks = CustomerFeedback.objects.all()

    return render(request, 'feedback.html', {'username': username, 'feedbacks': feedbacks})

def feedback_response(request, feedback_id):
    if request.method == 'POST':
        feedback = get_object_or_404(CustomerFeedback, pk=feedback_id)
        response = request.POST.get('response')
        feedback.response = response
        feedback.responded_at = datetime.now()
        feedback.save()
        return JsonResponse({'response': feedback.response, 'responded_at': feedback.responded_at})