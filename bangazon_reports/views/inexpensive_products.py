from django.shortcuts import render 
from django.db import connection   
from django.views import View 
from bangazon_reports.views.helpers import dict_fetch_all 

class InexpensiveProducts(View):
    def get(self, request):
        with connection.cursor() as db_cursor:
            
            db_cursor.execute("""
            select
                bangazon_api_product.name as name,
                bangazon_api_product.price as price,
                bangazon_api_store.name as store
            from bangazon_api_product
            join bangazon_api_store on bangazon_api_store.id == bangazon_api_product.store_id
            where price < 1000 
            """)
            # turns response into a dictionary 
            dataset = dict_fetch_all(db_cursor)
            
            products = []
            
            for row in dataset:
                order = {
                    'name': row['name'], 
                    'price': row['price'], 
                    'store': row['store']
                }
                products.append(order)
        # needs to match the name of the html template 
        template = "inexpensive_products.html"
        # context is a dictionary containing the data to be displayed 
        context = {
            "inexpensive_products_list": products  
        }
        
        return render(request, template, context)