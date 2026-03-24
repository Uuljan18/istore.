from django.db import models
from product.models import Product 

class Cart(models.Model):
    session_key = models.CharField(max_length=40, null=True, blank=True)  
    products = models.ManyToManyField(Product, through="CartItem")

    def __str__(self):
        return f"Cart {self.id}"

    # общая сумма корзины
    def get_total_price(self):
        total = 0
        for item in self.items.all():
            total += item.product.price * item.quantity
        return total

    # добавить товар
    def add_product(self, product_id, quantity=1):
        item, created = CartItem.objects.get_or_create(
            cart=self,
            product_id=product_id
        )
        if not created:
            item.quantity += quantity
        else:
            item.quantity = quantity
        item.save()

    # удалить товар
    def remove_product(self, product_id):
        CartItem.objects.filter(cart=self, product_id=product_id).delete()


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

    @property
    def total_price(self):
        return self.quantity * self.product.price