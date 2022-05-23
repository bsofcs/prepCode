#bestTimeToBuy
#You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#
#Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
#
#Example 1:
#
#Input: prices = [7,1,5,3,6,4]
#Output: 5
#Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.


class Solution:
    def maxProfit(self, prices):
        if prices is None:
            return 0
        min_so_far=prices[0]
        max_so_far=float("-INF")
        l=len(prices)
        dp=[0]*l
        for i in range(1,l):
            if prices[i]<min_so_far:
                min_so_far=prices[i]
                max_so_far=prices[i]
            if prices[i]>max_so_far:
                max_so_far=prices[i]
            dp[i]=max_so_far-min_so_far
        return max(dp)
    def maxProfit1(self,prices):
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit
            
s=Solution()
prices = [7,1,5,3,6,4]
print(prices,s.maxProfit(prices),s.maxProfit1(prices))
prices = [7,6,4,3,1]
print(prices,s.maxProfit(prices),s.maxProfit1(prices))
prices = [1,4,5,7,1,5,3,6,4]
print(prices,s.maxProfit(prices),s.maxProfit1(prices))