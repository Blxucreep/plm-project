from django.urls import path
from .views import logout, login, signup, home, dashboard

urlpatterns = [
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout, name='logout'),

    path('home/', home, name='home'),

    path('dashboard/', dashboard, name='dashboard'),
]
