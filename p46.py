class Solution:
    def permute(self, nums: list) -> list:
        if not nums:
            return [[]]
        
        res = []
        for i in range(len(nums)):
            for j in self.permute(nums[:i] + nums[i+1:]):
                res.append([nums[i]] + j)
        return res

if __name__ == '__main__':
    a = [1,2,3]
    s = Solution()
    print(s.permute(a))