# Hackathon Objective

Learn a concept in Banking and Finance domain and create an App to demonstrate the concept.

Here I have tried to learn the concept of increasing Financial Gain by learning how to optimize the price of sold goods.

I have followed this website to learn the basic idea
https://www.analyticsvidhya.com/blog/2016/07/solving-case-study-optimize-products-price-online-vendor-level-hard/

-- Average Price/Unit : Market price of the product

-- Cost/Unit : Current cost of the product

-- Average Profit/Unit : Profit for each unit

-- Average units sold : Average number of units of product sold to a customer who makes a purchase

-- Incremental acquisition : For every 10% decline in unit price, this is the increase in total customer response rate. Note that overall response rate initially is 5% (5000 out of 100000 make a purchase). You are allowed to decrease the price of a product maximum by 10% by market laws.

-- Increase in sale volume : For every 10% decline in unit price of product, this is the increase in volume. Again, you are allowed to decrease the price of a product maximum by 10% by market laws.

# App Name: 
Sales Profit Maximizer

# App Goal: 

Let's assume, a Company sells products and is looking for a way to maximize the profits.  

This App can help find the best estimated price for all the products based on the sales data so that the company can achieve its Financial Goal.

In Finance, there is a concept of increasing Conversion Rate and increasing Demand by decreasing Price.

The Sales data contains average unit_price , avgerage unit_quantity_sold and average unit_cost along with incr_cvr and incr_sales for every item.

When a company generates the sales data , incr_cvr  and incr_sales are calculated from the historical dataset.

incr_cvr is increase in conversion rate for every 10% decrease in price that means %of new consumers attracted after decreasing price

incr_sales is increase in sales for every 10% decrease in price, that means %of increase in quantity of same product purchased by a customer.

This Pricing strategy can help increase the profit significantly.

# App Tools & Technology:

DASH library is used for running Flask python Web App. 

DASH allows the creation of web components (html, css) in python. 

The App can be deployed in cloud using app.yaml or can be executed in a container using Dockerfile.dash

Used Visual Studios Code as the development environment with Github Desktop for code management.

# App Execution:

python MainApp.py

Internally, the app will start the server in a specified port

app.run_server(host='0.0.0.0', port=8088, debug=True, use_reloader=True)

By default it will run in local machine.

# App Workflow:

1) Once the App is started, MainApp.py generates the UI to upload the Sales Data

Screenshot 1: https://github.com/srijon-mandal/sales-profit-maker/blob/main/Initial_UI.jpeg

2) User uploads the Sales data

Example: https://www.analyticsvidhya.com/wp-content/uploads/2016/07/Vendor_Data.csv

3) MainApp calls SalesProfitEstimator

   -- SalesProfitEstimator calculate the current profit based on existing sales data. It doesn't use any algorithm.
   
   -- Next it tries to estimate the price of each item through multiple iterations. 
   
   -- The loop will stop when either estimated profit doesn't change or it has reached maximum iterations.
   
   -- Within each iteration The Algorithm applies following Business Rules to find proposed change in price (modules/PriceCalculator.py)
   
          -- decrese the price if incr_cvr and incr_sales already high (this is one approach - we can also try other way round)
          
          -- increase the price if incr_cvr and incr_sales are low (we can do the reverse and test if this this approach offers better result)
          
          -- decrease the price if price and units_sold are already high. 
          
          -- increase the price if price and units_sold are already low.
          
          -- ensure the new price always within the range 10% below base price and 20% above base price
   
   -- once the change in price is dertermined by PriceCalculator, then ProfitCalculator.py creates the profit by using following rules
          
          -- price_change_multiplier = 1 + price_change_val (determined in previous step)
          
          -- adjusted_price = original_unit_price * price_change_multiplier
          
          -- if (price_reduction):
          
                 sales_incr_per_tx = incr_sales*abs(price_change_val)*10
                 
                 customer_incr = incr_cvr*abs(price_change_val)*10
             
             else:
             
                 customer_incr = incr_cvr_default

          -- sales_multipler = 1 + sales_incr_per_tx
          
          -- transaction_multiplier = 1 + customer_incr
          
          -- adjusted_volume = original_units_sold * sales_multipler * transaction_multiplier
          
          -- calculate final profit using the adjusted_price and adjusted_volume
          
          -- est_profit = (adjusted_price * adjusted_volume) - (original_cost * adjusted_volume)

6) Show Final Profit Summary and Report in UI

Profit without Optimization: 3285.90

Net Estimated Profit: 4772.95 , LIFT by [45.26 %]

Increase in Total Pricing: 879.47, [5.80 %]

Increase in Total Units Sold: 18.76 %, [5 %]

Screenshot 2: https://github.com/srijon-mandal/sales-profit-maker/blob/main/FinalUI.jpeg

# Future Work

1) User Login 

3) Allow user to upload historical data with user info and calculate incr_cvr and incr_sales

# References

https://www.analyticsvidhya.com/blog/2016/07/solving-case-study-optimize-products-price-online-vendor-level-hard/

https://www.coursera.org/lecture/uva-darden-bcg-pricing-strategy-cost-economics/price-elasticities-KJaeh


