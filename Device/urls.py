
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import CategoryView,ProductView,ViewDevice,ViewError

urlpatterns = [
    path("category",CategoryView.as_view(),name="category"),
    path("product",ProductView.as_view(),name="product"),
    path("view",ViewDevice.as_view(),name="view"),
    path("error",ViewError.as_view(),name="error"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


