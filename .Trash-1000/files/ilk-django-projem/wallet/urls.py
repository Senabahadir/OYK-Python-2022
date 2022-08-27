from django.urls import path
from wallet.views import add_wallet, remove_wallet

app_name = 'wallet'

urlpatterns = [
    path('new/', add_wallet, name='wallet_add'),
    path('<cuzdan_id>/sil/', remove_wallet, name='wallet_remove'),
]
