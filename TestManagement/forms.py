from django import forms
from TestManagement.models import APIProject


class ProjectForm(forms.ModelForm):


    class Meta:
        model = APIProject
        fields = ["name", "describe", "status"]