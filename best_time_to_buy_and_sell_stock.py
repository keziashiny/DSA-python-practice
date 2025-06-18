def max_profit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            max_profit = max(max_profit, profit)
    return max_profit   
print(max_profit([7, 1, 5, 3, 6, 4]))  
print(max_profit([7, 6, 4, 3, 1]))    
         

def max_profit(prices):
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
print(max_profit([7, 1, 5, 3, 6, 4]))  
print(max_profit([7, 6, 4, 3, 1])) 