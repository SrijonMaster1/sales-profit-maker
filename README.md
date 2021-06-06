# Sales-Profit-Maker

# App Name: 
Maximize Sales Profit

# App Goal: 


Let's assume, a Company sells products and is looking for a way to maximize the profits.  This App finds the best estimated price for all the products based on the sales data.

In Finance, there is a concept of increasing Conversion Rate and Increasing Demand by decreasing Price.

The data contains avg_unit_price , avg_unit_quantity and avg_unit_cost along with incr_cvr and incr_sales for every item.

This Pricing strategy can help increase the profit significantly.

When a company generates the sales data , incr_cvr  and incr_sales are calculated from the historical dataset.

incr_cvr is increase in conversion rate for every 10% decrease in price that means %of new consumers attracted after decreasing price

incr_sales is increase in sales for every 10% decrease in price, that means %of increase in quantity of same product purchased by a customer.

# App Setup:

DASK library is used to create a container for running a Flask python App. 

DASK allows the creation of web components in python. 

The App can be deployed in cloud using app.yaml

By default it will run in local machine.

# App Workflow:

1) Once the App is started MainApp.py generates the UI to upload the Sales Data

Pricing-Strategy python MainApp Up 0.0.0.0:8081->8088/tcp

http://0.0.0.0/8081

Screenshot 1: 


2) User Logs into App (Not implemented)

3) User uploads the Sales data
Example: https://www.analyticsvidhya.com/wp-content/uploads/2016/07/Vendor_Data.csv

4) MainApp calls SalesProfitEstimator

5) The Algorithm tries to decrease the price if incr_cvr and incr_sales already high and decrease the price if incr_cvr and incr_sales are low. 

It also checks if price and units_sold are already high then reduce it. 

It also checks if price and units_sold are already low then increase it.

6) Final Profit and Report is display in UI

Profit without Optimization: 3285.90

Net Estimated Profit: 4772.95 , LIFT by [45.26 %]

Increase in Total Pricing: 879.47, [5.80 %]

Increase in Total Units Sold: 18.76 %, [5 %]

Screenshot2: 

# Future Work

1) Allow user to upload historical data with user info and calculate incr_cvr and incr_sales

# References

https://www.analyticsvidhya.com/blog/2016/07/solving-case-study-optimize-products-price-online-vendor-level-hard/

https://www.coursera.org/lecture/uva-darden-bcg-pricing-strategy-cost-economics/price-elasticities-KJaeh
