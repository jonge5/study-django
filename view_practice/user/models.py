from django.db import models


class User(models.Model):
    user_email = models.CharField(null=False, blank=False, max_length=255)
    user_password = models.CharField(null=False, blank=False, max_length=255)
    user_name = models.CharField(null=False, blank=False, max_length=255)
    user_status = models.BooleanField(null=False, blank=False, default=False)

    class Meta:
        db_table = 'tbl_user'
        ordering = ['-id']