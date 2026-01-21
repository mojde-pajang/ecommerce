from rest_framework import permissions, viewsets
from django.http import HttpRequest
from rest_framework.response import Response
from main.models import Customer, Product, Order
from rest_framework.decorators import action
from main.serializers import CustomerSerializer, OrderSerializer, ProductSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from uuid import UUID
from django.core.exceptions import ValidationError

# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # permission_classes = [permissions.IsAuthenticated]


class ProductViewSet(viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail= False, methods= ['get'])
    def all(self, request= HttpRequest):
        queryset = self.get_queryset()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        

    @action(detail= True, methods= ['get'])
    def get_product_detail(self, request= HttpRequest, pk=None):
        try:
            UUID(pk)
        except Exception as e:
            return Response(
                {'error': 'Invalid ID format'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        queryset = self.get_queryset()
        product = get_object_or_404(queryset, pk= pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


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




