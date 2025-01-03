from django.shortcuts import render

from .models import Orders

def logout(request):
    # TODO
    return render(request, 'logout.html')

def login(request):
    # TODO
    return render(request, 'login.html')

def signup(request):
    # TODO
    return render(request, 'signup.html')

def contact(request):
    # TODO
    return render(request, 'contact.html')

def home(request):
    #user_email = request.COOKIES.get('email', None)

    return render(request, 'home.html')

def dashboard(request):
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
        'sales': sales,
        'months': months
    }
    return render(request, 'dashboard.html', context)
