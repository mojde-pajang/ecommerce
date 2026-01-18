from rest_framework import permissions, viewsets
from django.http import HttpRequest
from main.models import Customer, Product, Order
from rest_framework.decorators import action
from main.serializers import CustomerSerializer, OrderSerializer, ProductSerializer

# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # permission_classes = [permissions.IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

class OrderViewSet(viewsets.GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    #Like regular actions, extra actions may be intended for either a single object,
    # or an entire collection. To indicate this, set the detail argument to True or False
    @action(detail=False, methods=['post'])
    def place_order(self, http_request: HttpRequest):

        mail = http_request.data.get('mail')
        product_ids = http_request.data.get('product_ids', [])
        quantity = http_request.data.get('quantity')

