import modules.ProfitCalculator as profitCalc

#This code basically determines what price to sell the item at depending on the increments of conversion rate. 

def calc_price_reduction(df, initial_reductions, incr_cvr_array,
                         incr_sales_array, initial_profit):
    print('initial profit =', initial_profit)

    final_profit = 0
    intermediate_change = initial_reductions

    reduction_flag = True

    for i in range(0, 250):
        # ToDo consider a combination of hi/lo price and hi/lo unit sld in this pricing strategy
        if intermediate_change[i] >= -0.09 and intermediate_change[i] <= 0.19:
            boost = 0
            if incr_cvr_array[i] >= 0.4 or incr_sales_array[i] >= 0.09:
                boost = 0.003  # maximum reduction for products with higher propensity to boost sales and conversion
            elif incr_cvr_array[i] >= 0.3 or incr_sales_array[i] >= 0.09:
                boost = 0.002  # moderate reduction for products with higher propensity to boost converstion and moderate increment in sales
            elif incr_cvr_array[i] >= 0.2 or incr_sales_array[i] >= 0.07:
                boost = 0.001
            elif incr_cvr_array[i] >= 0.1 or incr_sales_array[i] >= 0.05:
                boost = 0
            elif incr_cvr_array[i] < 0.1 and incr_sales_array[i] < 0.05:
                boost = -0.05  # try aggressive price increase
            else:
                if (df['units_sold'][i] > 1.4 & df['unit_price'][i] > 80):
                    boost = -0.01
                elif (df['units_sold'][i] < 1.4 & df['unit_price'][i] < 30):
                    boost = 0.003
                else:
                    boost = 0.001
            intermediate_change[i] = intermediate_change[i] - boost

        if intermediate_change[i] < -0.10:
            intermediate_change[i] = 0.09
        elif intermediate_change[i] > 0.20:
            intermediate_change[i] = 0.19
    ###

    if (reduction_flag >= 0):
        reduction_flag = False

    profit_wo_price_change_effect, final_profit = profitCalc.calc_profit(
        df, intermediate_change, reduction_flag)
    if final_profit > initial_profit:
        final_reductions = intermediate_change
    else:
        final_reductions = intermediate_change
        final_profit = initial_profit

    print('final profit = ', final_profit)
    return final_reductions, final_profit
