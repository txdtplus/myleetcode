class Solution:
    def maxArea(self, height: list) -> int:
        i = 0
        j = len(height) - 1
        max_area = 0
        while i < j:
            max_area = max(max_area, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area



if __name__ == '__main__':
    a = [1,8,6,2,5,4,8,3,7]
    b = []
    b.append([1,2,3,4])
    print(b)
    s = Solution()
    print(s.maxArea(a))