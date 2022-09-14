
class Solution:
    def sortedSquares(self, nums: list) -> list:
        for i in range(len(nums)):
            nums[i] *= nums[i]
        
        left = 0
        right = len(nums) - 1
        k = len(nums) - 1
        new_nums = nums[:]

        while left <= right:
            if nums[left] > nums[right]:
                new_nums[k] = nums[left]
                left += 1
            else:
                new_nums[k] = nums[right]
                right -= 1
            k -= 1

        return new_nums

if __name__ == '__main__':
    nums = [-10000,-9999,-7,-5,0,0,10000]
    s = Solution()
    print(s.sortedSquares(nums))