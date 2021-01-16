from django.urls import path
from cookieManager import views
from django.conf.urls import url
urlpatterns = [
    path('product/', views.product_list),
    path('product/<int:pk>/', views.product_detail),
    # path('product/update-partial/<int:pk>', views.ProductPartialUpdateView.as_view(), name='order_amount'),
    url(r'^product/update-partial/(?P<ProductID>\d+)/$', views.ProductPartialUpdateView.as_view(), name='InventoryAmount'),



    path('customer/', views.customer_list),
    path('customer/<int:pk>/', views.customer_detail),

    path('marketingIndex/', views.marketingIndex_list),
    path('marketingIndex/<int:pk>/', views.marketingIndex_detail),

    path('customerPurchaseInfo/', views.customerPurchaseInfo_list),
    path('customerPurchaseInfo/<int:pk>/', views.customerPurchaseInfo_detail),

]