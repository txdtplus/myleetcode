from typing import List

class Solution:
    def climbStairs(self, n: int) -> int:

        array = [1, 2, 3]

        for i in range(3, n + 1):
            array[2] = array[0] + array[1]
            array[0] = array[1]
            array[1] = array[2]
        
        return array[n-1] if n < 3 else array[2]


if __name__ == '__main__':
    n = 6
    s = Solution()
    print(s.climbStairs(n=n))