# Generated by Django 2.0.2 on 2018-02-02 10:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Care', '0003_auto_20180202_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_of_Birth',
            field=models.DateField(blank=True),
        ),
    ]