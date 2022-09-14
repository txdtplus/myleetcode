class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        P = [[0] * n for _ in range(n)]

        maxlength = 1
        for i in range(n):
            P[i][i] = 1
            max_string = s[i]
        
        for i in range(n-1):
            if s[i] == s[i+1]:
                P[i][i+1] = 1
                maxlength = 2
                max_string = s[i:i+2]
        
        
        for i in range(3, n+1):
            for j in range(n+1-i):
                if s[j] == s[j+i-1]:
                    P[j][j+i-1] = P[j+1][j+i-2]
                
                if P[j][j+i-1]:
                    max_string = s[j:j+i]

        return max_string

if __name__ == '__main__':
    s = "babadadc"
    print(s[1:2])
    solu = Solution()
    print(solu.longestPalindrome(s))