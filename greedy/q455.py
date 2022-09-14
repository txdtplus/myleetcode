from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g.sort()
        s.sort()
        res = 0

        for i in range(len(s)):
            if res < len(g) and s[i] >= g[res]:
                res += 1
        
        return res


if __name__ == '__main__':
    g = [1,2,3]
    s = [3]
    solu = Solution()
    print(solu.findContentChildren(g,s))