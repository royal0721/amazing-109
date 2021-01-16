from django.shortcuts import render
from rest_framework import viewsets
from cookieManager.serializers import ProductSerializer, CustomerSerializer, MarketingIndexSerializer, CustomerPurchaseInfoSerializer
from cookieManager.models import Product, Customer, MarketingIndex, CustomerPurchaseInfo
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from rest_framework.parsers import JSONParser
import json
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
"""
Product API
"""
@csrf_exempt
def product_list(request):
    """
    List all code products, or create a new snippet.
    """
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def product_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return JsonResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        #serializer = ProductSerializer(product, data={'content': 'foo bar'}, partial=True)

        serializer = ProductSerializer(product, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        product.delete()
        return HttpResponse(status=204)

class ProductPartialUpdateView(GenericAPIView, UpdateModelMixin):
    '''
    You just need to provide the field which is to be modified.
    '''
    lookup_field = 'ProductID'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def patch(self, request, *args, **kwargs):
        # print(request.POST)
        request.data._mutable = True
        id = request.get_full_path_info()[-6:-1]
        #拿到資料庫裡的值
        product = Product.objects.get(ProductID = id)
        newValue = product.InventoryAmount + int(request.POST.get('InventoryAmount'))
        request.POST.__setitem__('InventoryAmount', newValue)
        request.data._mutable = False

        return self.partial_update(request, *args, **kwargs)
    
# class ArticleDetail(generic.DetailView):
#     template_name = 'blog/article-detail.html' # 用來 render 的 template 
#     context_object_name = 'article' # 傳給 template 的 context 名稱

#     def get_object(self, queryset=None): # 依照傳入的資料，拿取單一一筆資料
#         pk = self.kwargs.get("pk")
#         return Article.objects.get(id=pk)
"""
Customer API
"""
@csrf_exempt
def customer_list(request):
    """
    List all code products, or create a new snippet.
    """
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def customer_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        customer = Customer.objects.get(CustomerID=pk)
    except Customer.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(customer)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(customer, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        customer.delete()
        return HttpResponse(status=204)


"""
MarketingIndex API
"""
@csrf_exempt
def marketingIndex_list(request):
    """
    List all code products, or create a new snippet.
    """
    if request.method == 'GET':
        marketIndex = MarketingIndex.objects.all()
        serializer = MarketingIndexSerializer(marketIndex, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MarketingIndexSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def marketingIndex_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        marketIndex = MarketingIndex.objects.get(pk=pk)
    except MarketingIndex.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MarketingIndexSerializer(marketIndex)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MarketingIndexSerializer(marketIndex, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        marketIndex.delete()
        return HttpResponse(status=204)

"""
CustomerPurchaseInfo API
"""

@csrf_exempt
def customerPurchaseInfo_list(request):
    """
    List all code products, or create a new snippet.
    """
    if request.method == 'GET':
        customerpurchase = CustomerPurchaseInfo.objects.all()
        serializer = CustomerPurchaseInfoSerializer(customerpurchase, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CustomerPurchaseInfoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def customerPurchaseInfo_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        customerpurchase = CustomerPurchaseInfo.objects.get(CustomerID=pk)
    except CustomerPurchaseInfo.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CustomerPurchaseInfoSerializer(customerpurchase)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CustomerPurchaseInfoSerializer(customerpurchase, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        customerpurchase.delete()
        return HttpResponse(status=204)


#index
#index
def index(request):
    ctx ={}
    if request.POST:
        ctx['username'] = request.POST['username']
        password = request.POST['password']
        if ctx['username']=='admin':
            if password=='12345':
                print(request.user.username)
                request.session['username'] = 'admin' 
                return render(request, 'pages/index.html',ctx)
        else :
            return redirect('/')
    else:    
        if request.session['username']!='admin':
            return redirect('/')
        else:
            request.session['username']='admin'
            ctx['username']=request.session['username']
            return render(request, 'pages/index.html',ctx)

def crmPage(request):
    # j = product_list(request).content.decode()[2:-2].split('}, {')
    ctx ={}
    if request.session['username']!='admin':
        return redirect('/')
    else:
        ctx['username']=request.session['username']
        customerList = customer_list(request).content.decode()
        productList = product_list(request).content.decode()
        purchaseInfo = customerPurchaseInfo_list(request).content.decode()
        return render(request, 'pages/crmPage.html', { 'productList': json.dumps(productList), 'purchaseInfo': json.dumps(purchaseInfo), 'customerList': json.dumps(customerList),'ctx':ctx})

def discountPage(request):
    ctx ={}
    if request.session['username']!='admin':
        return redirect('/')
    else:
        ctx['username']=request.session['username']
        customerList = customer_list(request).content.decode()
        productList = product_list(request).content.decode()
        purchaseInfo = customerPurchaseInfo_list(request).content.decode()
        return render(request, 'pages/discountPage.html', { 'productList': json.dumps(productList), 'purchaseInfo': json.dumps(purchaseInfo), 'customerList': json.dumps(customerList),'ctx':ctx})

def inventoryPage(request):
    # j = product_list(request).content.decode()[2:-2].split('}, {')
    ctx ={}
    if request.session['username']!='admin':
        return redirect('/')
    else:
        ctx['username']=request.session['username']
        productList = product_list(request).content.decode()
        purchaseInfo = customerPurchaseInfo_list(request).content.decode()
        return render(request, 'pages/inventoryPage.html', { 'productList': json.dumps(productList), 'purchaseInfo': json.dumps(purchaseInfo),'ctx':ctx})



def login_form(request):
    return render(request, 'pages/login_form.html')

def login(request):
    ctx ={}
    if request.POST:
        ctx['username'] = request.POST['username']
        password = request.POST['password']
        if ctx['username']=='admin':
            if password=='12345':
                return render(request, 'pages/index.html')


def logout(request):
    request.session['username']=''
    return redirect('/')
