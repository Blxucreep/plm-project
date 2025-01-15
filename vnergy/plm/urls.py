from django.urls import path
from .views import logout, login, signup, home, dashboard, supplier, supplier_add, supplier_edit, supplier_delete, supplier_command, supplier_order, feedback, feedback_response

urlpatterns = [
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout, name='logout'),

    path('home/', home, name='home'),

    path('dashboard/', dashboard, name='dashboard'),

    path('supplier/', supplier, name='supplier'),
    path('supplier/add/', supplier_add, name='supplier_add'),
    path('supplier/edit/<int:pk>/', supplier_edit, name='supplier_edit'),
    path('supplier/delete/<int:pk>/', supplier_delete, name='supplier_delete'),

    path('supplier_command/', supplier_command, name='supplier_command'),
    path('supplier_order/<int:supplier_id>/', supplier_order, name='supplier_order'),

    path('feedback/', feedback, name='feedback'),
    path('feedback/<int:pk>/', feedback_response, name='feedback_response'),
]
