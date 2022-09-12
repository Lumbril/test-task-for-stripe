import stripe
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from api import models

stripe.api_key = 'sk_test_4eC39HqLyjWDarjtT1zdp7dc'


class PurchaseView(View):
    def get(self, request, *args, **kwargs):
        item = get_object_or_404(models.Item, id=kwargs['id'])

        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                        'description': item.description,
                    },
                    'unit_amount': item.price,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='https://example.com/success',
            cancel_url='https://example.com/cancel',
        )

        return JsonResponse(data={'session_id': session.id})


class ItemView(View):
    def get(self, request, *args, **kwargs):
        item = get_object_or_404(models.Item, id=kwargs['id'])

        context = {
            'name': item.name,
            'description': item.description,
            'price': item.price / 100
        }

        return render(request, 'index.html', context=context)
