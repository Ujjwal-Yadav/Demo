# Generated by Django 3.1.7 on 2021-04-06 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20210404_0821'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='rejected',
        ),
        migrations.AlterField(
            model_name='request',
            name='accepted',
            field=models.IntegerField(default=-1),
        ),
    ]