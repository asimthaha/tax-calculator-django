from django.contrib import admin
from jazzmin.utils import attr
from .models import (
    UserDetails,
    TaxDetails,
    UserFeedback,
    CarouselImages,
    TaxSavingsGuide,
    TaxSlabRates,
)

# Register your models here.


@admin.register(TaxDetails)
class TaxDetailsAdmin(admin.ModelAdmin):
    list_display = ('financial_year', 'regime', 'age_group',"total_tax")
    list_filter = ('regime', 'age_group')
    
    fieldsets = (
        (None, {
            'fields': ('financial_year', 'age_group', 'category_emp_or_pen','regime')
        }),
        ('Income', {
            'fields': ('salary_income', 'other_income','total_tax')
        }),
        ('Deductions', {
            'fields': ('standard_deduction', 'professional_tax','house_rent_exemption','home_loan', 'deductions_u_80c','nps_u_80c',)
        }),
        ('Taxable', {
            'fields': ('taxable_income', 'tax_on_taxable_income','rebate_u_87a','surcharge_on_tax', 'education_cess')
        }),
    )

@admin.register(TaxSlabRates)
class TaxSlabRatesAdmin(admin.ModelAdmin):
    list_display = ("regime", "slabs", "rates", "age_group")
    list_filter = ("regime", "age_group")

@admin.register(TaxSavingsGuide)
class TaxSavingsGuideAdmin(admin.ModelAdmin):
    list_display = ("photo", "card_title", "card_description")
    fields = ["photo", "card_title", "card_description"]
    list_filter = ("card_title","photo")

@admin.register(CarouselImages)
class CarouselImagesAdmin(admin.ModelAdmin):
    list_display = ("photo", "description")
    fields = ["photo","description"]

@admin.register(UserDetails)
class UserDetails(admin.ModelAdmin):
    list_display = ("name","email")
    list_filter = ("zipcode","name")
    
@admin.register(UserFeedback)  
class UserFeedbackAdmin(admin.ModelAdmin):
   list_display = ("name","email")
   list_filter = ("description","name")
   