from django import forms
from django.contrib.auth.models import User
from newApp.models import UserExtension

#  This UserForm and UserExtensionForm are for admin User
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'is_superuser', 'email')

class UserExtensionForm(forms.ModelForm):
    # links = forms.URLField(required=False)
    # picture = forms.ImageField(required=False)
    class Meta:
        model = UserExtension
        fields = ('links', 'profile_pic')

