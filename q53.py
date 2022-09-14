from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = nums[0]
        max_value = nums[0]
        n = len(nums)
        if n == 1:
            return max_value
        
        for i in range(1, n):
            pre = max(nums[i], pre + nums[i])
            max_value = max(pre, max_value)

        return max_value


if __name__ == '__main__':
    nums = [1]
    s = Solution()
    print(s.maxSubArray(nums=nums))

    for i in range(1, 2):
        print(555)