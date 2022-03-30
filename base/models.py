from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Vendor(models.Model):
    fname = models.CharField(max_length = 50)
    sname = models.CharField(max_length = 50)
    phone_num = models.CharField(max_length = 10)
    item_name = models.CharField(max_length = 50)
    item_img = models.ImageField(verbose_name="Item Name",upload_to="images/")
    item_price = models.IntegerField(default=0)
    item_type = models.CharField(max_length = 50)

    def __str__(self):
        return self.fname

