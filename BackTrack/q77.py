class Solution:
    def combine(self, n: int, k: int) -> list:
        res = []
        path = []
        def backtrack(n, k, StartIndex):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(StartIndex, n + 1):
                path.append(i)
                backtrack(n, k, i+1)
                path.pop()
        backtrack(n, k, 1)
        return res
    
    def combine2(self, n: int, k: int) -> list:
        res = []
        path = []
        def backtrack(n, k, StartIndex):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(StartIndex, n - (k-len(path)) + 2):
                print('yes')
                path.append(i)
                backtrack(n, k, i+1)
                path.pop()
        backtrack(n, k, 1)
        return res
    
    def combine3(self, n: int, k: int) -> list:
        res = []
        path = []

        def backtrack(n, k, start_idx):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(start_idx, n + 1):
                path.append(i)
                backtrack(n, k, i+1)
                path.pop()
        
        backtrack(n, k, 1)     
        return res
    
    def combine4(self, n: int, k: int) -> list:
        res = []
        path = []

        def dfs(n, k, startIdx):
            if len(path) == k:
                res.append(path[:])
                return

            for i in range(startIdx, n-k+len(path)+2):
                path.append(i)
                dfs(n, k, i+1)
                path.pop()
        
        dfs(n, k, 1)
        return res

if __name__ == '__main__':
    s = Solution()
    n = 4
    k = 2
    # print(s.combine(n,k))
    # print(s.combine2(n,k))
    print(s.combine4(n,k))
