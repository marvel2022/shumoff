from django import forms

from .models import (
    Customer,
)


class CustomerForm(forms.ModelForm):
    message = forms.CharField(widget = forms.Textarea(attrs={ 'rows':"10", 'cols':"80", 'style':"width: 100%;", 'placeholder' : 'Сообщение ...'}), required=False)
    class Meta:
        model = Customer
        fields = ('user', 'name', 'phone', 'address',) 

        widgets = {
            # 'user'    : forms.Select(attrs={'placeholder' : 'Author'}),
            'user'    : forms.TextInput(attrs={'value' : '', 'class':"form-control", 'type':'hidden', 'id':'curront-user'}),
            'name'    : forms.TextInput(attrs={'type':'text', 'class':"form-control", 'placeholder' : 'имя'}),
            'phone'   : forms.TextInput(attrs={'type':'text', 'class':"form-control", 'placeholder' : 'Телефонный номер'}),
            'address' : forms.TextInput(attrs={'type':'text', 'class':"form-control", 'placeholder' : 'Адрес'}),
        }