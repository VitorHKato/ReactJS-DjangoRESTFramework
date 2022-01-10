from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=300)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

class Employee(Person):
    position = models.CharField(max_length=200)

class Client(Person):
    contract_end_date = models.DateField()
    contract_start_date = models.DateField()
