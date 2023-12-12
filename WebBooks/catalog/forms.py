from django import forms
from datetime import date

class AuthorsForm(forms.Form):
    name = forms.CharField(label="Имя автора")
    last_name = forms.CharField(label="Фамилия автора")
    date_of_birth = forms.DateField(label="Дата рождения автора",
                                    initial=format(date.today()),
                                    widget=forms.DateInput(attrs={'type': 'date'}))
    date_of_beath = forms.DateField(label="Дата смерти автора",
                                    initial=format(date.today()),
                                    widget=forms.DateInput(attrs={'type': 'date'}))