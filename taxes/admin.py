from django.contrib import admin
from admincharts.admin import AdminChartMixin
from .models import *



# Register your models here.
@admin.register(TaxDetails)
class TaxDetailsChartModel(AdminChartMixin, admin.ModelAdmin):
    list_display = ('name', 'financial_year', 'age_group', 'category_emp_or_pen', 'regime', 'salary_income',
                    'other_income', 'standard_deduction', 'professional_tax', 'house_rent_exemption',
                    'home_loan', 'deductions_u_80c', 'nps_u_80c', 'taxable_income', 'tax_on_taxable_income',
                    'rebate_u_87a', 'surcharge_on_tax', 'education_cess', 'total_tax')
    list_filter = ('financial_year', 'age_group', 'category_emp_or_pen', 'regime')
    search_fields = ('name', 'financial_year', 'age_group', 'category_emp_or_pen', 'regime')


@admin.register(TaxSlabRates)
class TaxSlabRatesAdmin(admin.ModelAdmin):
    list_display = ("regime", "slabs", "rates", "age_group")
    list_filter = ("regime", "age_group")


@admin.register(TaxSavingsGuide)
class TaxSavingsGuideAdmin(admin.ModelAdmin):
    list_display = ("photo", "card_title", "card_description")
    fields = ["photo", "card_title", "card_description"]
    list_filter = ("card_title", "photo")


@admin.register(CarouselImages)
class CarouselImagesAdmin(admin.ModelAdmin):
    list_display = ("photo", "description")
    fields = ["photo", "description"]


@admin.register(UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
    list_filter = ("zipcode", "name")
    search_fields = ("name", "email")
    


@admin.register(UserFeedback)
class UserFeedbackAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
    list_filter = ("description", "name")
