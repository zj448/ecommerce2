from django.shortcuts import render
from .models import Product

# 商品列表视图
def product_list(request):
    products = Product.objects.all()  # 获取所有商品
    return render(request, 'store/product_list.html', {'products': products})

