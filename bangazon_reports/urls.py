from django.urls import path
from bangazon_reports.views.completed_orders import CompletedOrders

from bangazon_reports.views.favorited_sellers_by_customer import FavoritedSellersByCustomer
from bangazon_reports.views.incompleted_orders import IncompletedOrders
from .views import (InexpensiveProducts, ExpensiveProducts)


urlpatterns = [
    path('inexpensiveproducts', InexpensiveProducts.as_view()),
    path('expensiveproducts', ExpensiveProducts.as_view()),
    path('favorites', FavoritedSellersByCustomer.as_view()),
    path('completed', CompletedOrders.as_view()),
    path('incompleted', IncompletedOrders.as_view()),
]
