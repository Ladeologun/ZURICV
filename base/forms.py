from django import forms

class Contactform(forms.Form):
    fullname = forms.CharField(max_length=255)
    email = forms.EmailField(label="E-Mail")
    gender = forms.ChoiceField(choices=[("M","Male"),("F","Female")])
    subject = forms.CharField(max_length=255,required=False)
    body =  forms.CharField(widget=forms.Textarea)