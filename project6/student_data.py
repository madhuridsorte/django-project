import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project6.settings')

import django
django.setup()

from testapp.models import Student
from faker import Faker
from random import *
fakegen = Faker()

def phonenumber_gen():
    d1 = randint(6,9)
    num = str(d1)
    for i in range(9):
        num = num+ str(randint(6,9))
    return int(num)

fake = Faker()
def populate(n):
    for i in range(n):
        frollno = fake.random_int(min=1, max=999)
        fname = fake.name()
        fdob = fake.date()
        fmarks = fake.random_int(min=1, max=100)
        femail = fake.email()
        fphonenumber = phonenumber_gen()
        faddress = fake.address()
        
        student_record = Student.objects.get_or_create(rollno=frollno, name=fname, dob=fdob, marks=fmarks, 
                                                       email=femail,phonenumber=fphonenumber, address= faddress)
        
n = int(input("Insert the number of records: "))
populate(n)    
print(f"{n} numbers of record inserted successfully !") 
        

