class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        
        pre_row = [1] * n

        for i in range(1, m):
            pre_col = 1
            for j in range(1, n):
                cur = pre_col + pre_row[j]
                pre_col = cur 
                pre_row[j] = cur
        
        return cur


if __name__ == '__main__':
    m = 3
    n = 7
    s = Solution()
    print(s.uniquePaths(m,n))