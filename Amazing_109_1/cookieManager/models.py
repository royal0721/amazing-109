from django.db import models

class Product(models.Model):  
    ProductName = models.TextField()  
    InventoryAmount = models.IntegerField()
    ProductID =  models.IntegerField()
    ProductPrice = models.DecimalField(max_digits=19, decimal_places=2, default=0.0)

class Customer(models.Model):
    CustomerID = models.IntegerField()
    CustomerName = models.TextField()  
    Gender = models.TextField()
    pos_po = models.DecimalField(max_digits=19, decimal_places=2, default=0.0)
    CLV = models.DecimalField(max_digits=19, decimal_places=2, default=0.0)

class MarketingIndex(models.Model):  
    CustomerID = models.IntegerField()
    ForecastPurchaseProb = models.DecimalField(max_digits=19, decimal_places=2, default=0.0)
    CLV = models.DecimalField(max_digits=19, decimal_places=2, default=0.0)
    WalletShare = models.DecimalField(max_digits=19, decimal_places=2, default=0.0)
    CategoryDemandShare = models.DecimalField(max_digits=19, decimal_places=2, default=0.0)
    ProportionofPositiveComment = models.DecimalField(max_digits=19, decimal_places=2, default=0.0)

class CustomerPurchaseInfo(models.Model):  
    CustomerID = models.IntegerField()
    ProductID =  models.IntegerField()
    PurchaseQuantity = models.IntegerField() 
    PurchasePrice = models.IntegerField() 
    Comment = models.TextField()
    Date = models.IntegerField()
    pos_or_neg = models.DecimalField(max_digits=19, decimal_places=2, default=0.0)

