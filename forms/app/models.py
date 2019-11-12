from django.db import models

class StudentModel(models.Model):
    regno= models.IntegerField(primary_key=True)
    name=models.CharField(max_length=25)
    email=models.EmailField(max_length=30,unique=True)
    password=models.CharField(max_length=8)
    mobile_number = models.IntegerField(max_length=11)
    image=models.ImageField(upload_to='images')

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True,default=False)