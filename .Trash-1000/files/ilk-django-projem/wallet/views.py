from django.shortcuts import render, redirect, get_object_or_404
from wallet.forms import CuzdanForm
from wallet.models import Cuzdan

# Create your views here.
def add_wallet(request):
    context = {}
    form = CuzdanForm(request.POST or None)
    if form.is_valid():
        wallet = form.save(commit=False)
        wallet.user = request.user
        wallet.bakiye = 50 # bonus
        wallet.save()
        return redirect('/')

    context['form'] = form
    return render(request, 'add_wallet.html', context)

def remove_wallet(request, cuzdan_id):
    cuzdan = get_object_or_404(Cuzdan, id=cuzdan_id, user=request.user)
    cuzdan.delete()
    return redirect('/')