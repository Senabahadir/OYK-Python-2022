from django.shortcuts import render, redirect
from vip.models import Subscribe
# Create your views here.
def vip_home(request):
    if request.user.subsribe.type not in [Subscribe.USER_TYPE.Gold, Subscribe.USER_TYPE.Platinum, Subscribe.USER_TYPE.PlatinumPlus]:
        return redirect('/')
    return render(request, 'vip.html', {})