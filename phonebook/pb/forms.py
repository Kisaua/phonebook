from django import forms
from .models import Contact

class ContactCreateForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['fname','lname','city','address', 'phone', 'contactUrl', 'image']