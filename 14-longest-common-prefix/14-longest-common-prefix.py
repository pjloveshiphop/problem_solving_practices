from collections import Counter
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        else:
            s=sorted(strs)
            x=s.pop(0)
            answer=[]
            for i in range(len(x)):
                if x[i]==s[-1][i]:
                    answer.append(x[i])
                else:
                    break

            return "".join(answer)

        
        