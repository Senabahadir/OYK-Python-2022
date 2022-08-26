from django.urls import path
from wallet.views import add_wallet

urlpatterns = [
    path('new', add_wallet, name='wallet_add'),
]
