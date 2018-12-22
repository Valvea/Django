from django import forms

class LoginForm(forms.Form):
    username=forms.CharField(
        label='Логин',
        max_length=150,
        widget=forms.widgets.TextInput(
            attrs={
                'class': 'field field-password'
            }
        )
    )
    password = forms.CharField(
        label='Пароль',
        max_length=72,
        widget=forms.widgets.PasswordInput(
            attrs={
                'class':'field field-password'
            }
        )

    )