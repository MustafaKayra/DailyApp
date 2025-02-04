from django import forms
from .models import Contact, Daily
from django.core.exceptions import ValidationError

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','subject','message']


class DailyForm(forms.ModelForm):
    class Meta:
        model = Daily
        fields = ['gratitude','field1','affirmations','field2','field3','field4','field5']