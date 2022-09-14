from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        bill_dict = {
            5: 0,
            10: 0
        }
        for i in range(len(bills)):
            if bills[i] == 20:
                if bill_dict[10] > 0:
                    bill_dict[10] -= 1
                    bill_dict[5] -= 1
                else:
                    bill_dict[5] -= 3

            elif bills[i] == 10:
                bill_dict[10] += 1
                bill_dict[5] -= 1

            else:
                bill_dict[5] += 1

            if bill_dict[5] < 0:
                return False
        
        return True


if __name__ == '__main__':
    bills = [5,5,5,10,20]
    s = Solution()
    print(s.lemonadeChange(bills))