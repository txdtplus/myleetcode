
class Solution:
    def BubbleSort(self, input:list)->list:
        for i in range(len(input)-1):
            for j in range(len(input)-1-i):
                if input[j] > input[j+1]:
                    input[j], input[j+1] = input[j+1], input[j]
        return input


if __name__ == '__main__':
    a = [4,3,6,7,3,2,4,6,7,8,21,3]
    print(Solution().BubbleSort(a))