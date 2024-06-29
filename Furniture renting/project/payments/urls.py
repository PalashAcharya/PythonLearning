# payments/urls.py
# myapp/urls.py

from django.urls import path
from .views import create_checkout_session, product_page, thank_you_page

urlpatterns = [
    path('', product_page, name='product'),
    path('create-checkout-session/', create_checkout_session, name='create-checkout-session'),
    path('thank-you/', thank_you_page, name='thank-you'),
]