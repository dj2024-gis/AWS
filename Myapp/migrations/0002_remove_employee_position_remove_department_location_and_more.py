# Generated by Django 5.1.2 on 2024-10-18 19:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='position',
        ),
        migrations.RemoveField(
            model_name='department',
            name='location',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='email',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='hire_date',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='employee',
            name='address',
            field=models.CharField(default='Unknown Address', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='designation',
            field=models.CharField(default='Unknown Address', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='name',
            field=models.CharField(default='Unknown Address', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.FloatField(),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('NEW', 'New'), ('ON-GOING', 'On-going'), ('ENDED', 'Ended')], default='NEW', max_length=20)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('team', models.ManyToManyField(related_name='assigned_projects', to='Myapp.employee')),
                ('team_lead', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='led_projects', to='Myapp.employee')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='projects',
            field=models.ManyToManyField(related_name='employees', to='Myapp.project'),
        ),
        migrations.DeleteModel(
            name='Position',
        ),
    ]
