from django.db import models

# 商品模型
class Product(models.Model):
    name = models.CharField(max_length=100)  # 商品名称
    description = models.TextField()  # 商品描述
    price = models.DecimalField(max_digits=10, decimal_places=2)  # 商品价格
    stock = models.IntegerField()  # 商品库存
    image = models.ImageField(upload_to='product_images/')  # 商品图片

    def __str__(self):
        return self.name

# 订单模型
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # 关联商品
    quantity = models.IntegerField()  # 商品数量
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # 总价，自动计算
    customer_name = models.CharField(max_length=100)  # 客户姓名
    shipping_address = models.CharField(max_length=255)  # 收货地址

    def save(self, *args, **kwargs):
        # 在保存订单前计算总价
        self.total_price = self.product.price * self.quantity
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return f"Order for {self.customer_name} - {self.product.name}"
