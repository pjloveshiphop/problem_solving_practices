class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        c = Counter(nums)
        ans=0
        for x in c:
            if c[x]==1:
                ans=x
        return ans
        