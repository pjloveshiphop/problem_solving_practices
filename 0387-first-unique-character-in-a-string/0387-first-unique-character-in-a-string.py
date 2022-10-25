class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        c = Counter(s)
        ans = []
        for x in c:
            if c[x] >1:
                continue
            else:
                ans.append(s.index(x))
        return min(ans) if len(ans)!=0 else -1
                
        