from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def get_available_products(self):
        '''Gets products of current category with quantity=0'''
        return Product.object.filter(category=self, quantity__gte=0)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    category = models.ForeignKey(Category, null=True)
    f = models.ManyToManyField