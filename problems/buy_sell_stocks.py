
""" 
Let say, we've an array 
[7, 1, 5, 3, 6, 4]
At value 1, this is the best time to buy stocks
and at value 6, this is the best time to sell stocks
cause, profit is, 6-1 = 5

7 is the worst time to buy stocks
"""
""" 
Pseudocode for this, 
1. First we find min_price from overall array
2. Then we find profit that is current price - min_price
3. Then we return the maximum profit

"""


def BuySellStocks(array: list):
    min_price = float('inf')
    max_profit = 0

    for price in array:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit


array = [7, 1, 5, 3, 6, 4]
print(BuySellStocks(array))

# Time complexity: O(n)
# Space complexity: O(1)
