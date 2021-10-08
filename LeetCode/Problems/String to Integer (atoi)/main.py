import re
pattern = '.*?([+-]?\d+)'

class Solution:
    def myAtoi(self, str: str) -> int:
        result = re.match(pattern, str)
        lstr = str.rstrip().lstrip()
        if not result:
            return 0
        if not(lstr[:len(result.group(1))] == result.group(1)):
            return 0
        
        if result.group(1)[0] != "-":
            return 2147483647 if 2147483647 < int(result.group(1)) else int(result.group(1))
        else:
            return -2147483648 if - int(result.group(1)[1:]) < -2147483648 else - int(result.group(1)[1:])
