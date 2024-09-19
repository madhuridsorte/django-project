from django.contrib import admin
from jobapp.models import HydJobs,BangaloreJobs,PuneJobs

class HydJobsAdmin(admin.ModelAdmin):
    list_display = ["date", "company", "title","eligibility", "address","email", "phonenumber"]
   
admin.site.register(HydJobs, HydJobsAdmin)

class BangaloreJobsAdmin(admin.ModelAdmin):
    list_display = ["date", "company", "title","eligibility", "address","email", "phonenumber"]
    
admin.site.register(BangaloreJobs, BangaloreJobsAdmin)

class PuneJobsAdmin(admin.ModelAdmin):
    list_display = ["date", "company", "title","eligibility", "address","email", "phonenumber"]
    
admin.site.register(PuneJobs, PuneJobsAdmin)
    
