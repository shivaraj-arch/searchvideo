from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class SubmitForm(forms.Form):
    search_text = forms.CharField(
        validators=[]
    )
    av_name = forms.CharField(
        validators=[]
    )
