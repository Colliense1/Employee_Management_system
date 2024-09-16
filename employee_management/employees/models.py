from django.db import models

# Create your models here.
class Employee(models.Model):

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    Designation_choices = [
        ('manager', 'Manager'),
        ('full stact developer', 'Full Stack Developer'),
        ('android developer', 'Android Developer'),
        ('web developer', 'Web Developer'),
        ('frontend developer', 'Frontend Developer'),
        ('web designer', 'Web Designer'),
    ]

    name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    salary = models.CharField(max_length=10)
    designation = models.CharField(max_length=50, choices=Designation_choices, default='manager')
    short_description = models.TextField()

    def __str__(self):
        return self.name