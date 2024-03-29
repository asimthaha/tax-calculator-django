# Generated by Django 4.1.7 on 2023-05-29 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxdetails',
            name='age_group',
            field=models.CharField(blank=True, choices=[('For All Age Groups', 'For All Age Groups'), ('Below 60', 'Below 60'), ('60 to 80', '60 to 80'), ('Above 80', 'Above 80')], default='Below 60', help_text='Age Group of People', max_length=19, null=True),
        ),
        migrations.AlterField(
            model_name='taxdetails',
            name='category_emp_or_pen',
            field=models.CharField(blank=True, choices=[('Employee/Pensioner', 'Employee/Pensioner'), ('Other', 'Other')], default='Employee/Pensioner', help_text='Category of People', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='taxdetails',
            name='financial_year',
            field=models.CharField(blank=True, choices=[('2024-2023', '2024-2023'), ('2023-2022', '2023-2022'), ('2022-2021', '2022-2021'), ('2021-2020', '2021-2020')], default='2024-2023', help_text='Financial Year', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='taxdetails',
            name='regime',
            field=models.CharField(blank=True, choices=[('New Regime', 'New Regime'), ('Old Regime', 'Old Regime')], default='New Regime', help_text='regime status new or old', max_length=20),
        ),
    ]
