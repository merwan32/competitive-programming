class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        limit = n/3
        mydict = defaultdict(int)
        result = set()
        for i in nums:
            if i in mydict:
                mydict[i] = mydict[i] +1
                if mydict[i] > limit:
                    result.add(i)
            else:
                mydict[i] = 1
                if mydict[i] > limit:
                    result.add(i)
        return result
            