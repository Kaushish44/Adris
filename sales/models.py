from django.db import models
from django.core.validators import RegexValidator,MinLengthValidator
#from django.contrib.auth import get_user


class customers(models.Model):
    Name = models.CharField(max_length = 100)
    Email = models.EmailField(max_length = 100)
    phone_regex = RegexValidator(regex=r'^\d{9,10}$')#, message= 'Phone number must be 10 digits long and', code = 'invalid_Phone')
    Phone = models.CharField(validators=[phone_regex,MinLengthValidator(10)],max_length=10, blank=False)
    
class orders(models.Model):
    customer = models.ForeignKey(customers, on_delete=models.CASCADE)
    food_ordered = models.CharField(max_length =900)
    bill = models.IntegerField()
    owner = models.CharField(max_length =10)
    date = models.DateTimeField(auto_now_add = True)
    
class menu(models.Model):
    description = models.CharField(max_length = 250)
    price = models.IntegerField()
    category = models.IntegerField()
    
    def __str__(self):
        return self.description