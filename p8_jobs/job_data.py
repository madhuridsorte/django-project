import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'p8_jobs.settings')

import django
django.setup()

from jobapp.models import *
from faker import Faker
from random import *

fake = Faker()

def phonenumber_gen():
    d1 = randint(6,9)
    num = str(d1)
    for i in range(9):
        num = num+ str(randint(6,9))
    return int(num)

["date", "company", "title","eligibility", "address","email", "phonenumber"]
def populate(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements = ["Manager", "Team-Lead", "Software Engineer", "System Engineer"])
        feligibility = fake.random_element(elements = ["M.TECH", "MCA", "BTECH", "PHD"])
        faddress = fake.address()
        femail = fake.email()
        fphonenumber = phonenumber_gen()
        
        HydJobs_record = HydJobs.objects.get_or_create(date=fdate, company=fcompany, title=ftitle, eligibility=feligibility, 
                                                       address=faddress, email=femail, phonenumber=fphonenumber)
        
n = int(input("Insert the number of records: "))
populate(n)    
print(f"{n} numbers of record inserted successfully !") 
        

