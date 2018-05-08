from datetime import datetime
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import Permission, User
from django.utils import timezone


class Dept(models.Model):

    Dept_name= models.CharField(max_length=100)
    Dept_detail1= models.CharField(max_length=10000 , blank=True , null=True)
    Dept_detail2= models.TextField(max_length=10000 , blank=True , null=True)
    Dept_address1=models.CharField(max_length=1000 , blank=True , null=True)
    Dept_address2=models.CharField(max_length=1000 , blank=True , null=True)
    Dept_phone=models.IntegerField( blank=True , null=True)
    Dept_Fax=models.IntegerField( blank=True , null=True)
    Dept_email=models.EmailField(max_length=1000 , blank=True , null=True)
    Dept_image=models.FileField( blank=True , null=True)

    def __str__(self):
        return self.Dept_name

class Position(models.Model):

    Position_name= models.CharField(max_length=100)

    def __str__(self):
        return self.Position_name


class Prof(models.Model):

    user = models.ForeignKey(User, default=1)
    Department = models.ForeignKey(Dept,on_delete=models.CASCADE)
    Name= models.CharField(max_length=100)
    Designation = models.ForeignKey(Position,on_delete=models.CASCADE)
    Image = models.FileField()
    address1=models.CharField(max_length=1000 , blank=True , null=True)
    address2=models.CharField(max_length=1000 , blank=True , null=True)
    phone_office=models.IntegerField()
    phone_residency=models.IntegerField()
    email=models.EmailField(max_length=1000)
    Room_No=models.CharField(max_length=1000)
    Research_Interests=models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse('project:prof_detail' , kwargs={'pk': self.pk} )

    def __str__(self):
        return self.Name

class Facility(models.Model):

    Facility_dept = models.ForeignKey(Dept, on_delete=models.CASCADE)
    Facility_name= models.CharField(max_length=100)
    Facility_description = models.TextField(max_length=10000)

    def __str__(self):
        return self.Facility_name


class Publication(models.Model):

    Professor = models.ForeignKey(Prof,on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Detail = models.CharField(max_length=10000)
    Date = models.DateField(default=datetime.today())


    def get_absolute_url(self):
        return reverse('project:prof_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.Name


class Recognition(models.Model):

    Professor = models.ForeignKey(Prof,on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Detail = models.CharField(max_length=10000)
    Date = models.DateField(default=datetime.today())

    def get_absolute_url(self):
        return reverse('project:prof_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.Name


class Student(models.Model):

    Professor = models.ForeignKey(Prof, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Detail = models.CharField(max_length=10000)
    Start_date = models.DateField(default=datetime.today())
    End_date = models.DateField(default=datetime.today())

    def get_absolute_url(self):
        return reverse('project:prof_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.Name


class Teaching(models.Model):

    Professor = models.ForeignKey(Prof, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Detail = models.CharField(max_length=10000)
    Start_date = models.DateField(default=datetime.today())
    End_date = models.DateField(default=datetime.today())

    def get_absolute_url(self):
        return reverse('project:prof_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.Name


class Projects(models.Model):

    Funding_agency = models.CharField(max_length=100)
    Professor = models.ForeignKey(Prof, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Detail = models.CharField(max_length=10000)
    Start_date = models.DateField(default=datetime.today())
    End_date = models.DateField(default=datetime.today())

    def get_absolute_url(self):
        return reverse('project:prof_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.Name


class Experience(models.Model):

    Professor = models.ForeignKey(Prof, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Detail = models.CharField(max_length=10000)
    Start_date = models.DateField(default=datetime.today())
    End_date = models.DateField(default=datetime.today())

    def get_absolute_url(self):
        return reverse('project:prof_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.Name