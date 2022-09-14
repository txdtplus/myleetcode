class Solution:
    def fun1(self, num: int)-> int:

        flag = 1
        if num < 0:
            flag = 0
            num = -1 * num

        num_str = str(num)
        five_num = num_str.count('5')

        dict = {}
        results = []
        
        k = 0
        for i in range(len(num_str)):
            if num_str[i] == '5':
                dict[k] = i
                k += 1

        for i in range(five_num):
            new_num_str = ''
            for j in range(len(num_str)):
                if num_str[j] != '5' or j != dict[i]:
                    new_num_str += num_str[j]
            results.append(int(new_num_str))
        
        if flag:
            return max(results)
        else:
            return -min(results)





if __name__ == '__main__':
    a = -345995
    s = Solution()
    print(s.fun1(a))