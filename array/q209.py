
class Solution:
    def minSubArrayLen2(self, s: int, nums: list):
        if not nums:
            return 0
        
        n = len(nums)
        ans = n + 1
        start, end = 0, 0
        total = 0
        while end < n:
            total += nums[end]
            while total >= s:
                ans = min(ans, end - start + 1)
                total -= nums[start]
                start += 1
            end += 1
        
        return 0 if ans == n + 1 else ans


    def minSubArrayLen(self, s: int, nums: list) -> int:
        N = len(nums)
        max_sum = sum(nums)

        if max_sum < s:
            return 0

        P = [0] * N

        for i in range(N):
            P[i] = nums[i]
            if P[i] >= s:
                return 1

        for d in range(2, N + 1):
            for i in range(N-d+1):
                start_idx = i
                end_idx = i + d - 1

                P[start_idx] = P[start_idx] + nums[end_idx]
                
                if P[start_idx] >= target:
                    return end_idx - start_idx + 1



if __name__ == '__main__':
    nums = [2,-2,3,0,4,-7]
    target = 0
    s = Solution()
    print(s.minSubArrayLen(target, nums))
