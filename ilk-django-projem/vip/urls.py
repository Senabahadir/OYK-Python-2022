from django.urls import path
from vip.views import vip_home

app_name = 'vip'

urlpatterns = [
    path('', vip_home, name='vip_home'),
]
