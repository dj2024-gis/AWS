# Generated by Django 5.1.2 on 2024-11-06 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0004_remove_employee_projects_employee_projects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='team',
            field=models.ManyToManyField(null=True, related_name='assigned_projects', to='Myapp.employee'),
        ),
    ]