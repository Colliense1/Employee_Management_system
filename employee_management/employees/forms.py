from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'phone_number', 'address', 'gender', 'salary', 'designation', 'short_description']
        widgets = {
            'address': forms.TextInput(attrs={'size': '100'}),
            'short_description': forms.TextInput(attrs={'size': '200'}),
            #'salary': forms.NumberInput(attrs={'readonly': 'readonly'}),
            #'designation': forms.Select(attrs={'readonly': 'readonly'}),
        }
        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['salary'].widget.attrs['readonly'] = 'readonly'
            self.fields['designation'].widget.attrs['disabled'] = 'disabled'
            self.fields['salary'].required = False
            self.fields['designation'].required = False

    