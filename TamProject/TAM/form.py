from django.forms import ModelForm
from .models import *


class NameForm(ModelForm):
    class Meta:
        model = Name
        fields = '__all__'


class PhoneNumberForm(ModelForm):
    class Meta:
        model = PhoneNumber
        fields = '__all__'


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
