from django.contrib import admin
from .models import (
    UserDetails,
    TaxDetails,
    UserFeedback,
    CarouselImages,
    TaxSavingsGuide,
    TaxSlabRates,
)

# Register your models here.
admin.site.register(UserDetails)
admin.site.register(UserFeedback)


@admin.register(TaxDetails)
class TaxDetailsAdmin(admin.ModelAdmin):
    pass


@admin.register(TaxSlabRates)
class TaxSlabRatesAdmin(admin.ModelAdmin):
    list_display = ("regime", "slabs", "rates", "age_group")
    list_filter = ("regime", "age_group")


@admin.register(TaxSavingsGuide)
class TaxSavingsGuideAdmin(admin.ModelAdmin):
    list_display = ("photo", "card_title", "card_description")
    fields = ["photo", "card_title", "card_description"]


@admin.register(CarouselImages)
class CarouselImagesAdmin(admin.ModelAdmin):
    list_display = ("photo", "description")
