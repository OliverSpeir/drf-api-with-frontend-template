from django import forms
from django.forms import ModelForm
from .models import Item


class CustomForm(ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'creator', 'image_url', 'description')
        widgets = {
            'name': forms.TextInput(attrs={'class': "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg"
                                                    " focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 "
                                                    "dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 "
                                                    "dark:text-white dark:focus:ring-blue-500 "
                                                    "dark:focus:border-blue-500"}),
            'creator': forms.Select(attrs={'class': "bg-gray-50 border border-gray-300 text-gray-900 text-sm "
                                                     "rounded-lg focus:ring-blue-500 focus:border-blue-500 "
                                                     "block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 "
                                                     "dark:placeholder-gray-400 dark:text-white "
                                                     "dark:focus:ring-blue-500 dark:focus:border-blue-500"}),
            'image_url': forms.TextInput(attrs={'class': "bg-gray-50 border border-gray-300 text-gray-900 text-sm "
                                                         "rounded-lg focus:ring-blue-500 focus:border-blue-500 "
                                                         "block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 "
                                                         "dark:placeholder-gray-400 dark:text-white "
                                                         "dark:focus:ring-blue-500 dark:focus:border-blue-500"}),
            'description': forms.TextInput(attrs={'class': "block w-full p-4 text-gray-900 border border-gray-300 "
                                                           "rounded-lg bg-gray-50 sm:text-md focus:ring-blue-500 "
                                                           "focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600"
                                                           " dark:placeholder-gray-400 dark:text-white "
                                                           "dark:focus:ring-blue-500 dark:focus:border-blue-500"}),
        }
