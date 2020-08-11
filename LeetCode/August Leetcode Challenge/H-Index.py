# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/550/week-2-august-8th-august-14th/3420/
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        count=0
        for i in range(len(citations)):
            if (i+1)<=citations[i]:
                count+=1
        return count