from django.urls import path

from bangazon_reports.views.favorited_sellers_by_customer import FavoritedSellersByCustomer
from .views import (InexpensiveProducts, ExpensiveProducts)


urlpatterns = [
    path('inexpensiveproducts', InexpensiveProducts.as_view()),
    path('expensiveproducts', ExpensiveProducts.as_view()),
    path('favorites', FavoritedSellersByCustomer.as_view())
]
