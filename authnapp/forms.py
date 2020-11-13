from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm
import hashlib
import random

from .models import ShopUser, ShopUserProfile


class ShopUserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(ShopUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = ShopUser
        fields = ("username", "password")


class ShopUserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(ShopUserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.help_text = ""

    def clean_age(self):
        data = self.cleaned_data["age"]
        if data < 18:
            raise forms.ValidationError(
                "У вас еще молого на губах не обсохло!")
        return data

    def clean_first_name(self):
        name = self.cleaned_data['first_name']
        if name == 'Santa':
            raise forms.ValidationError('Санты не существует, малыш')
        return name

    def save(self):
        user = super(ShopUserRegisterForm, self).save()
        user.is_active = False
        salt = hashlib.sha1(
            str(random.random()).encode('utf-8')).hexdigest()[6:]
        user.activation_key = hashlib.sha1(
            (user.email+salt).encode('utf-8')).hexdigest()
        user.save()
        return user

    class Meta:
        model = ShopUser
        fields = ("username", "first_name", "password1",
                  "password2", "email", "age", "avatar")


class ShopUserEditForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(ShopUserEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.help_text = ""

    def clean_age(self):
        data = self.cleaned_data["age"]
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")
        return data

    def clean_first_name(self):
        name = self.cleaned_data['first_name']
        if name == 'Santa':
            raise forms.ValidationError('Санты не существует, малыш')
        return name

    class Meta:
        model = ShopUser
        fields = ("username", "first_name", "email", "age", "avatar")


class ShopUserProfileEditForm(forms.ModelForm):
    class Meta:
        model = ShopUserProfile
        fields = ("tagline", "aboutMe", "gender")

    def __init__(self, *args, **kwargs):
        super(ShopUserProfileEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
