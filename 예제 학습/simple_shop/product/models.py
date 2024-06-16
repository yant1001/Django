from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=256, verbose_name="상품명")
    product_price = models.IntegerField(verbose_name="상품가격")
    product_desc = models.TextField(verbose_name="상품설명")
    product_stock = models.IntegerField(verbose_name="상품재고")
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name="등록날짜")

    def __str__(self):
        return self.product_name

    class Meta:
        db_table="tb_product"
        verbose_name = "상품"
        verbose_name_plural = "상품"