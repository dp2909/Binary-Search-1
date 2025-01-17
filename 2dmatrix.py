#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if (matrix == None or len(matrix) == 0):
            return False
        m = len(matrix)
        n = len(matrix[0])
        low , high = 0, m*n -1
        while (low <= high):
            mid = low + (high - low) //2
            row = mid // n
            col = mid % n
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                high = mid -1
            else:
                low = mid + 1
                
                
        return False

