from django import forms

class Checkout_contact_form(forms.Form):
    name   = forms.CharField(required=True)
    phone  = forms.CharField(required=True)
    adress = forms.CharField(required=True)
    comment = forms.CharField(required=False)