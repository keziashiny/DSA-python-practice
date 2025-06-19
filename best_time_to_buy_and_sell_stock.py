# File: best_time_to_buy_and_sell_stock.py
# Description: Solves the "Best Time to Buy and Sell Stock" problem using an efficient single-pass algorithm.

def max_profit(prices):
     """
    Calculates the maximum profit from a single buy-sell transaction.

    Parameters:
    prices (list): List of daily stock prices.

    Returns:
    int: Maximum achievable profit.
    """
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            max_profit = max(max_profit, profit)
    return max_profit
# Example usage
print(max_profit([7, 1, 5, 3, 6, 4]))  
print(max_profit([7, 6, 4, 3, 1]))    
         

def max_profit(prices):
    """
    Debug version: Prints internal steps while calculating max profit.

    Parameters:
    prices (list): List of daily stock prices.

    Returns:
    int: Maximum achievable profit.
    """
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        print(f"Day price: {price}, Min so far: {min_price}")
        if price < min_price:
            min_price = price
            print(f"  New min found → min_price = {min_price}")
        else:
            profit = price - min_price
            print(f"  Profit = {price} - {min_price} = {profit}")
            max_profit = max(max_profit, profit)
            print(f"  Max profit so far = {max_profit}")

    return max_profit
    # Example usage (debug)
print(max_profit([7, 1, 5, 3, 6, 4]))  
print(max_profit([7, 6, 4, 3, 1])) 
