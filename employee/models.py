from django.db import models

class Employee(models.Model):  
   
    name = models.CharField(max_length=100)  
    email = models.EmailField()  
    contact = models.CharField(max_length=15)  
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Fe-Male', 'Fe-male'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    dob = models.DateField()  
    class Meta:  
        db_table = "employee"  
# Create your models here.
