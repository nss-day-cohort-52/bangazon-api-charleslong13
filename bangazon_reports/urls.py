from django.urls import path
from .views import (InexpensiveProducts, ExpensiveProducts)


urlpatterns = [
    path('inexpensiveproducts', InexpensiveProducts.as_view()),
    path('expensiveproducts', ExpensiveProducts.as_view())
]
