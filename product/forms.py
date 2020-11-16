from django import forms
from product.models import FeedBack
from product.models import BillingAddress


class BillingAddressForm(forms.ModelForm):
    Address = forms.CharField(
        widget=forms.Textarea(attrs={'class': "form-control", "placeholder": "Enter your Address"}))

    class Meta:
        model = BillingAddress
        fields = ["fname", "lname","Address", "city", "zip", "state", "contact_no", "email"]

    def __init__(self, *args, **kwargs):
        super(BillingAddressForm, self).__init__(*args, **kwargs)
        self.fields['fname'].widget.attrs.update(
            {
                'class': "form-control",
                'placeholder': "Enter Your FirstName",
            }
        )
        self.fields['lname'].widget.attrs.update(
            {
                'class': "form-control",
                'placeholder': "Enter Your LastName",
            }
        )
        self.fields['city'].widget.attrs.update(
            {
                'class': "form-control",
                'placeholder': "Enter Your City",
            }
        )
        self.fields['state'].widget.attrs.update(
            {
                'class': "form-control",
                'placeholder': "Enter Your state",
            }
        )
        self.fields['zip'].widget.attrs.update(
            {
                'class': "form-control",
                'placeholder': "Enter Your zip",
            }
        )
        self.fields['contact_no'].widget.attrs.update(
            {
                'class': "form-control",
                'placeholder': "Enter Your Contact Number",
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'class': "form-control",
                'placeholder': "Enter Your email",
            }
        )


class FeedBackForm(forms.ModelForm):
    feedback = forms.CharField(
        widget=forms.Textarea(attrs={'class': "form-control", "placeholder": "Please Enter Your FeedBack...", }))

    class Meta:
        model = FeedBack
        fields = ["name", "city", "contact_no", "feedback"]

    def __init__(self, *args, **kwargs):
        super(FeedBackForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {
                'class': "form-control",
                'placeholder': "Enter Your Name",
            }
        )
        self.fields['city'].widget.attrs.update(
            {
                'class': "form-control",
                'placeholder': "Enter Your City",
            }
        )
        self.fields['contact_no'].widget.attrs.update(
            {
                'class': "form-control",
                'placeholder': "Enter Your Contact Number",
            }
        )
