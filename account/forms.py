from django import forms
from django.contrib.auth.models import User
from .models import Profile


class DateInput(forms.DateInput):
    input_type = 'date'

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', 
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', 
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match')
        return cd['password2']

class ProfileRegistrationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('nic', 'paye', 'birth_date', 'photo')
        widgets = {
            'birth_date': DateInput()
            }

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('paye', 'photo')