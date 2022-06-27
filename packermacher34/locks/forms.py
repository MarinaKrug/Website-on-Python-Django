from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from locks.models import Contacts


class AddMessageForm(ModelForm):

    class Meta:
        model = Contacts
        fields = ['name', 'phone_number', 'date', 'time', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ваше имя'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ваш номер телефона'}),
            'date': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Удобная дата для записи'}),
            'time': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Удобное время'}),
            'message': forms.Textarea(attrs={'placeholder': 'Напишите тут ваше сообщение'})
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) > 25:
            raise ValidationError("Длина превышает 25 символов")
        return name



