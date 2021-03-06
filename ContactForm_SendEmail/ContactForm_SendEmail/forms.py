from django import forms

class contactFormEmail(forms.Form):
    fromemail = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea,required=True)