from django import forms

class FormFile(forms.Form):
    titulo = forms.CharField(max_length=50)
    arquivo = forms.FileField(label='arquivo')