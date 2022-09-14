from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(candidates, target, sum_, startIdx):
            if sum_ == target:
                res.append(path[:])
                return
            
            for i in range(startIdx, len(candidates)):
                if sum_ + candidates[i] > target:
                    return
                
                sum_ += candidates[i]
                path.append(candidates[i])
                dfs(candidates, target, sum_, i)
                sum_ -= candidates[i]
                path.pop()
        
        candidates.sort()
        dfs(candidates, target, 0, 0)

        return res

if __name__ == '__main__':
    nums = [2,3,6,7]
    target = 7
    s = Solution()
    print(s.combinationSum(candidates=nums, target=target))