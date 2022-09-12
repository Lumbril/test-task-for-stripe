from . import views
from django.urls import path

from .views import PurchaseView, ItemView

urlpatterns = [
    path('buy/<id>', PurchaseView.as_view(), name='buy item'),
    path('item/<id>', ItemView.as_view(), name='buy item'),
]
