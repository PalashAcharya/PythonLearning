from django.shortcuts import render

# Create your views here.
# myapp/views.py

from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_checkout_session(request):
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'The Product',
                    },
                    'unit_amount': 9900,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri('/thank-you/'),
            cancel_url=request.build_absolute_uri('/'),
        )
        return JsonResponse({'id': session.id})
    except Exception as e:
        return JsonResponse({'error': str(e)})

def product_page(request):
    return render(request, 'product.html', {'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY})

def thank_you_page(request):
    return render(request, 'thank_you.html')

