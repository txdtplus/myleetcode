from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        inf = int(1e9)
        min_price = inf
        max_profit = 0
        for price in prices:
            max_profit = max(price - min_price, max_profit)
            min_price = min(price, min_price)
        return max_profit



if __name__ == '__main__':
    prices = [2,2,5,-100,-99]
    s = Solution()
    print(s.maxProfit(prices=prices))