class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        result = []
        for i in nums:
            if i >= 0:
                pos.append(i)
            else:
                neg.append(i)
        for i in range(len(pos)):
            result.append(pos[i])
            result.append(neg[i])
        return result