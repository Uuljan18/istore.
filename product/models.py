from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name="название категории", max_length=100)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories', null=True)
    name = models.CharField(verbose_name="название подкатегории", max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(verbose_name="название", max_length=100)
    price = models.DecimalField(verbose_name="цена", max_digits=10, decimal_places=2)
    color = models.CharField(verbose_name="цвет", max_length=50)
    memory = models.CharField(verbose_name="память", max_length=50)
    simcard = models.CharField(verbose_name="сим-карта", max_length=50)
    image = models.ImageField(verbose_name="изображение", upload_to='products/', null=True, blank=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='products', null=True)
    

    def __str__(self):
        return self.name