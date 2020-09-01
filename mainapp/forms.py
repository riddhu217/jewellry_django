from django import forms
from mainapp.models import Contact


class ContactForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control","placeholder":"tell me about contact me",}))

    class Meta:
        model = Contact
        fields = ["name", "email", "phone", "desc"]

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {
                'class': "form-control",
                'placeholder': "Enter Your Name",
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'class': "form-control",
                'placeholder': "Enter Your email'id",
            }
        )
        self.fields['phone'].widget.attrs.update(
            {
                'class': "form-control",
                'placeholder': "Enter Your Contact Number",
            }
        )
