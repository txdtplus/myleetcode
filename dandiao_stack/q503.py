class Solution:
    def nextGreaterElements(self, nums: list) -> list:
        res = [-1] * len(nums)
        stack = [0]

        for i in range(1, len(nums) * 2):
            idx = i % len(nums)
            if nums[stack[-1]] >= nums[idx]:
                stack.append(idx)
            else:
                while stack and nums[stack[-1]] < nums[idx]:
                    res[stack[-1]] = nums[idx]
                    stack.pop()
                stack.append(idx)
        
        return res


if __name__ == '__main__':
    a = [1,2,1]
    s = Solution()
    print(s.nextGreaterElements(a))