from django import forms
from .models import *

class ChaveForm(forms.ModelForm):
    class Meta:
        model = Chave
        fields = '__all__'
