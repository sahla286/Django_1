from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}))
    description = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Description'}))
    date = forms.DateField(widget=forms.SelectDateWidget(attrs={'class': 'form-control'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control'}))
