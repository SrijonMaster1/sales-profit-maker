import pandas as pd
import numpy as np

"""This code provides the methods to calculate profit"""


def calc_profit(df, price_change_val, price_reduction_flag=True):
    original_unit_price = df['unit_price']
    price_change_multiplier = 1 + price_change_val

    # For iterantion#1 increment = 0, price_change_multiplier = 1
    # Note that price adjustment is calculated against the original_unit_price
    adjusted_price = original_unit_price * price_change_multiplier

    print('Original Net price ', np.sum(original_unit_price),
          'Adjusted Net price', np.sum(adjusted_price))

    # Avg units sold at base price in one transaction
    original_units_sold = df['units_sold']

    # Calculate additional units for given % of price reduction
    incr_sales = df['incr_sales']
    incr_cvr = df['incr_cvr']
    incr_cvr_default = 0.05
    sales_incr_per_tx = 0

    if (price_reduction_flag):
        sales_incr_per_tx = incr_sales*abs(price_change_val)*10
        customer_incr = incr_cvr*abs(price_change_val)*10
    else:
        customer_incr = incr_cvr_default

    sales_multipler = 1 + sales_incr_per_tx
    transaction_multiplier = 1 + customer_incr
    adjusted_volume = original_units_sold * sales_multipler * transaction_multiplier

    print('Original total units sold ', np.sum(original_units_sold), 'Adjusted total units sold',
          np.sum(adjusted_volume))

    original_cost = df['unit_cost']  # unit cost

    orig_profit = (original_unit_price * original_units_sold) - \
        (original_cost * original_units_sold)
    profit_wo_price_change_effect = np.sum(
        original_unit_price * original_units_sold) - np.sum(original_cost * original_units_sold)

    # Now that price and volume have been adjusted, its time to compute new profit
    est_profit = (adjusted_price * adjusted_volume) - \
        (original_cost * adjusted_volume)
    profit_with_price_change_effect = np.sum(
        adjusted_price * adjusted_volume) - np.sum(original_cost * adjusted_volume)

    print('profit_wo_price_change_effect ', profit_wo_price_change_effect, 'profit_with_price_change_effect',
          profit_with_price_change_effect)

    df['price_change_val'] = price_change_val
    df['price_change_multiplier'] = price_change_multiplier
    df['est_price'] = adjusted_price
    df['est_volume'] = adjusted_volume
    df['original_profit'] = orig_profit
    df['est_profit'] = est_profit

    price_comp = df[['price_change_val', 'price_change_multiplier',
                     'unit_price', 'est_price', 'est_volume', 'est_profit']]
    print(price_comp)

    return profit_wo_price_change_effect, profit_with_price_change_effect
