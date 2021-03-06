from django import forms

class studentForm(forms.Form):
    rno=forms.IntegerField(max_value=999,label="Roll No",min_value=100)
    name=forms.CharField(max_length=30,label="Full Name")
    contactno=forms.IntegerField(max_value=9999999999,label="Mobile No",min_value=6000000000)
    email=forms.EmailField(label="College Email ID")
    password=forms.CharField(max_length=8,widget=forms.PasswordInput,min_length=8)

    groups=(("cse","CSE"),("it","Information"))
    branch=forms.ChoiceField(choices=groups)

    #for Radio buttons
    gen=(("male","MALE"),("female","FEMALE"))
    gender=forms.ChoiceField(choices=gen,widget=forms.RadioSelect)

    #for Check Box
    python=forms.CharField(widget=forms.CheckboxInput)
    Django=forms.CharField(widget=forms.CheckboxInput)
