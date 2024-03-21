from django.db import models

from cart.models import Cart
from model.models import Period
from product.models import Product


class CartDetail(Period):
    cart = models.ForeignKey(Cart, on_delete=models.PROTECT, null=False)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(null=False, default=1)
    # 게시 중(0), 결제 완료(1), 결제 취소(-1) - Period에 선언된 매니저 사용 안 함
    status = models.SmallIntegerField(null=False, default=0)

    class Meta:
        db_table = 'tbl_cart_detail'
        ordering = ['-id']  # 최신 내역이 맨 위에 표시
