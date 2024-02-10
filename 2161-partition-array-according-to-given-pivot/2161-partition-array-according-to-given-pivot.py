class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        greater = []
        for i in nums:
            if i < pivot:
                less.append(i)
            elif i>pivot:
                greater.append(i)
        return less+[pivot]*(len(nums)-len(less)-len(greater))+greater