from django import forms
from .models import Projects

class ProjectModelForm(forms.ModelForm):
    class Meta:
        model=Projects
        fields='__all__'