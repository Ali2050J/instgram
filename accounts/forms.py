from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Profile


class UserRegisterForm(forms.ModelForm):
    password2 = forms.CharField(label='')

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        help_texts = {'username': None}
        labels = {'username': '', 'email': '', 'password': ''}

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(
            attrs={
                'class': 'border w-60 p-1 pl-3 bg-gray-50 border-gray-200 rounded-sm placeholder:text-xs outline-none',
                'placeholder': 'Username', 'autocomplete': 'off'})
        self.fields['email'].widget = forms.EmailInput(
            attrs={
                'class': 'border w-60 p-1 pl-3 bg-gray-50 border-gray-200 rounded-sm placeholder:text-xs outline-none',
                'placeholder': 'Email'})
        self.fields['password'].widget = forms.PasswordInput(
            attrs={
                'class': 'border w-60 p-1 pl-3 bg-gray-50 border-gray-200 rounded-sm placeholder:text-xs outline-none',
                'placeholder': 'Password', 'type': 'password', 'autocomplete': 'off'})
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={
                'class': 'border w-60 p-1 pl-3 bg-gray-50 border-gray-200 rounded-sm placeholder:text-xs outline-none',
                'placeholder': 'Confirm Password', 'type': 'password'})

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('This Email Is Already Exist.')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).exists()
        if user:
            raise ValidationError('This Username Is Already Exist.')
        return username

    def clean(self):
        cd = super().clean()
        password1 = cd.get('password')
        password2 = cd.get('password2')

        if (password1 and password2) and (password1 != password2):
            raise ValidationError('Password must match.')

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number, username, or email '}))
    password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))


class UserEditProfileForm(forms.ModelForm):
    username = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = Profile
        fields = ('full_name', 'bio', 'gender', 'image')
