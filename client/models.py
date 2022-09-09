from django.db import models

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    bottles_ordered= models.IntegerField(default=1)
    photo = models.ImageField(verbose_name="фото", upload_to="Photos", null=True, blank=True)
