from django.urls import path
from . import views
from .views import logout, login, signup, home, dashboard

urlpatterns = [
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout, name='logout'),

    path('home/', home, name='home'),

    path('dashboard/', dashboard, name='dashboard'),

    path('suppliers/', views.supplier_list, name='supplier_list'),
    path('suppliers/delete/<int:pk>/', views.supplier_delete, name='supplier_delete'),

    path('order-management/', views.order_management_view, name='order_management'),
    path('update-quantity/<int:supplier_id>/', views.update_quantity, name='update_quantity'),
    path('update-order-date/<int:supplier_id>/', views.update_order_date, name='update_order_date'),

    path('feedback-management/', views.feedback_management_view, name='feedback_management'),
    path('respond-to-feedback/<int:feedback_id>/', views.respond_to_feedback, name='respond_to_feedback'),

]
