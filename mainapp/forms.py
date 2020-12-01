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

def csv_que_up(request):
    e_path = 'G:/projects/feedback/'
    l1,l2 = request.POST['csv'].split('/')
    csv_file = e_path+l1
    data = open(csv_file,'r')
    lst1 = []
    iterdata = iter(data)
    next(iterdata)
    for i in iterdata:
        i,j = i.split('\n')
        lst = [i for i in i.split(',')]
        lst1.append(lst)
    for i in lst1:
        que = FeedBack.objects.create(que_id=i[0],que=i[1])
        que.save()
    return True
