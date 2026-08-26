class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        daily_profit=0
        min_price=None
        for price in prices:
            if min_price is None: min_price=price
            else:
                if price<min_price:
                    min_price=price
                    daily_profit=0
                elif price>min_price:
                    daily_profit=price-min_price
                if daily_profit>max_profit:max_profit=daily_profit
        return max_profit