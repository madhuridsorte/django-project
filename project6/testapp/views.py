from django.shortcuts import render
from testapp.models import Student

def student_view(request):
    # student_list = Student.objects.all()
    student_list = Student.objects.filter(marks__lt=50)
    my_dict = {'student_list': student_list }
    return render(request, 'testapp\data.html', my_dict)