from django.db import models

# Create your models here.




class Name(models.Model):
    firstName = models.CharField(max_length=100, null=True)
    lastName = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.firstName+" "+self.lastName

class PhoneNumber(models.Model):
    country_code = (
        ('+966', 'Saudi Arabia'),
        ('+991', 'y'),
    )
    countryCode = models.CharField(max_length=200, null=True, choices=country_code)
    mNumber = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.countryCode+self.mNumber

class Contact(models.Model):
    name = models.ForeignKey(Name, on_delete=models.CASCADE)
    phoneNumber = models.ForeignKey(PhoneNumber, on_delete=models.CASCADE)

    def __str__(self):
        return self.name.firstName+" "+self.name.lastName

