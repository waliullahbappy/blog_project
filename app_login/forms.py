from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django.http.response import StreamingHttpResponse
from app_login.models import UserProfile


class UserProfileChange(UserChangeForm):
    class Meta:
        model=User
        fields=('username', 'email','first_name','last_name','password')
        
class ProfilePic(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields =['profile_pic']
    def __str__(self):
        return self.User
    
