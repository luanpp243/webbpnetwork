from django.contrib import admin

from products import models
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','code_number','brand','status','price',)
    search_fields = ('name','code_number','brand','status',)

admin.site.register(models.Product,ProductAdmin)
