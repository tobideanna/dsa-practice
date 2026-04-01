class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #we need to find the best day to buy and sell stocks
        #we can keep two pointers. for example:
        #[10,1,5,6,7,1]
        #we want to be pointer l for buy prices, and pointer r
        #for sell prices
        buy_day, sell_day = 0, 1
        max_profit = 0
        
        while sell_day < len(prices):
        #we wanna check if the sell price is higher than buy price:
            if prices[sell_day] > prices[buy_day]:
                profit = prices[sell_day] - prices[buy_day]
                max_profit = max(max_profit, profit)
            else:
                buy_day = sell_day
            sell_day += 1
        return max_profit

