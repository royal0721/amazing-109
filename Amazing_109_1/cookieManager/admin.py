from django.contrib import admin

# Register your models here.
from .models import Product,Customer,MarketingIndex,CustomerPurchaseInfo


admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(MarketingIndex)
admin.site.register(CustomerPurchaseInfo)