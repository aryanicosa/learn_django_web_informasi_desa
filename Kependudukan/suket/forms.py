from django import forms
from django.forms import ModelForm
from .models import Borang

# membuat form dari model yang sudah ada di models.py dan terhubung dengan postgresql
# melalui settings.py
class Borang_form(forms.ModelForm):
    class Meta:
        exclude = []
        model = Borang