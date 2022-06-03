from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField

UserModel = get_user_model()

class UserCreationForm(forms.ModelForm):
    error_messages ={
        'password_mismatch':("Two password fields didn't match.")
    }
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        label="Password Confirmation",
        widget=forms.PasswordInput(),
        help_text=("Enter same password as above for verification")
    )

    class Meta:
        model = UserModel
        fields = ("userID",)
    
    def clean_password(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                'password1 and password2 must be matched'
            )
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(label=("Password"),
        help_text=("Raw passwords are not stored, so there is no way to see "
                    "this user's password, but you can change the password "
                    "using <a href=\"password/\">this form</a>."))
    class Meta:
        model = UserModel
        fields = ('userID', 'password', 'is_active')
    def clean_password(self):
        return self.initial["password"]