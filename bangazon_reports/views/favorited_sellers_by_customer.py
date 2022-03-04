from django.shortcuts import render 
from django.db import connection   
from django.views import View 
from bangazon_reports.views.helpers import dict_fetch_all 

class FavoritedSellersByCustomer(View):
    def get(self, request):
        with connection.cursor() as db_cursor:
            
            db_cursor.execute("""
            select
                auth_user.id as customer_id,
                auth_user.first_name ||" "||auth_user.last_name as customer,
                bangazon_api_store.name as store
            FROM bangazon_api_favorite 
            join bangazon_api_store on bangazon_api_store.id = bangazon_api_favorite.store_id
            join auth_user on auth_user.id = bangazon_api_favorite.customer_id
            """)
            # turns response into a dictionary 
            dataset = dict_fetch_all(db_cursor)
            
            customers = []
            
            for row in dataset:
                store = { 
                    'store': row['store']
                    
                }
                customer_dict = next(
                (    customer_store for customer_store in customers
                    if customer_store['customer_id'] == row['customer_id']
                ),
                None
            )
                if customer_dict:
                    customer_dict['stores'].append(store)
                else:
                    customers.append({
                        'customer_id': row['customer_id'],
                        'customer': row['customer'], 
                        'stores': [store]
                    })
                
        # needs to match the name of the html template 
        template = "favorited_sellers_by_customer.html"
        # context is a dictionary containing the data to be displayed 
        context = {
            "favorited_sellers_by_customers_list": customers 
        }
        
        return render(request, template, context)