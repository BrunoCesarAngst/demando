# /home/bruno/demando/demandas/forms.py

from django import forms
from .models import Demanda

class DemandaForm(forms.ModelForm):
    class Meta:
        model = Demanda
        fields = ['titulo', 'descricao', 'concluido']
