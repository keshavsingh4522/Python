class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        i = 0
        res = [""]*numRows      # We will fill in each line in the zigzag
        for letter in s:
            if i == numRows-1:  # If this is the last line in the zigzag we go up
                grow = False
            elif i == 0:        #Otherwise we go down
                grow = True 
            res[i] += letter    #Add the letter to its row
            i = (i+1) if grow else i-1  # We increment (add 1) if grow is True, 
			                            # and decrement otherwise
										
        return "".join(res)     # return the joined rows