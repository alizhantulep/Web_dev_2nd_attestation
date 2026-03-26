from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Product, Category
from django.http import HttpResponse
def product_list(request):
    products = Product.objects.all()
    return JsonResponse([p.to_json() for p in products], safe=False)

def product_detail(request, id):
    try:
        product = Product.objects.get(id=id)
        return JsonResponse(product.to_json())
    except Product.DoesNotExist:
        return JsonResponse(
            {'error': 'Product not found', 'id': id}, 
            status=404
        )
def category_list(request):
    categories = Category.objects.all()
    return JsonResponse([c.to_json() for c in categories], safe=False)

def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    return JsonResponse(category.to_json())

def category_products(request, id):
    category = get_object_or_404(Category, id=id)
    products = category.products.all()
    return JsonResponse([p.to_json() for p in products], safe=False)

def index(request):
    return HttpResponse("<h1>Welcome to Shop Back API</h1><p>Try /api/products/</p>")