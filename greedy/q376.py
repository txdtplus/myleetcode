from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:

        n = len(nums)
        if n < 2:
            return n
        
        prevdiff = nums[1] - nums[0]
        ret = (2 if prevdiff != 0 else 1)
        for i in range(2, n):
            diff = nums[i] - nums[i - 1]
            if (diff > 0 and prevdiff <= 0) or (diff < 0 and prevdiff >= 0):
                # 若序列相等，取后边作为极值点
                ret += 1
                prevdiff = diff
        
        return ret


if __name__ == '__main__':
    nums = [1,7,4,9,2,5]
    s = Solution()
    print(s.wiggleMaxLength(nums=nums))