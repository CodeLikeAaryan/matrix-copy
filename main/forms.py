from msilib.schema import File
from operator import imod
from attr import field
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PersonalFiles, Book


class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={'class': 'pass form-control w-full p-4 pr-12 text-sm rounded-lg', 'type': 'password',
                   'align': 'center', 'placeholder': 'Password', 'style': 'box-shadow: rgba(0, 0, 0, 0.12) 0 1px 4px'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(
            attrs={'class': 'pass form-control w-full p-4 pr-12 text-sm rounded-lg', 'type': 'password',
                   'align': 'center', 'placeholder': 'Confirm Password', 'style': 'box-shadow: rgba(0, 0, 0, 0.12) 0 1px 4px'}),
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control w-full p-4 pr-12 text-sm rounded-lg',
                'style': 'box-shadow: rgba(0, 0, 0, 0.12) 0 1px 4px',
                'placeholder': 'John Doe'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control w-full p-4 pr-12 text-sm rounded-lg',
                'style': 'box-shadow: rgba(0, 0, 0, 0.12) 0 1px 4px',
                'placeholder': 'johndoe@gmail.com'
            }),
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'description', 'cover')


class AddFile(forms.ModelForm):
    class Meta:
        model = PersonalFiles
        fields = ('title', 'category', 'cover')
