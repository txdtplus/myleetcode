class Solution:
    def numTrees(self, n: int) -> int:
        if n == 1:
            return 1
        
        if n == 2:
            return 2

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[0] = 1

        for i in range(2, n + 1):
            for j in range(i):
                dp[i] = dp[j] * dp[i-j-1] + dp[i]

        return dp[-1]


if __name__ == '__main__':
    n = 4
    s = Solution()
    print(s.numTrees(n))