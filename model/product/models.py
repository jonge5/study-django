from django.db import models

from model.models import Period
from product.managers import ProductManager


class Product(Period):
    product_name = models.TextField(null=False, blank=False)
    product_price = models.BigIntegerField(null=False, blank=False)
    product_discount = models.SmallIntegerField(null=False, blank=False, default=0)
    # 판매중 True, 판매 중지 False
    status = models.BooleanField(null=False, default=False)
    objects = models.Manager()
    sell_price_objects = ProductManager()

    class Meta:
        db_table = 'tbl_product'
        base_manager_name = 'sell_price_objects'
        