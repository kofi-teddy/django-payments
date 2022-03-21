from django.db import models


class OrderDetails(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    country = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    city = models.CharField(max_length=255) 
    province = models.CharField(max_length=255) 
    address1 = models.CharField(max_length=255)   
    address2 = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    credit_card_number = models.CharField(max_length=255)
    expiration = models.CharField(max_length=255)
    name_on_card = models.CharField(max_length=255)
    cvv_number = models.CharField(max_length=255)
