from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:

        candies = [1] * len(ratings)
        local_min_idx = []

        for i in range(1, len(candies)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1

        for i in range(1, len(candies)):
            if ratings[-(i + 1)] > ratings[-i] and candies[-(i + 1)] <= candies[-i]:
                candies[-(i + 1)] = candies[-i] + 1

        
        return sum(candies)



if __name__ == '__main__':
    ratings = [1,6,10,8,7,3,2]
    s = Solution()
    print(s.candy(ratings=ratings))