class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        best = 0
        for price in prices:
            min_price = min(min_price, price)
            best = max(best,price - min_price)
        return best




        # i=0
        # while i < len(prices)-1:
        #     if prices[i] < prices[i+1]:
        #         if prices[i] < buy or buy == 0 :
        #             buy = prices[i]
        #     else:
        #         if prices[i+1] < buy:
        #             buy = prices[i+1]

        #     print(buy)
        #     i+=1
        # return profit