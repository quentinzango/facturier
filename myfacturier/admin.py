from django.contrib import admin
from .models import *

# Register your models here.


class AdminCustomer(admin.ModelAdmin):
    list_display =  ('name', 'email', 'phone', 'age')
    
    
class AdminInvoice(admin.ModelAdmin):
    list_display = ('customer', 'saved_by', 'invoice_date_time', 'total', 'last_updated_date', 'paid', 'invoice_type', 'comments')




admin.site.register(Customer, AdminCustomer)
admin.site.register(Invoice, AdminInvoice)