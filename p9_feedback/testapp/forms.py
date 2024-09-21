from django import forms
from django.core import validators

def start_with_d(value):
    print("************inside start_with_d***************")
    if value[0].lower()!='d':
        raise forms.ValidationError("name should be start with d or D")
def gmail_validator(value):
    print("************inside gmail_validator***************")
    if value[-10:] !="@gmail.com":
        raise forms.ValidationError("mail extension should be @gmail.com ")
        

class FeedbackForm(forms.Form):
    name = forms.CharField(validators=[start_with_d]) # created our own validator 
    rollno = forms.IntegerField()
    email = forms.EmailField(validators=[gmail_validator])
    feedback = forms.CharField(widget=forms.Textarea, 
                               validators=[validators.MaxLengthValidator(40)]) # parameter to validate field
    
    # def clean_name(self):   # clean_ name is fixed, django callled this method automatically
    #     inputname = self.cleaned_data['name'] # cleaned_date is a dictionary ... fixed name
    #     print("*****validating name field*******")
    #     if len(inputname)<4:
    #         raise forms.ValidationError("char should be greater than 4")
    #     return inputname
    
