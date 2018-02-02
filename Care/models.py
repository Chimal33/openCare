from django.db import models
from django.utils import timezone


class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    full_Name= models.CharField(max_length=200,blank=True)
    age= models.IntegerField(blank=True)
    sex= models.CharField(max_length=200,blank=True)
    date_of_Birth= models.DateField(blank=True)
    home_Address= models.CharField(max_length=200,blank=True)
    phone_Number= models.CharField(max_length=20,blank=True)
    next_of_kin= models.CharField(max_length=200,blank=True)
    email_Address=models.EmailField(max_length=200,blank=True)

    created_date = models.DateField(
            default=timezone.now)
    def __str__(self):
        return self.full_Name

class MedicalHistory(models.Model):
     blood_group = models.CharField(max_length=200,blank=True)
     allergies = models.CharField(max_length=200,blank=True)
     regular_medications=models.CharField(max_length=200,blank=True)
     current_or_recurringInjuries=models.CharField(max_length=200,blank=True)
     disabilities= models.CharField(max_length=200,blank=True)
     passed_Illness=models.CharField(max_length=200,blank=True)
     imunizations=models.CharField(max_length=200,blank=True)
     health_Risks_Assesments =models.TextField(max_length=200,blank=True)

class Hereditary(models.Model):
    diseases = models.CharField(max_length=200,blank=True)
    generalAssessments = models.TextField(max_length=200,blank=True)
    functional_Assessments = models.TextField(max_length=200,blank=True)
