# Generated by Django 2.0.1 on 2018-01-12 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='dateTaken',
            field=models.DateTimeField(verbose_name='Date taken'),
        ),
    ]
