#!/usr/bin/env python
# coding: utf-8

# In[1]:


# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        low , high = 0,1
        while (reader.get(high) < target):
            low = high
            high = 2 * high
        while (low <= high):
            mid = low + (high - low)// 2
            x = reader.get(mid)
            if x == target:
                return mid
            elif target > x:
                low = mid + 1
            elif target < x:
                high = mid -1
                
        return -1

