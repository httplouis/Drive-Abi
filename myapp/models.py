from django.db import models

from django.contrib.humanize.templatetags.humanize import intcomma

class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    seats = models.IntegerField(default=0)
    img = models.URLField(default=' ')
    description = models.TextField(max_length=1000, default=' ')

    def formatted_price(self):
        return intcomma(self.price)
    
    def __str__(self):
        return str(self.year) + ' ' + self.brand + ' ' + self.model




class Membership(models.Model):
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    fname = models.CharField(max_length=100, null=False, blank=False)  
    lname = models.CharField(max_length=100, null=False, blank=False)
    cell = models.IntegerField()


    def __str__(self):
        return self.fname

class Addbook(models.Model):
    author = models.CharField(max_length=100, null=False, blank=False)
    title = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.title

class sign1(models.Model):
    user = models.CharField(max_length=100, null=False, blank=False)
    passw = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.user + ' ' + self.passw
