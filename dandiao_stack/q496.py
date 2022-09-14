import numpy as np

class Solution:
    def dailyTemperatures(self, nums1: list, nums2: list) -> list:
        answer = [-1] * len(nums1)
        stack = [0]
        
        for i in range(1, len(nums2)):

            if nums2[i] <= nums2[stack[-1]]:
                stack.append(i)

            else:
                while len(stack) != 0 and nums2[i] > nums2[stack[-1]]:
                    if nums2[stack[-1]] in nums1:
                        index = nums1.index(nums2[stack[-1]])
                        answer[index] = nums2[i]
                    
                    stack.pop()
                stack.append(i)
            
        return answer


if __name__ == '__main__':
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    s = Solution()
    print(s.dailyTemperatures(nums1, nums2))
