class Solution:
    def permuteUnique(self, nums: list) -> list:
        res = []
        nums.sort()
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                addtmp = tmp + [nums[i]]
                backtrack(nums[:i] + nums[i + 1:], addtmp)
        backtrack(nums, [])
        return res

if __name__ == '__main__':
    a = [1,1,2]
    s = Solution()
    print(s.permuteUnique(a))