# lines 2 - 18 added in template
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': ("bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500"
                      " focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 "
                      "dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"),
            'placeholder': 'username',
            "required": True
            })
        self.fields['password1'].widget.attrs.update({
            'class': ("bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500"
                      " focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 "
                      "dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"),
            'placeholder': 'password',
            "required": True,
            'maxlength': '22',
            'minlength': '8'
            })
        self.fields['password2'].widget.attrs.update({
            'class': ("bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 "
                      "focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 "
                      "dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"),
            'placeholder': 'password',
            "required": True,
            'maxlength': '22',
            'minlength': '8'
            })
        self.fields['email'].widget.attrs.update({
            'class': ("bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 "
                      "focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 "
                      "dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"),
            'placeholder': 'email',
            })

    class Meta:
        model = CustomUser
        fields = ('email', "username")


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("email", "username")


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': ("bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500"
                      " focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 "
                      "dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"),
            'placeholder': 'username',
        })
        self.fields['password'].widget.attrs.update({
            'class': ("bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500"
                      " focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 "
                      "dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"),
            'placeholder': 'password',
            })

    class Meta:
        model = CustomUser
        fields = ("email", "username")

