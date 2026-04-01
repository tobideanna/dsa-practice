class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #we need to find the best day to buy and sell stocks
        #we can keep two pointers. for example:
        #[10,1,5,6,7,1]
        #we want to be pointer l for buy prices, and pointer r
        #for sell prices
        b, s = 0, 1
        max_p = 0
        while s < len(prices):
            if prices[s] > prices[b]:
                profit = prices[s] - prices[b]
                max_p = max(max_p, profit)
            else:
                b = s
            s += 1
        return max_p

