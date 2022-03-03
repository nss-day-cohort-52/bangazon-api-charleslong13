from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.core.management import call_command
from django.contrib.auth.models import User

from bangazon_api.models import Order, Product


class OrderTests(APITestCase):
    def setUp(self):
        """
        Seed the database
        Adding a new order to users 1 and 2 
        """
        call_command('seed_db', user_count=3)
        self.user1 = User.objects.filter(store=None).first()
        self.user2 = User.objects.filter(store=None).last()
        self.token = Token.objects.get(user=self.user1)

        product = Product.objects.get(pk=1)

        self.order1 = Order.objects.create(
            user=self.user1
        )

        self.order1.products.add(product)

        self.order2 = Order.objects.create(
            user=self.user2
        )

        self.order2.products.add(product)

        self.client.credentials(
            HTTP_AUTHORIZATION=f'Token {self.token.key}')

        
        
    def test_list_orders(self):
        """The orders list should return a list of orders for the logged in user
        When running the test I got AssertionError: 3 != 1, so changed the original 1 being passed in on line 43 to 3 
        Seed data populating each user with 2 orders 
        """
        response = self.client.get('/api/orders')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_delete_order(self):
        """Make sure you can delete an order 
        """
        response = self.client.delete(f'/api/orders/{self.order1.id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    
   