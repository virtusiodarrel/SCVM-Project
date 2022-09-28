from django import forms
from django.forms import ModelForm
from .models import BDSA
from prettyjson import PrettyJSONWidget
from django.contrib import admin

class BDSAForm(ModelForm):
    class Meta:
        model = BDSA
        fields = ("cve_id", "bdsa_id", "title", "json_raw")

        labels = {
            "cve_id": '',
            "bdsa_id": '',
            "title": '',
            "json_raw": '',

        }

        widgets = {
            "cve_id": forms.TextInput(attrs={'class':'form-control-sm', 'placeholder': 'CVE ID'}),
            "bdsa_id": forms.TextInput(attrs={'class':'form-control-sm', 'placeholder': 'BDSA ID'}),
            "title": forms.TextInput(attrs={'class':'form-control-sm', 'placeholder': 'Title'}),
            "json_raw": forms.TextInput(attrs={'class':'form-control-sm', 'placeholder': 'JSON Raw Contents'}),
            "myjsonfield": PrettyJSONWidget(),

        }

class UploadFileForm(forms.Form):
    file = forms.FileField(widget = forms.ClearableFileInput(attrs={'multiple': True}))

class JsonAdmin(admin.ModelAdmin):
  form = BDSAForm