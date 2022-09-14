class Solution:
    def letterCombinations(self, digits: str) -> list:
        
        dict = {"2":["a","b","c"],
                "3":["d","e","f"],
                "4":["g","h","i"],
                "5":["j","k","l"],
                "6":["m","n","o"],
                "7":["p","q","r","s"],
                "8":["t","u","v"],
                "9":["w","x","y","z"],}

        def printCombination(digits, dict):
            if not digits:
                return []
            
            if len(digits) == 1:
                return dict[digits]
            res = []
            resPrint = printCombination(digits[1:], dict)

            for i in range(len(dict[digits[0]])):
                letter = dict[digits[0]][i]
                tmp = [resPrint[k] for k in range(len(resPrint))]
                for j in range(len(resPrint)):
                    tmp[j] = letter + tmp[j]
                
                res += tmp

            return res
        
        return printCombination(digits, dict)

        

        
if __name__ == '__main__':
    digits = "23"
    print(digits[1:])
    print(Solution().letterCombinations(digits))