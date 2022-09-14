class Solution:
    def reverse(self, x: int) -> int:

        positive_x = abs(x)
        sign = 1 if x > 0 else -1
        str_x = str(positive_x)

        if sign > 0:
            inf_max = 2**31-1
        else:
            inf_max = 2**31

        list_inf = list(str(inf_max))

        n = len(str_x)

        y = 0
        y_list = []
        for i in range(n):
            num = int(str_x[n-i-1])
            y_list.append(num)
        
        if n > len(list_inf):
            return 0
        
        if n == len(list_inf):
            for i in range(len(y_list)):
                if int(y_list[i]) < int(list_inf[i]):
                    break
                elif int(y_list[i]) > int(list_inf[i]):
                    return 0
                
        for i in range(n):
            y += y_list[i] * 10 ** (n-i-1)
        return sign * y

if __name__ == '__main__':
    a = 1534236469
    s = Solution()
    print(s.reverse(a))