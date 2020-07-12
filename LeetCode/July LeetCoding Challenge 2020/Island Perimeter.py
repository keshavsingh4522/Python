'''
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:


'''

class Solution:
    def islandPerimeter(self, mat: List[List[int]]) -> int:
        def numofneighbour(mat, i, j): 
            count = 0; 
            if (i > 0 and mat[i - 1][j]): 
                count+= 1; 
            if (j > 0 and mat[i][j - 1]): 
                count+= 1; 
            if (i < R-1 and mat[i + 1][j]): 
                count+= 1
            if (j < C-1 and mat[i][j + 1]): 
                count+= 1; 
            return count; 
        def findperimeter(mat): 
            perimeter = 0; 
            for i in range(0, R): 
                for j in range(0, C): 
                    if (mat[i][j]): 
                        perimeter += (4 - numofneighbour(mat, i, j)); 
            return perimeter; 
        R = len(mat)
        C = len(mat[0])
        return(findperimeter(mat));