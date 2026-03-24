from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Cart
from .serializers import CartSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    # добавить товар через API
    @action(detail=True, methods=['post'])
    def add_product(self, request, pk=None):
        cart = self.get_object()
        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity', 1))
        cart.add_product(product_id, quantity)
        serializer = CartSerializer(cart, context={'request': request})
        return Response(serializer.data)

    # удалить товар через API
    @action(detail=True, methods=['post'])
    def remove_product(self, request, pk=None):
        cart = self.get_object()
        product_id = request.data.get('product_id')
        cart.remove_product(product_id)
        serializer = CartSerializer(cart, context={'request': request})
        return Response(serializer.data)