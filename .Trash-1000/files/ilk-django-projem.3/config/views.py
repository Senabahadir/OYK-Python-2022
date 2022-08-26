from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {}

    if request.user.is_authenticated:
        context['cuzdanlar'] = request.user.cuzdanlar.all()

    return render(request, 'index.html', context)

def isim_yaz(request, isim):
    return render(request, 'isim.html', {'isim': isim})

def python(request):
    return HttpResponse('Bunu goremezsin.')

def ad_soyad_yaz(request, ad, soyad):
    return render(request, 'adsoyad.html', {'ad': ad, 'soyad':soyad})
    