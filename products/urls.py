from django.urls import path
from .views import *

urlpatterns = [
    # path('', home, name='home'),
    path('items/<int:item_id>/',ItemDetail.as_view(), name="item_details"),
    path('purchase/', PurchaseItem.as_view(), name='purchase_item'),

]