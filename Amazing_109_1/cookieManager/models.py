from django.db import models

# Create your models here.


class Product(models.Model):  
    ProductID =  models.IntegerField()
    ProductName = models.TextField()  
    ProductPrice = models.DecimalField(max_digits=19, decimal_places=2)
    InventoryAmount = models.IntegerField()



class Customer(models.Model):
    CustomerID = models.IntegerField()
    CustomerName = models.TextField()  
    Gender = models.TextField()
    pos_po = models.DecimalField(max_digits=19, decimal_places=2)
    CLV = models.DecimalField(max_digits=19, decimal_places=2)

class MarketingIndex(models.Model):  
    CustomerID = models.IntegerField()
    ForecastPurchaseProb = models.DecimalField(max_digits=19, decimal_places=2)
    CLV = models.DecimalField(max_digits=19, decimal_places=2)
    WalletShare = models.DecimalField(max_digits=19, decimal_places=2)
    CategoryDemandShare = models.DecimalField(max_digits=19, decimal_places=2)
    ProportionofPositiveComment = models.DecimalField(max_digits=19, decimal_places=2)

class CustomerPurchaseInfo(models.Model):  
    CustomerID = models.IntegerField()
    ProductID =  models.IntegerField()
    PurchaseQuantity = models.IntegerField() 
    PurchasePrice = models.IntegerField() 
    Comment = models.TextField()
    Date = models.IntegerField()


