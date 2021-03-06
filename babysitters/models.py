from django.db import models
from datetime import datetime

# Create your models here.
class Babysitter(models.Model):
    list_display = ('firstName', 'lastName', 'minderType')
    firstName = models.CharField(max_length=50, blank=True, null=True)
    lastName = models.CharField(max_length=50, blank=True, null=True)
    minderType = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='images')
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    address1 = models.CharField(max_length=100, null=True)
    address2 = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=20, null=True)
    county = models.CharField(max_length=100, null=True)
    postcode = models.CharField(max_length=7, null=True)
    facebook = models.CharField(max_length=50, null=True)
    twitter = models.CharField(max_length=50, null=True)
    fact1 = models.CharField(max_length=140, null=True)
    fact2 = models.CharField(max_length=140, null=True)
    fact3 = models.CharField(max_length=140, null=True)
    description = models.CharField(max_length=140, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=0)
    smoking = models.CharField(max_length=140, null=True)
    driver = models.CharField(max_length=140, null=True)
    car = models.CharField(max_length=140, null=True)
    experience = models.CharField(max_length=140, null=True)
    expAges = models.CharField(max_length=140, null=True)
    prefLoc = models.CharField(max_length=140, null=True)
    verified = models.CharField(max_length=8,blank=True, null=True)
    donator = models.CharField(max_length=140, null=True)
    gender = models.CharField(max_length=6, null=True)
    age = models.CharField(max_length=2, null=True)
    max_num =  models.IntegerField(blank=False)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.firstName + ' ' + self.lastName
        
class Education(models.Model):
    babysitter = models.ForeignKey(Babysitter)
    school = models.CharField(max_length=50)
    qualification = models.CharField(max_length=50)
    fieldOfStudy = models.CharField(max_length=50)
    dateFrom = models.DateField(auto_now=False, auto_now_add=False)
    dateTo = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    current = models.BooleanField(default=False)
    graduated = models.BooleanField(default=False)
    def __str__(self):
        return self.school
        
class Work(models.Model):
    babysitter = models.ForeignKey(Babysitter)
    family = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    dateFrom = models.DateField(auto_now=False, auto_now_add=False)
    dateTo = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    current = models.BooleanField(default=False)
    def __str__(self):
        return self.family
        
class Reference(models.Model):
    babysitter = models.ForeignKey(Babysitter)
    refFamily = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    email = models.CharField(max_length=50, blank=True, null=True)
    reference = models.CharField(max_length=300)
    date = models.DateField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.refFamily