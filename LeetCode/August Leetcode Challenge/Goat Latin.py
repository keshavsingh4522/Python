# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/551/week-3-august-15th-august-21st/3429/
class Solution:
    def toGoatLatin(self, S: str) -> str:
        s=S.split()
        for i in range(len(s)):
            if s[i][0] in 'aeiouAEIOU':
                s[i]+='ma'+'a'*(i+1)
            else:
                s[i]=s[i][1:]+s[i][0]+'ma'+'a'*(i+1)
        return ' '.join(s)