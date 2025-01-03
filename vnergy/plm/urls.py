from django.urls import path
from .views import logout, login, signup, contact, home, dashboard

urlpatterns = [
    path('logout/', logout, name='logout'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),

    path('contact/', contact, name='contact'),

    path('home/', home, name='home'),

    path('dashboard/', dashboard, name='dashboard'),
]
