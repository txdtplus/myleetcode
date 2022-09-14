from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []
        sum_now = [0]

        def dfs(n, k, startIdx):
            if len(path) == k:
                if sum_now[0] == n:
                    res.append(path[:])
                return

            for i in range(startIdx, 10 - (k - len(path)) + 1):
                path.append(i)
                sum_now[0] += i
                dfs(n, k, i+1)
                path.pop()
                sum_now[0] -= i

        dfs(n, k, 1)
        return res

if __name__ =='__main__':
    n = 7
    k = 3
    s = Solution()
    print(s.combinationSum3(k, n))