from django.urls import path
from .views import logout, login, signup, home, dashboard, sale, sale_update_status, supplier, supplier_add, supplier_delete, manufacture, supplier_order, manufacture_item, feedback, feedback_answer

urlpatterns = [
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout, name='logout'),

    path('home/', home, name='home'),

    path('dashboard/', dashboard, name='dashboard'),

    path('sale/', sale, name='sale'),
    path('sale_update_status/<int:order_id>/', sale_update_status, name='sale_update_status'),

    path('supplier/', supplier, name='supplier'),
    path('supplier/add/', supplier_add, name='supplier_add'),
    path('supplier/delete/<int:supplier_id>/', supplier_delete, name='supplier_delete'),

    path('manufacture/', manufacture, name='manufacture'),
    path('supplier_order/<int:supplier_id>/<int:item_id>/', supplier_order, name='supplier_order'),
    path('manufacture_item/<int:item_id>/', manufacture_item, name='manufacture_item'),

    path('feedback/', feedback, name='feedback'),
    path('feedback/<int:feedback_id>/', feedback_answer, name='feedback_answer'),
]
