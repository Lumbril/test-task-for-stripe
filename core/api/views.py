from django.shortcuts import render, get_object_or_404
from django.views import View

from api import models


class PurchaseView(View):
    def get(self, request, *args, **kwargs):
        pass


class ItemView(View):
    def get(self, request, *args, **kwargs):
        item = get_object_or_404(models.Item, id=kwargs['id'])

        context = {
            'name': item.name,
            'description': item.description,
            'price': item.price
        }

        return render(request, 'index.html', context=context)
