from django.contrib import admin
from .models import UserDetails, TaxDetails,UserFeedback
# Register your models here.
admin.site.register(UserDetails)
admin.site.register(UserFeedback)
admin.site.register(TaxDetails)