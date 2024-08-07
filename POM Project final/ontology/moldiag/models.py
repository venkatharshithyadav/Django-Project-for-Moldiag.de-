from django.db import models

# Create your models here.

class TodoItem(models.Model):
    title = models.CharField(max_length = 200)
    completed = models.BooleanField(default = False)

class HPOEntry(models.Model):
    code = models.CharField(max_length=50)
    term = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.term

class Diagnosis(models.Model):
    code = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.code

class GeneTest(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


    