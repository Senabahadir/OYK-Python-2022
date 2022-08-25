from django.shortcuts import render

def home(request):
    bakiye = 300
    return render(request, 'index.html', {'bakiye': bakiye})