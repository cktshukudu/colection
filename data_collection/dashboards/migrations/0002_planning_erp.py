# Generated by Django 4.0.6 on 2022-09-14 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='planning_erp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yes', models.CharField(max_length=1)),
                ('no', models.CharField(max_length=1)),
            ],
        ),
    ]
