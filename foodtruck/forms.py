from django import forms

class AddressForm(forms.Form):
    input_address = forms.CharField(label='Enter address here!', max_length=100)