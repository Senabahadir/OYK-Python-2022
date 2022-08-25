from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    bakiye = 300
    return render(request, 'index.html', {'bakiye': bakiye})

def isim_yaz(request, isim):
    return render(request, 'isim.html', {'isim': isim})

def python(request):
    return HttpResponse('Bunu goremezsin.')

def ad_soyad_yaz(request, ad, soyad):
    return render(request, 'adsoyad.html', {'ad': ad, 'soyad':soyad})
    