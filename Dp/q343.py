class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 3:
            return 1
        
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n+1):
            for j in range(1, i):
                b = max(dp[i-j], i-j)
                dp[i] = max(j * b, dp[i])
        
        return dp[-1]

if __name__ == '__main__':
    n = 10
    s = Solution()
    print(s.integerBreak(n))