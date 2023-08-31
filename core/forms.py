from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from .models import Inscricoes, Contact


class InscricaoForm(forms.ModelForm):
    
    class Meta:
        model = Inscricoes
        fields = ['nome','email','phone']


class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ['nome','email','body', 'assunto']