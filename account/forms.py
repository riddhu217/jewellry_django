from django import forms
from django.contrib.auth.forms import AuthenticationForm
from account.models import CustomUser


class RegistrationForm(forms.ModelForm):
    address = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control", "placeholder": "address"}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': "form-control", "placeholder": "confirm password"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': "form-control", "placeholder": "Enter Your  password"}))

    class Meta:
        model = CustomUser
        fields = ["username", "gender", "address", "city", "state", "email", "contact_number", "password"]

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {
                'class': "form-control",
                'placeholder': "Enter Your Name",
            }
        )
        self.fields['gender'].widget.attrs.update(
            {
                'class': "form-control",
                'placeholder': "Enter Your Gender",
            }
        )
        self.fields['city'].widget.attrs.update(
            {
                'class': "form-control",
                'placeholder': "Enter Your city",
            }
        )
        self.fields['state'].widget.attrs.update(
            {
                'class': "form-control",
                'placeholder': "Enter Your state",
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'class': "form-control",
                'placeholder': "Enter Your email'id",
            }
        )
        self.fields['contact_number'].widget.attrs.update(
            {
                'class': "form-control",
                'placeholder': "Enter Your Contact number",
            }
        )

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password == password2:
            return cleaned_data

    def save(self, commit=True):
        instance = super(RegistrationForm, self).save(commit=False)
        instance.set_password(self.cleaned_data["password"])
        return super(RegistrationForm, self).save(commit=commit)


class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {
                'class': "form-control",
                'placeholder': "Enter Your Username ",
            }
        )
        self.fields['password'].widget.attrs.update(
            {
                'class': "form-control",
                'placeholder': "Enter Your Password ",
            }
        )
