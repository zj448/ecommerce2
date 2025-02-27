from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),  # 首页显示商品列表
]
