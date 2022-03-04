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