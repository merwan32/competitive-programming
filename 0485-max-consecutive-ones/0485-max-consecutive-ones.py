class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = 0
        maxc = 0
        for i in nums:
            if i == 1:
                c = c +1
            else:
                maxc = max(maxc,c)
                c = 0
        return max(maxc,c)