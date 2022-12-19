from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=40, required=True)
    email = forms.EmailField(required=True)
    mensaje = forms.CharField(widget=forms.Textarea)