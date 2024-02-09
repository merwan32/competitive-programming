class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sorted_list = sorted(nums)
        for i in range(n):
            if i != sorted_list[i]:
                return i
        return n