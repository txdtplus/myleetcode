class Solution:
    def removeElement(self, nums: list, val: int) -> int:

        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        
        print(nums)
        return slow

if __name__ == '__main__':
    a = [3,4,3,2,4,5,6,7]
    v = 3
    s = Solution()
    print(s.removeElement(a, v))