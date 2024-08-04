from django.db import models

# Create your models here.
class Submission(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    date = models.DateField()
    next_followup_date = models.DateField()
    additional_data = models.CharField(max_length=255)

    def _str_(self):
        return self.name 