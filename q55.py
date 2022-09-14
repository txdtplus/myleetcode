from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)
        k = 0
        for i in range(n):
            if k >= n - 1:
                return True
            
            if i == k and nums[i] == 0:
                return False
                
            k = max(i + nums[i], k)


        return False 


if __name__ == '__main__':
    nums = [2,1,2,2,1,2,2,2]
    s = Solution()
    print(s.canJump(nums=nums))