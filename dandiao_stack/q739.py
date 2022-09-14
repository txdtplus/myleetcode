class Solution:
    def dailyTemperatures(self, temperatures: list) -> list:
        answer = [0]*len(temperatures)
        stack = [0]
        for i in range(1,len(temperatures)):
            # 情况一和情况二
            if temperatures[i]<=temperatures[stack[-1]]:
                stack.append(i)
            # 情况三
            else:
                while len(stack) != 0 and temperatures[i]>temperatures[stack[-1]]:
                    answer[stack[-1]]=i-stack[-1]
                    stack.pop()
                stack.append(i)
            
        return answer


if __name__ == '__main__':
    a = [3,4,2,4,5,3,3,5,7]
    s = Solution()
    print(s.dailyTemperatures(a))