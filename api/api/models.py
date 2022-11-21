from django.db import models

#create company Model.
 
class CompanyModel(models.Model):
	company_id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 100)
	location = models.CharField(max_length = 100)
	about = models.TextField()
	domain = models.CharField(max_length=100,choices=(('IT','IT'),('Non IT','No IT')))
	added_date = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.name + ' '+ self.location

#create Employee Model.
class EmployeeModel(models.Model):
	name = models.CharField(max_length = 100)
	email = models.CharField(max_length = 100)
	address = models.CharField(max_length = 100)
	phone = models.CharField(max_length = 10)
	about = models.TextField()
	position = models.CharField(max_length=100,choices=(('Manager','Manager'),('Software Developer','SD'),('Team Lead','TL')))

	company = models.ForeignKey(CompanyModel,on_delete = models.CASCADE)