from django.shortcuts import render, redirect

from .models import Orders, Admins

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
