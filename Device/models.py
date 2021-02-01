from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    category_name=models.CharField(max_length=20,unique=True)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    name=models.CharField(max_length=40,null=False)
    price=models.IntegerField(max_length=40,null=False)
    image=models.ImageField(upload_to="images",null=False)
    category=models.ForeignKey(ProductCategory,on_delete=models.CASCADE)

    def __str__(self):
        return self.name