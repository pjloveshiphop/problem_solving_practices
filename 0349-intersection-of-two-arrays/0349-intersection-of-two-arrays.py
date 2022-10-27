class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = set(nums1+nums2)
        r=[]
        for x in s:
            if x in nums1 and x in nums2:
                r.append(x)
        return r
                    
        