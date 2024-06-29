from django.shortcuts import render

# Create your views here.
# myapp/views.py

from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_checkout_session(request):
    if request.method == 'POST':
        try:
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': 'Animi Dolor Pariatur',
                        },
                        'unit_amount': 1000,
                    },
                    'quantity': 1,
                },{
                    'price_data':{
                        'currency':'usd',
                        'product_data':{
                            'name':'Art Deco Home',
                        },
                        'unit_amount':3000,
                    },
                    'quantity':1,
                }],
                mode='payment',
                success_url=request.build_absolute_uri('/thank-you/?session_id={CHECKOUT_SESSION_ID}'),
                cancel_url=request.build_absolute_uri('/'),
            )
            return JsonResponse({'id': session.id})
        except Exception as e:
            return JsonResponse({'error': str(e)})
    return JsonResponse({'error': 'Invalid request method'})

def product_page(request):
    return render(request, 'shipping.html', {'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY})

def thank_you_page(request):
    return render(request, 'thank_you.html')