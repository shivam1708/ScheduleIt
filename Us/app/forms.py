from django import forms
from django.contrib.auth.models import User
from app.models import UserProfileInfo,CouncilProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        help_texts = {
            'username': None,
        }
        model = User
        fields = ('first_name','last_name','username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('pointer','phone_no','profile_pic',)

class CouncilForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        help_texts = {
            'username': None,
        }
        model = User
        fields = ('username','email','password')
