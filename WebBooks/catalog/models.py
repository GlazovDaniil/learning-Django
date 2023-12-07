from django.db import models

# Create your models here.


class BookInstance(models.Model):
    due_back = models.DateField()

class Status(models.Model):
    status = models.CharField(max_length=30)
class Autor(models.Model):
    name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()

class Meta:
    ordering = ["-my_field_name"]
def __str__ (self):
    return self.field_name

class Language(models.Model):
    name = models.CharField(max_length=30)

class Genre(models.Model):
    name = models.CharField(max_length=30)

class Books(models.Model):
    title = models.CharField(max_length=50)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    nummary = models.CharField(max_length=30)
    inprint = models.CharField(max_length=30)
    ISBN = models.BigIntegerField()
    genre = models