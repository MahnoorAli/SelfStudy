from django.db import models
from datetime import datetime
from simple_history.models import HistoricalRecords


# Create your models here.

class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    timestamp = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.name


class User(models.Model):
    team_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)

    salary_per_day = models.IntegerField(default=0)
    total_working_days = models.IntegerField(default=30)

    department = models.ForeignKey(Department, models.DO_NOTHING)
    timestamp = models.DateTimeField(default=datetime.now())
    history = HistoricalRecords()

    def __str__(self):
        return self.first_name
