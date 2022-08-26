from dataclasses import field
from django import forms
from wallet.models import Cuzdan

class CuzdanForm(forms.ModelForm):
    class Meta:
        model = Cuzdan
        fields = ['para_birimi']