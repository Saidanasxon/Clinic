from django import forms
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm


class LoginForm(forms.Form):
    username = forms.CharField(label='Username kiriting')
    password = forms.CharField(label='Parolingizni kiriting',widget=forms.PasswordInput)

class RegisterForm(forms.ModelForm):
    username=forms.CharField(label='Login kiriting')
    password=forms.CharField(label='Parol yarating', widget=forms.PasswordInput )
    password2=forms.CharField(label='Parolni tasdiqlang', widget=forms.PasswordInput )

    class Meta:
        model= User
        fields=['username' ,'email','password','password2','first_name','last_name']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password']!= cd['password2']:
           
            raise forms.ValidationError('Parollar bir biriga mos emas')
        
        else:
            return cd['password2']
        
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Bunday email allaqachon mavjud')
        return email
from django.contrib.auth import get_user_model
class ProfileForm(forms.ModelForm):
    username=forms.CharField(label='Username', disabled=True)
    email = forms.CharField(label='Email', disabled=True)

    class Meta:
        model = get_user_model()
        fields=('first_name', 'last_name', 'username', 'email')