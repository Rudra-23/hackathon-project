from django.db import models

class Doctor(models.Model):
    userid = models.IntegerField(primary_key=True)
    f_name = models.CharField(max_length=20, blank=False, null=True)
    l_name = models.CharField(max_length=20, blank=False, null=True)
    age = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=144, blank=True, null=True)
    phone_number = models.CharField(max_length=45, blank=False, null=True)
    email = models.CharField(max_length=45, blank=False, null=True)
    time = models.IntegerField(blank=False, null=True)
    special = models.CharField(max_length = 100, blank=False, null=False)
    
    class Meta:
        db_table = 'doctor'