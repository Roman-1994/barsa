from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    age = models.IntegerField()
    date_birth = models.DateField()

#a = Employee.objects.filter(age=35)
#print(a.query)
