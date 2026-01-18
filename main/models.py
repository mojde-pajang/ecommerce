from django.db import models
from django.contrib.auth.models import  AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import MinLengthValidator, MaxLengthValidator
import uuid

# Create your models here.
class Product (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, verbose_name="product name")
    description = models.TextField( verbose_name="product description")
    price = models.FloatField(verbose_name= "product price")

    #how the object is shown as text in Django admin, shell, logs and relations in admin
    def __str__(self):
        return self.name
    
    class Meta:
        #define how the model name appears to humans in Django’s UI

        #Used in Django Admin and forms
        verbose_name = "Product"
        verbose_name_plural = "Products"
    
class CustomerManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
 
        return self.create_user(email, password, **extra_fields)
    
    
class Customer(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Modification date")
    first_name = models.CharField(max_length=30, blank=True, null=True, verbose_name="First name")
    last_name = models.CharField(max_length=30, blank=True, null=True, verbose_name="Last name")
    phone_number = models.CharField(max_length=10, default="", blank=True, validators=[MinLengthValidator(10), MaxLengthValidator(10)])
    address = models.CharField(max_length=100, blank=True, null=True, verbose_name="Address")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomerManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []  # No username field required

    def __str__(self):
        return self.email
    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
    
class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    items = models.ForeignKey(Product, verbose_name= "Items", related_name= "products",  on_delete=models.RESTRICT)
    item_quantity = models.PositiveIntegerField(default=1, verbose_name= 'counts')
    customer = models.OneToOneField(Customer, related_name= "customer",  on_delete=models.RESTRICT  )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name= "Creation date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Modification date")
    total_price = models.FloatField(verbose_name= "order price")

    def __str__(self):
        return self.id
    
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    
