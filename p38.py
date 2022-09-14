class Solution:
    def countAndSay(self, n: int) -> str:

        def describe_str(input_str: str) -> str:

            if len(input_str) < 2:
                return "11"
            
            out_str = ""
            value = input_str[0]
            count = 1
    
            for i in range(1, len(input_str)):
                if input_str[i] != value:
                    out_str += str(count)
                    out_str += value
                    value = input_str[i]
                    count = 1
                else:
                    count += 1
                
                if i == len(input_str) - 1:
                    out_str += str(count)
                    out_str += value
            
            return out_str

        for i in range(n):
            if i == 0:
                out_str = "1"
            else:
                out_str = describe_str(out_str)
        
        return out_str

        
if __name__ == '__main__':
    a = 5
    s = Solution()
    print(s.countAndSay(a))