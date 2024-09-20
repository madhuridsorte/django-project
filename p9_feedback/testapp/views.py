from django.shortcuts import render
from testapp.forms import FeedbackForm

def feedback_view(request):
    submitted = False
    name = ''
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print("************student feedback data*******************")
            print("name: ", form.cleaned_data['name'])
            print("rollno: ", form.cleaned_data['rollno'])
            print("email: ", form.cleaned_data['email'])
            print("feedback: ", form.cleaned_data['feedback'])
            print("************end******************")
            submitted = True
            name = form.cleaned_data['name']
        else:
            print("******validation failed*******")
        
    form = FeedbackForm()
    return render(request, 'testapp/feedback.html', {'form':form, 'submitted':submitted,'name':name})
