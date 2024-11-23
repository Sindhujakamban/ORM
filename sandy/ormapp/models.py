
from django.db import models
from django.contrib import admin
class bank_loan(models.Model):
	Name=models.CharField(max_length=10)
	loan_amount=models.IntegerField(primary_key="Refno")
	mobile_number=models.FloatField()
	DoB=models.DateField()
	Email=models.EmailField()
class bank_loanAdmin(admin.ModelAdmin):
	list_display=('Name','loan_amount','mobile_number','DoB','Email')



