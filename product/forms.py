from django import forms
from product.models import FeedBack


class FeedBackForm(forms.ModelForm):
    feedback = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control", "placeholder":"Please Enter Your FeedBack...",}))

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
