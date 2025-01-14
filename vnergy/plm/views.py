from django.shortcuts import render, redirect, get_object_or_404
from .models import Orders, Admins, Supplier
from .forms import SupplierForm
from django.http import JsonResponse
from .models import CustomerFeedback
from datetime import datetime

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

    # Récupérer les données des commandes
    orders = Orders.objects.all()

    # Calculer les ventes mensuelles
    monthly_sales = {}
    for order in orders:
        # Extraire le mois de la date de commande
        month = order.order_date.strftime('%B')  # Obtenez le mois au format texte (ex. : "January")
        if month not in monthly_sales:
            monthly_sales[month] = 0
        monthly_sales[month] += float(order.total_price)

    # Ordonner les mois pour un affichage correct
    months = ["January", "February", "March", "April", "May", "June"]
    sales = [monthly_sales.get(month, 0) for month in months]

    context = {
        'username': username,
        'sales': sales,
        'months': months
    }
    return render(request, 'dashboard.html', context)



def supplier_list(request):
    if request.method == 'POST':
        supplier_id = request.POST.get('supplier_id')
        if supplier_id:  # Modification d'un fournisseur existant
            supplier = get_object_or_404(Supplier, pk=supplier_id)
            form = SupplierForm(request.POST, instance=supplier)
        else:  # Ajout d'un nouveau fournisseur
            form = SupplierForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('supplier_list')

    suppliers = Supplier.objects.all()
    return render(request, 'supplier_list.html', {'suppliers': suppliers})

def supplier_delete(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    supplier.delete()
    return redirect('supplier_list')

import json

def supplier_view(request):
    suppliers = list(Supplier.objects.values('name', 'performance_score'))
    suppliers_json = json.dumps(suppliers)  # Sérialisation en JSON
    return render(request, 'template.html', {'suppliers_json': suppliers_json})


def order_management_view(request):
    suppliers = Supplier.objects.all()
    return render(request, 'order_management.html', {'suppliers': suppliers})

def update_quantity(request, supplier_id):
    if request.method == 'POST':
        supplier = get_object_or_404(Supplier, pk=supplier_id)
        data = request.POST
        action = data.get('action')
        if action == 'increase':
            supplier.quantity_purchased += 1
        elif action == 'decrease' and supplier.quantity_purchased > 0:
            supplier.quantity_purchased -= 1
        supplier.save()
        return JsonResponse({'quantity': supplier.quantity_purchased})

def update_order_date(request, supplier_id):
    if request.method == 'POST':
        supplier = get_object_or_404(Supplier, pk=supplier_id)
        data = request.POST
        next_order_date = data.get('next_order_date')
        if next_order_date:
            supplier.next_order_date = next_order_date
            supplier.save()
        return JsonResponse({'next_order_date': supplier.next_order_date})
    

def feedback_management_view(request):
    feedbacks = CustomerFeedback.objects.all()
    return render(request, 'feedback_management.html', {'feedbacks': feedbacks})

def respond_to_feedback(request, feedback_id):
    if request.method == 'POST':
        feedback = get_object_or_404(CustomerFeedback, pk=feedback_id)
        response = request.POST.get('response')
        feedback.response = response
        feedback.responded_at = datetime.now()
        feedback.save()
        return JsonResponse({'response': feedback.response, 'responded_at': feedback.responded_at})