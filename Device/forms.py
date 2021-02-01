from django.forms import ModelForm
from .models import ProductCategory,Product



class CreateCategoryForm(ModelForm):
    class Meta:
        model=ProductCategory
        fields=["category_name"]

class CreateProductForm(ModelForm):
    class Meta:
        model=Product
        fields=["name","price","image","category"]

