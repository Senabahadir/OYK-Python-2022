from django.shortcuts import render
from wallet.forms import CuzdanForm

# Create your views here.
def add_wallet(request):
    context = {}
    form = CuzdanForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, 'add_wallet.html', context)