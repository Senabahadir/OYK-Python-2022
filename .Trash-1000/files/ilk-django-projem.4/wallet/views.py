from django.shortcuts import render
from wallet.forms import CuzdanForm

# Create your views here.
def add_wallet(request):
    context = {}
    form = CuzdanForm(request.POST or None)
    if form.is_valid():
        wallet = form.save(commit=False)
        wallet.user = request.user
        wallet.bakiye = 50
        wallet.save()
    context['form'] = form
    return render(request, 'add_wallet.html', context)