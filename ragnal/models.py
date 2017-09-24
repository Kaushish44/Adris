from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class City (models.Model):
    name = models.CharField(max_length = 250)
    poster = models.CharField(max_length = 250)
    
    def get_absolute_url(self):
        return reverse('ragnal:city',kwargs={'pk': self.pk})
    
    def __str__(self):  
        return self.name
    
class Site (models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    area = models.CharField(max_length = 150)
    address = models.CharField(max_length = 250)
    poster = models.CharField(max_length = 250, null=True)
    is_favourite = models.BooleanField(default = False)
    
    def __str__(self):  
        return self.area