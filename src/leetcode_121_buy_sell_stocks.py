# LeetCode 121: Best Time to Buy and Sell Stocks

# You are given an array prices where price[i] is the price of the stock on th ith day
# You want to maximize the profit by choosing a single day to buy one stock and choosing
# a different day in the future to sell the stock

# Return the maximum profit you can achieve from this transaction. Return 0 if not.

# prices = [7,1,5,3,6,4]
# Result = 5


# Brute Force (Time Complexity: O(n^2) and Space Complexity: O(1))
# def buy_sell_stock(prices):
    
#     profit = 0

#     for i in range(len(prices)):
#         for j in range(len(prices)):
#             if i < j and prices[j] - prices[i] > profit:
#                 profit = prices[j] - prices[i]
        
#     return profit

def buy_sell_stock(prices):
    
    buy = prices[0]
    sell = None

    max_profit = 0
    profit = 0

    for i in range(len(prices)-1):

        if prices[i] < buy:
            buy = prices[i]
        
        sell = prices[i+1]

        if sell > buy:
            profit = sell - buy
        
        max_profit = max(profit, max_profit)
    
    return max_profit

result = buy_sell_stock([7,1,5,3,6,4])
print(result)