from django.contrib import admin
from.models import Submission
# Register your models here.

class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'date', 'next_followup_date', 'additional_data')

admin.site.register(Submission,SubmissionAdmin)