from django.urls import path
from .views import logout, login, signup, home, dashboard, supplier, supplier_add, supplier_delete, supplier_command, supplier_order, feedback, feedback_answer

urlpatterns = [
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout, name='logout'),

    path('home/', home, name='home'),

    path('dashboard/', dashboard, name='dashboard'),

    path('supplier/', supplier, name='supplier'),
    path('supplier/add/', supplier_add, name='supplier_add'),
    path('supplier/delete/<int:supplier_id>/', supplier_delete, name='supplier_delete'),

    path('supplier_command/', supplier_command, name='supplier_command'),
    path('supplier_order/<int:supplier_id>/<int:item_id>/', supplier_order, name='supplier_order'),

    path('feedback/', feedback, name='feedback'),
    path('feedback/<int:feedback_id>/', feedback_answer, name='feedback_answer'),
]
