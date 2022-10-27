class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        c = Counter(nums)
        
        r=0
        for x in c:
            if c[x]> len(nums)/2:
                r=x
        return r