from django import forms
from django.forms import ModelForm
from django.contrib import admin
from .models import BDSA
from prettyjson import PrettyJSONWidget

class JsonForm(forms.ModelForm):
  class Meta:
    model = BDSA
    fields = '__all__'
    widgets = {
      'myjsonfield': PrettyJSONWidget(),
    }

class JsonAdmin(admin.ModelAdmin):
  form = JsonForm

class BDSAForm(ModelForm):
    class Meta:
        model = BDSA
        fields = ("cve_id", "bdsa_id", "title")

        labels = {
            "cve_id": '',
            "bdsa_id": '',
            "title": '',

        }

        widgets = {
            "cve_id": forms.TextInput(attrs={'class':'form-control-sm', 'placeholder': 'CVE ID'}),
            "bdsa_id": forms.TextInput(attrs={'class':'form-control-sm', 'placeholder': 'BDSA ID'}),
            "title": forms.TextInput(attrs={'class':'form-control-sm', 'placeholder': 'Title'}),

        }

class UploadFileForm(forms.Form):
    file = forms.FileField(widget = forms.ClearableFileInput(attrs={'multiple': True}))
