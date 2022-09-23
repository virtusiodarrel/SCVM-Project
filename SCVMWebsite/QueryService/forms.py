from django import forms
from django.forms import ModelForm
from .models import BDSA

class BDSAForm(ModelForm):
    class Meta:
        model = BDSA
        fields = ("cve_id", "bdsa_id", "title", "description", "technical_description", "solution", "patch_links", "mitigation", "vul_function")

        labels = {
            "cve_id": '',
            "bdsa_id": '',
            "title": '',
            "description": '',
            "technical_description": '',
            "solution": '',
            "patch_links": '',
            "mitigation": '',
            "vul_function": ''
        }

        widgets = {
            "cve_id": forms.TextInput(attrs={'class':'form-control-sm', 'placeholder': 'CVE ID'}),
            "bdsa_id": forms.TextInput(attrs={'class':'form-control-sm', 'placeholder': 'BDSA ID'}),
            "title": forms.TextInput(attrs={'class':'form-control-sm', 'placeholder': 'Title'}),
            "description": forms.TextInput(attrs={'class':'form-control-sm', 'placeholder': 'Description'}),
            "technical_description": forms.TextInput(attrs={'class':'form-control-sm', 'placeholder': 'Technical Description'}),
            "solution": forms.TextInput(attrs={'class':'form-control-sm', 'placeholder': 'Solution'}),
            "patch_links": forms.TextInput(attrs={'class':'form-control-sm', 'placeholder': 'Patch Links'}),
            "mitigation": forms.TextInput(attrs={'class': 'form-control-sm', 'placeholder': 'Mitigation'}),
            "vul_function": forms.TextInput(attrs={'class':'form-control-sm', 'placeholder': 'Vulnerable Function'}),
        }