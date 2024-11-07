from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.FloatField()
    designation = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    projects = models.ManyToManyField('Project')


    def __str__(self):
        return self.name   

class Project(models.Model):
    NEW = 'NEW'
    ON_GOING = 'ON-GOING'
    ENDED = 'ENDED'

    STATUS_CHOICE=[
        (NEW,'New'),
        (ON_GOING, 'On-going'),
        (ENDED,'Ended'),
    ]

    name = models.CharField(max_length=100)
    team = models.ManyToManyField('Employee',related_name='assigned_projects')
    team_lead = models.ForeignKey('Employee', related_name='led_projects',on_delete=models.SET_NULL,null=True)
    status = models.CharField(max_length=20,choices=STATUS_CHOICE,default=NEW)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name
    



