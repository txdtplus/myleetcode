import numpy as np

class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:
        nums.sort()
        n = len(nums)
        best = 10 ** 7

        def update(cur):
            nonlocal best
            if abs(cur - target) < abs(best - target):
                best = cur
        
        for one in range(n):
            if one > 0 and nums[one] == nums[one-1]:
                continue

            two, three = one + 1, n - 1
            while two < three:
                a = nums[one] + nums[two] + nums[three]
                
                if a == target:
                    return target
                
                update(a)
                if a > target:
                    three0 = three - 1
                    while two < three0 and nums[three0] == nums[three]:
                        three0 -= 1              
                    three = three0
                
                else:
                    two0 = two + 1
                    while two0 < three and nums[two0] == nums[two]:
                        two0 += 1
                    two = two0
        
        return best


if __name__ == '__main__':
    nums = [-738,-628,-94,-533,605,514,-345,538,719,-799,-46,428,286,947,-842,24,870,-326,-712,833,-21,395,968,655,-112,-941,-741,126,908,877,-5,534,-834,-627,851,-632,724,831,-428,140,718,-703,-578,-403,-858,871,117,-494,-209,812,885,989,-17,232,-888,-482,-943,89,-964,798,321,-653,828,-560,-318,-208,81,4,102,685,109,-126,-295,888,-692,-210,174,-95,610,-713,955,368,-140,-57,-143,555,986,455,-701,513,-442,879,11,987,310,-687,-949,-558,-883,504,7,-356,-189,-667,-690,892,-523,-379,-610,-748,963,667,-65,-325,525,616,680,-983,726,-172,280,364,777,789,-419,-488,-815,518,995,-199,-69,-440,822,-477,319,-40,344,739,-547,-362,-855,654,-626,849,-148,-60,234,-945,-212,495,129,-129,835,-266,-464,909,-726,-53,668,607,897,-534,-213,635,471,-530,-826,-260,-673,-656,523,-773,-438,492,-469,-753,355,-932,-630,529,-414,-88,512,553,-19,556,-629,872,700,-201,948,369,-955,-747,-114,925,-139,692,754,883,600,-808,847,-205,-918,-393,-735,159,-430,-903,-727]

    nums = np.array(np.array(nums))

    c = np.where(nums < 10000 and nums > 100, 33, nums)

    target = 5969
    s = Solution()
    print(s.threeSumClosest(nums=nums, target=target))