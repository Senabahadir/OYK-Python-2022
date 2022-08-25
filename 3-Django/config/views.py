from django.http import HttpResponse

def merhaba(request):
    return HttpResponse('Sanada merhaba')