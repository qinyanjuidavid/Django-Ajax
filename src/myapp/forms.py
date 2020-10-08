from django.forms import ModelForm
from django import forms
from myapp.models import Task,MyUser

class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=('title',)
    widgets={
    'title':forms.TextInput(attrs={"class":'form-control'})
    }
class UserAddForm(ModelForm):
    class Meta:
        model=MyUser
        fields=['name','phone_number','email']
