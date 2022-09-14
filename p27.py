class Solution:
    def removeElement(self, nums: list, val: int) -> int:
            start = 0
            for i,item in enumerate(nums):
                if item != val:
                    nums[start] = item
                    start += 1
            return start
    
if __name__ == '__main__':
    a = [0,1,2,3,2,2,3,5,4]
    val = 2
    s = Solution()
    print(s.removeElement(a, val))