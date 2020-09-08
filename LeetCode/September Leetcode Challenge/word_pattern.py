# https://leetcode.com/problems/word-pattern/
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        d=dict()
        str=str.split(' ')
        s=''
        if len(pattern)==len(str):
            for i,j in zip(pattern,str):
                if d.get(i,0)==0:
                    if j in s:
                        return False
                    d[i]=j
                    s+=j
                else:
                    if d[i]!=j:
                        return False
            return True
        return False
