from django import forms
from app17.models import EmployeeModel


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeModel
        fields = ["idno","name","email","salary"]