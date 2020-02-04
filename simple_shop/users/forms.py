from django import forms
from .models import User


# class LoginForm(forms.modelForm):
#     # email = forms.EmailField()
#     # password = forms.PasswordInput()
#
#     class Meta:
#         model = User
#         fields = ['email', 'password']
#         widgets = {
#             'email': forms.TextInput(verbose_name='Почта', attrs={
#                 'type': 'email', 'id': 'inputEmail',
#                 'class': 'form-control', 'placeholder': 'Email',
#             }),
#             'password': forms.TextInput(attrs={
#                 'type': 'password', 'id': 'inputPassword',
#                 'class': 'form-control', 'placeholder': 'Пароль',
#             })
#         }
