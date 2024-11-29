from django.shortcuts import render

def home(request):
    #user_email = request.COOKIES.get('email', None)

    return render(request, 'home.html')