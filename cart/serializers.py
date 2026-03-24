from rest_framework import serializers
from .models import Cart, CartItem
from product.serializers import ProductSerializer

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = CartItem
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()
    total_items = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'session_key', 'items', 'total_items', 'total_price']

    def get_total_price(self, obj):
        return obj.get_total_price()

    def get_total_items(self, obj):
        return sum(item.quantity for item in obj.items.all())