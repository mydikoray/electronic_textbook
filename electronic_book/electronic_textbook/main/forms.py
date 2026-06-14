from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class KyrgyzUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='Колдонуучу аты',
        help_text='',
        widget=forms.TextInput(attrs={
            'placeholder': 'Колдонуучу атыңызды жазыңыз'
        })
    )

    password1 = forms.CharField(
        label='Сыр сөз',
        help_text='',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Сыр сөз жазыңыз'
        })
    )

    password2 = forms.CharField(
        label='Сыр сөздү кайталоо',
        help_text='',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Сыр сөздү кайра жазыңыз'
        })
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class KyrgyzAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='Колдонуучу аты',
        widget=forms.TextInput(attrs={
            'placeholder': 'Колдонуучу атыңызды жазыңыз'
        })
    )

    password = forms.CharField(
        label='Сыр сөз',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Сыр сөзүңүздү жазыңыз'
        })
    )

    error_messages = {
        'invalid_login': 'Колдонуучу аты же сыр сөз туура эмес.',
        'inactive': 'Бул аккаунт активдүү эмес.',
    }