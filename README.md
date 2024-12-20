# Ex02 Django ORM Web Application
## Date: 18/11/2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM

![alt text](<Screenshot (10).png>)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
models.py

from django.db import models
from django.contrib import admin
class bank loan (models.Model):
	Name=models.CharField(max_length=10)
	Loan amount =models.IntegerField(primary_key="Refno")
	Mobile number=models.FloatField()
	DoB=models.DateField()
	Email=models.EmailField()
class StudentAdmin(admin.ModelAdmin):
	list_display=('Name','loan amount','mobile number','DoB','Email')

admin.py

from django.contrib import admin
from .models import Student,StudentAdmin
admin.site.register(Student,StudentAdmin)
```


## OUTPUT

![alt text](<Screenshot (13).png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully