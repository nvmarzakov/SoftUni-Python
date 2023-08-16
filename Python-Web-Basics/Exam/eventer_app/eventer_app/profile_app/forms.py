from django import forms
from django.forms import PasswordInput

from .models import ProfileModel


class ProfileCreateForm(forms.ModelForm):
    password = forms.CharField(widget=PasswordInput(render_value=True))

    class Meta:
        model = ProfileModel
        exclude = ['first_name', 'last_name']


class ProfileEditForm(forms.ModelForm):
    password = forms.CharField(widget=PasswordInput(render_value=True))

    class Meta:
        model = ProfileModel
        fields = "__all__"

