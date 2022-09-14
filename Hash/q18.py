class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        st = {}
        # st是不重复字符组成的字典，字典指出某个字符的后一个字符的位置
        i, ans = 0, 0
        for j in range(len(s)):
            if s[j] in st:
                # i = max(st[s[j]], i)
                i = j
            ans = max(ans, j - i + 1)
            st[s[j]] = j + 1
        return ans

if __name__ == '__main__':
    s = "abcabcbb"
    print(s[:-4])
    st = {'a':4, 'b':5}
    print(list(st.values()))
    print(Solution().lengthOfLongestSubstring(s))
    dict = {'1': 'a', '2': 'b', '3': 'c'}
    a = ""
    print([0] + [0])