from django import forms
from django.core import validators

class FeedbackForm(forms.Form):
    name = forms.CharField()
    rollno = forms.IntegerField()
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea, 
                               validators=[validators.MaxLengthValidator(40)]) # parameter to validate field
    
    # def clean_name(self):   # clean_ name is fixed, django callled this method automatically
    #     inputname = self.cleaned_data['name'] # cleaned_date is a dictionary ... fixed name
    #     print("*****validating name field*******")
    #     if len(inputname)<4:
    #         raise forms.ValidationError("char should be greater than 4")
    #     return inputname
    
