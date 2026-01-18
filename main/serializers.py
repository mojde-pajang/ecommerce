from main.models import Customer, Order, Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
     class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'
        model = Product
        fields = ['id', 'name', 'description', 'price']
  

class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        fields = ['id', 'email', 'first_name', 'last_name', 'is_active', 
                  'phone_number', 'address', 'phone_number', 'created_at']
        
class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    product = ProductSerializer(read_only=True)
    
    class Meta:
        model = Product
        fields = ['id', 'item_quantity', 'created_at', 'price']