from django.db import models

# Create your models here.


class Product(models.Model):
    product = models.CharField(max_length=1000)
    price = models.CharField(max_length=80)
    link_img = models.URLField(max_length=1000)
    link_url = models.URLField(max_length=1000)
    search = models.ForeignKey('Search', on_delete=models.CASCADE)
    origin = models.CharField(max_length=80)
    
    def __str__(self):
        return self.name

class Search(models.Model):
    name = models.CharField(max_length=40) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
        

        



