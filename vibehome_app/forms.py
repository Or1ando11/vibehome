from django.forms import ModelForm
from .models import ContactMessage
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'phone', 'email', 'property_type', 'comments']



#wyszukiwanie
class SearchForm(forms.Form):
    q = forms.CharField(label='Search', max_length=100)