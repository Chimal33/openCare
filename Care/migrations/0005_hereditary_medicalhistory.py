# Generated by Django 2.0.2 on 2018-02-02 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Care', '0004_auto_20180202_1049'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hereditary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diseases', models.CharField(blank=True, max_length=200)),
                ('generalAssessments', models.TextField(blank=True, max_length=200)),
                ('functional_Assessments', models.TextField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_group', models.CharField(blank=True, max_length=200)),
                ('allergies', models.CharField(blank=True, max_length=200)),
                ('regular_medications', models.CharField(blank=True, max_length=200)),
                ('current_or_recurringInjuries', models.CharField(blank=True, max_length=200)),
                ('disabilities', models.CharField(blank=True, max_length=200)),
                ('passedIllness', models.CharField(blank=True, max_length=200)),
                ('imunizations', models.CharField(blank=True, max_length=200)),
                ('healthRick_Assesments', models.TextField(blank=True, max_length=200)),
            ],
        ),
    ]
