class Solution:
    def fun3(self, nums: list)-> int:

        if not nums:
            return 0
        
        if len(nums) < 3:
            return 0

        diff_nums = [ nums[i]-nums[i+1] for i in range(len(nums)-1) ]
        diff2_nums = [ diff_nums[i]-diff_nums[i+1] for i in range(len(diff_nums)-1) ]

        lianxu_zero = 0
        stable_period = 0
        for i in range(len(diff2_nums)):
            if diff2_nums[i] == 0:
                lianxu_zero += 1
            if diff2_nums[i] != 0 and lianxu_zero != 0:
                stable_period += (1 + lianxu_zero) * lianxu_zero / 2
                lianxu_zero = 0

        if lianxu_zero != 0:
            stable_period += (1 + lianxu_zero) * lianxu_zero // 2
        
        if stable_period > 1000000000:
            return -1
        return int(stable_period)


if __name__ == '__main__':
    a = [2,2]
    # print(a[0:0])
    s = Solution()
    print(s.fun3(a))