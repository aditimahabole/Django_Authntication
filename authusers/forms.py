from django import forms
from .models import Person

class SignupForm(forms.ModelForm):
    USER_TYPES = [
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
    ]

    user_type = forms.ChoiceField(choices=USER_TYPES, widget=forms.RadioSelect)

    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'profile_picture', 'username', 'email', 'password','confirm_password' ,'address_line1', 'city', 'state', 'pincode']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
