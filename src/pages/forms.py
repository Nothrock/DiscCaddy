from django import forms
from pages.models import User, CheckIn


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'profile_pic', 'email', 'password', 'city', 'age', 'bio', 'pdga_member', 'pdga_number']
