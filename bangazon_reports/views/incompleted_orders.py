from django.shortcuts import render 
from django.db import connection   
from django.views import View 
from bangazon_reports.views.helpers import dict_fetch_all 

class IncompletedOrders(View):
    def get(self, request):
        with connection.cursor() as db_cursor:
            
            db_cursor.execute("""
             select 
                bangazon_api_order.id as order_id,
                auth_user.first_name || " " || auth_user.last_name as customer_name,
                sum(price) as total,
                bangazon_api_paymenttype.merchant_name as payment_type,
                bangazon_api_order.created_on
                FROM bangazon_api_order
                JOIN bangazon_api_product on bangazon_api_product.id == bangazon_api_orderproduct.product_id
                JOIN auth_user on auth_user.id == bangazon_api_order.user_id
                JOIN bangazon_api_orderproduct on bangazon_api_orderproduct.order_id == bangazon_api_order.id
                LEFT JOIN bangazon_api_paymenttype on bangazon_api_paymenttype.id == bangazon_api_order.payment_type_id
                WHERE payment_type IS NULL
                GROUP BY order_id
               
            """)
            # turns response into a dictionary 
            dataset = dict_fetch_all(db_cursor)
            
            orders = []
            
            for row in dataset:
                order = {
                    'order_id': row['order_id'], 
                    'customer_name': row['customer_name'], 
                    'total': row['total'],
                    'payment_type': row['payment_type'], 
                    'created_on': row['created_on']
                }
                orders.append(order)
        # needs to match the name of the html template 
        template = "incompleted_orders.html"
        # context is a dictionary containing the data to be displayed 
        context = {
            "incompleted_orders_list": orders
        }
        
        return render(request, template, context)