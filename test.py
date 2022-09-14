class Solution:
    def combine(self, n) -> list:
        res = []
        path = []
        def backtrack(n):
            if n == 1:
                res.append(n)
                return
            for i in range(n):
                print(i)
                backtrack(i -1)

        backtrack(n)    
        return res

if __name__ == '__main__':
    a = 123322
    str_num = str(a)

    b = [1,2,3,3,2,3,4,2,2]

    for idx, num in enumerate(b):
        print(idx)
        print(num)
