# Create your models here.
from django.db import models


# Create your models here.


class UserDetails(models.Model):
    user_id = models.AutoField(db_column="User_id", primary_key=True)
    name = models.CharField(db_column="Name", max_length=20)
    email = models.CharField(db_column="Email", max_length=254)
    password = models.CharField(db_column="Password", max_length=20)
    zipcode = models.IntegerField(null=True, db_column="Zipcode")

    def __str__(self):
        return self.name


class TaxDetails(models.Model):
    name = models.ForeignKey(UserDetails, on_delete=models.CASCADE, default=False)
    financial_year = models.DateField()
    age_group = models.CharField(max_length=5)
    category_emp_or_pen = models.CharField(max_length=30)
    regime = models.CharField(max_length=20)

    salary_income = models.IntegerField(null=True)
    other_income = models.IntegerField(null=True)
    gross_total_income = models.IntegerField(null=True)

    standard_deduction = models.IntegerField(null=True)
    professional_tax = models.IntegerField(null=True)
    house_rent_exemption = models.IntegerField(null=True)
    home_loan = models.IntegerField(null=True)
    deductions_u_80c = models.IntegerField(null=True)
    nps_u_80c = models.IntegerField(null=True)
    deductions_u_80d = models.IntegerField(null=True)
    deductions_u_80tta = models.IntegerField(null=True)
    deductions = models.IntegerField(null=True)

    taxable_income = models.IntegerField(null=True)

    tax_on_taxable_income = models.IntegerField(null=True)
    rebate_u_87a = models.IntegerField(null=True)
    surcharge_on_tax = models.IntegerField(null=True)
    education_cess = models.IntegerField(null=True)
    total_tax = models.IntegerField(null=True)
    tax_paid = models.IntegerField(null=True)
    balance_tax_to_be_paid = models.IntegerField(null=True)


class UserFeedback(models.Model):
    name = models.ForeignKey(UserDetails, on_delete=models.CASCADE, default=False)
    email = models.EmailField(max_length=254)
    description = models.CharField(max_length=200)


class CarouselImages(models.Model):
    photo = models.ImageField(upload_to="photo", blank=True, null=True)
    description = models.CharField(max_length=300)


class TaxSavingsGuide(models.Model):
    photo = models.ImageField(upload_to="photo", blank=True, null=True)
    card_title = models.CharField(max_length=50)
    card_description = models.CharField(max_length=200)


class TaxSlabRates(models.Model):
    REGIME_STATUS = (
        ("New Regime", "New Regime"),
        ("Old Regime", "Old Regime"),
    )

    AGE_GROUP = (
        ("For All Age Groups", "For All Age Groups"),
        ("Below 60", "Below 60"),
        ("60 to 80", "60 to 80"),
        ("Above 80", "Above 80"),
    )

    RATES_STATUS = (
        ("0%", "Nil"),
        ("5%", "5%"),
        ("10%", "10%"),
        ("15%", "15%"),
        ("20%", "20%"),
        ("30%", "30%"),
    )

    regime = models.CharField(
        max_length=20,
        choices=REGIME_STATUS,
        blank=True,
        default=True,
        help_text="regime status new or old",
    )

    age_group = models.CharField(
        max_length=20,
        choices=AGE_GROUP,
        blank=True,
        default="s",
        help_text="Age Group of People",
    )

    rates = models.CharField(
        max_length=20,
        choices=RATES_STATUS,
        blank=True,
        default="0",
        help_text="Tax Slab Rates",
    )

    slabs = models.CharField(max_length=30, help_text="Tax Slabs")

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.slabs
