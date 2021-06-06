import pandas as pd
import os
import numpy as np
import modules.ProfitCalculator as profitCalc
import modules.PriceCalculator as priceCalc

def findMaximumProfit(csv_files_path):
    pd.options.display.float_format = '{:,.2f}'.format
    df = pd.read_csv(csv_files_path)

    price_change_default_val = np.array(df.shape[0] * [0.0])
    current_price_change = price_change_default_val

    converged = False
    max_iter = 0

    print("====================================")
    profit_wo_price_change_effect, current_profit = profitCalc.calc_profit(df, current_price_change, False)

    print("Original profit", profit_wo_price_change_effect)

    incr_cvr_array = df['incr_cvr'].to_numpy()
    incr_sales_array = df['incr_sales'].to_numpy()

    cvr_val_i = np.min(incr_cvr_array)
    cvr_val_iii = np.amax(incr_cvr_array)
    range = np.amax(incr_cvr_array) - np.min(incr_cvr_array)
    cvr_val_ii = np.min(incr_cvr_array) + range/2

    while not converged and max_iter < 10:
        print("====================================")
        next_price_change, next_profit = priceCalc.calc_price_reduction(df, current_price_change, incr_cvr_array,
                                                              incr_sales_array,
                                                              current_profit)
        if (current_profit == next_profit):
            converged = True
        else:
            current_profit = next_profit
            current_price_change = next_price_change

        max_iter += 1

    #
    pd.options.display.float_format = lambda x: '{:.0f}'.format(x) if int(x) == x else '{:,.2f}'.format(x)

    df['est_price'] = df["unit_price"] * (1 + next_price_change)
    final_item_price_data = df[['item_id', 'unit_price', 'est_price', 'units_sold', 'est_volume', 'original_profit' ,'est_profit']]
    df.round(2)
    print('Old Net profit', current_profit)
    print('New Net profit', next_profit)

    change_in_total_price = np.sum(df['est_price']) - np.sum(df['unit_price'])
    change_in_total_units_sold = np.sum(df['est_volume']) - np.sum(df['units_sold'])

    profit_with_price_change_effect = next_profit
    perc_change_in_price = 100 * (change_in_total_price/ np.sum(df['unit_price']))
    perc_lift_in_profit = 100 * ((profit_with_price_change_effect - profit_wo_price_change_effect) / profit_wo_price_change_effect)
    perc_change_in_sales = 100 * (change_in_total_units_sold/ np.sum(df['units_sold']))

    #profit_spike_price_elasticity_df =df.loc[(df["est_price"] < df["unit_price"]) & (df["est_profit"] > df["original_profit"])]
    #print(np.sum(profit_spike_price_elasticity_df["est_profit"] - profit_spike_price_elasticity_df["original_profit"]))

    return final_item_price_data, profit_wo_price_change_effect, profit_with_price_change_effect, change_in_total_price, perc_lift_in_profit, perc_change_in_price, change_in_total_units_sold, perc_change_in_sales

