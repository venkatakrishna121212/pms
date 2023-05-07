from django import forms
from .models import StudentDB, Edit_Details, Notifications
from django.contrib.auth.forms import AuthenticationForm

class RegisterForm(forms.ModelForm):
    class Meta:
        model = StudentDB
        widgets = {
            's_password': forms.PasswordInput(),
            's_confirm_password' : forms.PasswordInput(),
            'dob': forms.TextInput(attrs={'placeholder': 'MM/DD/YYYY'}),
        }
        fields = ['s_username', 's_name', 's_password', 's_confirm_password', 'dob', 'emailid', 'contactno']
        labels = {
            's_username': 'Username',
            's_name': 'Name',
            's_password': 'Password',
            's_confirm_password': 'Confirm Password',
            'dob': 'Date of Birth',
            'emailid': 'Email Address',
            'contactno': 'Contact Number',
        }


class Loginform(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))
    def clean(self):
        pass

class EditForm(forms.ModelForm):
    class Meta :
        model = StudentDB
        fields=['s_name','emailid','resume']
    def clean(self):
        pass

'''class NotifyStudent(forms.ModelForm):
    class Meta:
        model=Notifications
        fields=['n_text','new']
    def clean(self):
        pass'''

class Registerform(forms.Form):
    def is_valid(self):
        pass
