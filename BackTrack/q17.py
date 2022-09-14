from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        mydict = {"2":["a","b","c"],
                "3":["d","e","f"],
                "4":["g","h","i"],
                "5":["j","k","l"],
                "6":["m","n","o"],
                "7":["p","q","r","s"],
                "8":["t","u","v"],
                "9":["w","x","y","z"],}

        res = []
        path = []
        if len(digits) == 0:
            return res

        def dfs(digits):
            if len(digits) == 0:
                res.append("".join(path))
                return
            
            first_num = digits[0]
            for i in range(len(mydict[first_num])):
                path.append(mydict[first_num][i])
                dfs(digits[1:])
                path.pop()
        
        dfs(digits)

        
        return res

if __name__ == '__main__':
    digits = "23"
    s = Solution()
    print(s.letterCombinations(digits=digits))