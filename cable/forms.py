
from django import forms
from .models import ResidencDimens, Project


class ResidencDimensForm(forms.ModelForm):
    class Meta:
        model = ResidencDimens
        fields = ('projeto','local','tipo','tensa_va','quant','potencia_va','comprimento',
                'queda_tensao_perm','numero_polos')

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('project','description')