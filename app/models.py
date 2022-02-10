from tkinter import CASCADE
from django.db import models

# Create your models here.

class employee(models.Model):
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    emp_id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.firstname

class projects(models.Model):
    project_name = models.CharField(max_length=10)
    project_id = models.CharField(max_length=10)
    emp_id = models.ForeignKey(employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.project_name




