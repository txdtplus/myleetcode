class Solution:
    def fun2(self, nums: list)-> int:

        if not nums:
            return -1

        n = len(nums)
        zero_num = 0
        for i in range(n):
            for j in range(i,n):
                sub_nums = nums[i:j+1]
                if sum(sub_nums) == 0:
                    zero_num += 1
                
                if zero_num > 1000000000:
                    return -1
        
        return zero_num






if __name__ == '__main__':
    a = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    # print(a[0:0])
    s = Solution()
    print(s.fun2(a))