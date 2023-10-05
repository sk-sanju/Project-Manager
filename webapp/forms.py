from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Record
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

# - Register/Create a user

class CreateUserFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1','password2']

# - Login a User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

# - Create a record
class CreateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['project_name', 'project_subject','project_description','client_firstname','client_lastname','client_contact','project_link']

# - Update a record
class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['project_name', 'project_subject','project_description','client_firstname','client_lastname','client_contact','project_link']