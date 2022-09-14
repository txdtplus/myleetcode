from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def dfs(first=0):
            if first == n-1:
                res.append(nums[:])
                return
            else:
                for i in range(first, n):
                    nums[i], nums[first] = nums[first], nums[i]
                    dfs(first+1)
                    nums[i], nums[first] = nums[first], nums[i]

        n = len(nums)
        res = []
        dfs()
        return res




if __name__ == '__main__':
    nums = [1,2,3]
    s = Solution()
    print(s.permute(nums=nums))