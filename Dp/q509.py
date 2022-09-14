class Solution:
    def fib(self, n: int) -> int:
        
        dp = [0] * 3
        dp[1] = 1

        for i in range(2, n+1):
            dp[2] = dp[1] + dp[0]
            dp[0] = dp[1]
            dp[1] = dp[2]
        
        return dp[n] if n < 2 else dp[-1]



if __name__ == '__main__':
    num = 4
    s = Solution()
    print(s.fib(n=num))