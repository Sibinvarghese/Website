from django.shortcuts import render
from .forms import CreateCategoryForm,CreateProductForm
from .models import ProductCategory,Product
from django.views.generic import TemplateView
# Create your views here.

class CategoryView(TemplateView):
    form_class=CreateCategoryForm
    template_name = "device/create_category.html"
    context={}

    def get(self, request, *args, **kwargs):
        form=CreateCategoryForm
        self.context["form"]=form
        return render(request,self.template_name,self.context)


    def post(self, request, *args, **kwargs):
        form=CreateCategoryForm(data=request.POST)
        if form.is_valid():
            form.save()
            print("saved")
            return render(request, self.template_name, self.context)

        else:
            self.context["form"] = form
            return render(request, self.template_name, self.context)

class ProductView(TemplateView):
    form_class=CreateProductForm
    template_name = "device/product.html"
    context={}

    def get(self, request, *args, **kwargs):
        form=CreateProductForm
        self.context["form"]=form
        return render(request,self.template_name,self.context)


    def post(self, request, *args, **kwargs):
        form=CreateProductForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            print("saved")
            return render(request, self.template_name, self.context)

        else:
            self.context["form"] = form
            return render(request, self.template_name, self.context)

class ProductEditView(TemplateView):
    form_class=CreateProductForm
    template_name = "device/product.html"
    context={}

    def get(self, request, *args, **kwargs):
        form=CreateProductForm
        self.context["form"]=form
        return render(request,self.template_name,self.context)


    def post(self, request, *args, **kwargs):
        form=CreateProductForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            print("saved")
            return render(request, self.template_name, self.context)

        else:
            self.context["form"] = form
            return render(request, self.template_name, self.context)

class ViewDevice(TemplateView):
    model=Product
    template_name = "device/Home_Page.html"
    context={}

    def get(self, request, *args, **kwargs):
        devices=self.model.objects.all()
        self.context["devices"]=devices
        return render(request,self.template_name,self.context)
class ViewError(TemplateView):
    model=Product
    template_name = "device/error.html"
    context={}

    def get(self, request, *args, **kwargs):
        form=Product
        self.context["devices"]=form
        return render(request,self.template_name)
