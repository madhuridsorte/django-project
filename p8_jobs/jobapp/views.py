from django.shortcuts import render
from jobapp.models import HydJobs,BangaloreJobs,PuneJobs


def homepage_view(request):
    return render(request, 'testapp\index.html')
    

def HybJobs_view(request):
    job_list = HydJobs.objects.all()
    my_dict = {"job_list":job_list}
    return render(request, 'testapp\hybjobs.html', my_dict)
    
