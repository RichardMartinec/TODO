from django import forms 
from .models import Uloha

class UlohaForm(forms.ModelForm):
    class Meta:
        model = Uloha
        fields = ['nazov', 'termin']
        widgets = {
            'termin': forms.DateInput(attrs={'type': 'date'})
        }