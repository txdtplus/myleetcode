from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        diff = [prices[i] - prices[i-1] for i in range(1, len(prices))]
        profit = 0

        for i in range(len(diff)):
            if diff[i] > 0:
                profit += diff[i]

        return profit



if __name__ == '__main__':
    prices = [2,2,5,-100,-99]
    s = Solution()
    print(s.maxProfit(prices=prices))