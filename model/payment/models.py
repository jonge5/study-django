from django.db import models

from member.models import Member
from model.models import Period
from product.models import Product


class Payment(Period):
    PAYMENT_STATUS = [
        (-1, '결제 실패'),
        (0, '결제 대기중'),
        (1, '결제 완료'),
    ]

    total_price = models.IntegerField(blank=False, null=False)
    payment_status = models.IntegerField(blank=False, null=False, choices=PAYMENT_STATUS, default=0)
    member = models.ForeignKey(Member, blank=False, null=False, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, blank=False, null=False, on_delete=models.PROTECT)

    def __str__(self):
        return self.total_price

    class Meta:
        ordering = ['-id']
        db_table = 'tbl_payment'
