# Generated by Django 4.1.4 on 2023-02-23 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaxDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('financial_year', models.CharField(max_length=8)),
                ('age_group', models.CharField(max_length=5)),
                ('category_emp_or_pen', models.CharField(max_length=30)),
                ('regime', models.CharField(max_length=20)),
                ('salary_income', models.IntegerField(null=True)),
                ('other_income', models.IntegerField(null=True)),
                ('gross_total_income', models.IntegerField(null=True)),
                ('standard_deduction', models.IntegerField(null=True)),
                ('professional_tax', models.IntegerField(null=True)),
                ('house_rent_exemption', models.IntegerField(null=True)),
                ('home_loan', models.IntegerField(null=True)),
                ('deductions_u_80c', models.IntegerField(null=True)),
                ('nps_u_80c', models.IntegerField(null=True)),
                ('deductions_u_80d', models.IntegerField(null=True)),
                ('deductions_u_80tta', models.IntegerField(null=True)),
                ('deductions', models.IntegerField(null=True)),
                ('taxable_income', models.IntegerField(null=True)),
                ('tax_on_taxable_income', models.IntegerField(null=True)),
                ('rebate_u_87a', models.IntegerField(null=True)),
                ('surcharge_on_tax', models.IntegerField(null=True)),
                ('education_cess', models.IntegerField(null=True)),
                ('total_tax', models.IntegerField(null=True)),
                ('tax_paid', models.IntegerField(null=True)),
                ('balance_tax_to_be_paid', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('user_id', models.AutoField(db_column='User_id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=20)),
                ('email', models.CharField(db_column='Email', max_length=254)),
                ('password', models.CharField(db_column='Password', max_length=20)),
                ('zipcode', models.IntegerField(db_column='Zipcode', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]
