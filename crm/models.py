from django.db import models

# Create your models here.

class Order(models.Model):
    order_name = models.CharField(max_length=30, verbose_name= "slovo")

    def __str__(self):
        return self.order_name
    class Meta:
        verbose_name ="NewSlovo"
        verbose_name_plural = "Name"