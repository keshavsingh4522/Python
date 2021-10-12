from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadEndSet = set(deadends)
        queue = deque()
        queue.append(('0000', 0))
        visited = set('0000')

        while queue:
            curStr, curSteps = queue.popleft()

            if curStr == target:
                return curSteps

            if curStr in deadEndSet:
                continue

            for i in range(4):
                digit = int(curStr[i])
                for dir in [1, -1]:
                    newDigit = (digit + dir) % 10

                    newStr = curStr[:i] + str(newDigit) + curStr[i+1:]

                    if newStr not in visited:
                        visited.add(newStr)
                        queue.append((newStr, curSteps+1))

        return -1
