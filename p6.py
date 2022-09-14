class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s
        
        n = len(s)
        res = n % (2 * numRows - 2)
        numCols = n // (2 * numRows - 2) * (numRows - 1) + max(0, res - numRows) + 1

        P = [[" "] * numCols for _ in range(numRows)]

        i = j = 0
        dir = 0
        for iter in range(n):
            P[i][j] = s[iter]

            if i == 0:
                dir = 0
            
            if i == numRows-1:
                dir = 1
            
            if not dir:
                i += 1
            else:
                i -= 1
                j += 1
        
        out_string = ""
        for i in range(numRows):
            for j in range(numCols):
                if P[i][j] != " ":
                    out_string += P[i][j]

        return out_string

if __name__ == '__main__':
    s = "PAYPALISHIRING"
    numRows = 3
    solu = Solution()
    print(solu.convert(s, numRows=numRows))