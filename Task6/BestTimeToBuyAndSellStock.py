

# 121. Best Time to Buy and Sell Stock

'''

Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.



Constraints:

    1 <= prices.length <= 105
    0 <= prices[i] <= 104



'''


import math
import time
import collections
from typing import List
import numpy as np
import random as rnd
import itertools as it
from collections import defaultdict, Counter
import re
from functools import reduce
from bisect import bisect, bisect_left


# my solution
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        buyingPrice = max(prices)+1
        #buyingPriceDayNumber = len(prices) + 1
        sellingPrice = min(prices)-1
        #sellingPriceDayNumber = len(prices) + 1
        curSellingPrice = sellingPrice
        curBuyingPrice = buyingPrice
        curBuyingPriceDayNumber = len(prices) + 1
        curSellingPriceDayNumber = len(prices) + 1
        maxProfit = -1
        for pos, price in enumerate(prices):
            isStockBought = False
            if price < curBuyingPrice:
                curBuyingPrice = price
                curBuyingPriceDayNumber = pos
                isStockBought = True
                curSellingPrice = -1
            if price >= curSellingPrice and pos > curBuyingPriceDayNumber and isStockBought == False:
                curSellingPrice = price
                curSellingPriceDayNumber = pos
            profit = curSellingPrice - curBuyingPrice
            if maxProfit < profit:
                if curBuyingPriceDayNumber < curSellingPriceDayNumber:
                    maxProfit = profit
                    #sellingPriceDayNumber = curSellingPriceDayNumber
                    #buyingPriceDayNumber = curBuyingPriceDayNumber
        #profit = sellingPrice - buyingPrice
        if maxProfit > 0:
            return maxProfit
        else:
            return 0


# solution after Vlad's tips (Vlad's solution)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            price = prices[i]
            max_profit = max(price - min_price, max_profit)
            min_price = min(price, min_price)
        return max_profit


if __name__ == "__main__":
    #
    start = time.perf_counter()
    solution = Solution()
    print(solution.maxProfit(prices = [7,1,5,3,6,4])) # 5
    end = time.perf_counter()
    print(f"test 1: {end - start:10.6f} sec")
    #
    start2 = time.perf_counter()
    print(solution.maxProfit(prices = [7,6,4,3,1])) # 0
    end2 = time.perf_counter()
    print(f"test 2: {end2 - start2:10.6f} sec")
    #
    start3 = time.perf_counter()
    print(solution.maxProfit(prices = [2,4,1])) # 2
    end3 = time.perf_counter()
    print(f"test 3: {end3 - start3:10.6f} sec")
    #
    start4 = time.perf_counter()
    print(solution.maxProfit(prices = [2,1,2,1,0,1,2])) # 2
    end4 = time.perf_counter()
    print(f"test 4: {end4 - start4:10.6f} sec")
    #
    start5 = time.perf_counter()
    print(solution.maxProfit(prices = [3,3,5,0,0,3,1,4])) # 4
    end5 = time.perf_counter()
    print(f"test 5: {end5 - start5:10.6f} sec")
    #
    start6 = time.perf_counter()
    print(solution.firstMissingPositive([1, 1]))
    end6 = time.perf_counter()
    print(f"test 6: {end6 - start6:10.6f} sec")
