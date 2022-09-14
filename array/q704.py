class Solution:
    def search(self, nums: list, target: int) -> int:
        nums.sort()

        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2

            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle
        
        return -1


if __name__ == '__main__':
    a = [1,45,4,32,3,5,27,1,3,3,6]
    a.sort()
    t = 3
    s = Solution()
    print(a)
    print(s.search(a, t))