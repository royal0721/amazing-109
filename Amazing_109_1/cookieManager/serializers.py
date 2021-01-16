from rest_framework import serializers
from cookieManager.models import Customer, CustomerPurchaseInfo, MarketingIndex, Product
import json

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Product
        fields = ['ProductID', 'ProductName','ProductPrice','InventoryAmount']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Customer
        fields = ['CustomerID', 'CustomerName','Gender','pos_po','CLV']

class MarketingIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model  = MarketingIndex
        fields = ['CustomerID', 'ForecastPurchaseProb','CLV','WalletShare','CategoryDemandShare','ProportionofPositiveComment',]

class CustomerPurchaseInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model  = CustomerPurchaseInfo
        fields = ['CustomerID', 'ProductID','PurchaseQuantity','PurchasePrice','Comment','Date',]
