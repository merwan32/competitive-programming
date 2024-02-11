class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        limit = len(nums)//3
        result = set()
        for i,c in Counter(nums).items():
            if c>limit:
                result.add(i)
        
        return result
            