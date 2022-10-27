class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        
        if len(s1) >= len(s2):
            return [x for x in s1 if x in s2]
        elif len(s2) >= len(s1):
            return [x for x in s2 if x in s1]
        
                    
        