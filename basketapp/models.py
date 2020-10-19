from django.conf import settings
from django.db import models, reset_queries

from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name="basket")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(
        verbose_name="количество", default=0)
    add_datetime = models.DateTimeField(
        verbose_name="время добавления", auto_now_add=True)

    def total_quantity(self):
        result = 0
        for product in self:
            result+= product.quantity
        return result

    def total_price(self):
        result = 0
        for product in self:
            result+= product.product.price * product.quantity
        return result


    def __str__(self):
        return f'{self.user} - {self.product.name} - {self.quantity}'

