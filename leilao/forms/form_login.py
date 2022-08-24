
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        help_text=(
            'Coloque seu Username aqui'
        ),
        error_messages={'required': 'Campo obrigatorio'},
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        error_messages={'required': 'Campo obrigatorio'},
    )
