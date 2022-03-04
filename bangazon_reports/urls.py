from django.urls import path
from .views import (InexpensiveProducts)


urlpatterns = [
    path('inexpensiveproducts', InexpensiveProducts.as_view())
]
