from django.db import models

# Create your models here.


class Details(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    email = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def is_chennai(self):
        return self.location == "chennai"

class Login(models.Model):
    detail = models.ForeignKey(Details)
    password=models.CharField(max_length=200)

    def __str__(self):
        return self.detail