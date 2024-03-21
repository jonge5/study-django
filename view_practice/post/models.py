from django.db import models

from user.models import User


class Post(models.Model):
    post_title = models.CharField(max_length=80,blank=False,null=False)
    post_content = models.TextField(blank=False,null=False)
    post_status = models.BooleanField(blank=False,null=False)
    user = models.ForeignKey(User,on_delete=models.PROTECT)

    class Meta:
        db_table = 'tbl_post'
        ordering = ['-id']