from django import forms

BROWSER_DATETIME_FORMAT = '%Y-%m-%dT%H:%M'


class CreateForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Имя')
    email = forms.EmailField(required=True, label='Email')
    text = forms.CharField(max_length=3000, required=False, label='Текст',
                           widget=forms.Textarea)
