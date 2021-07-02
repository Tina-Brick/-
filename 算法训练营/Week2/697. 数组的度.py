# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 22:15:51 2021

@author: ytgao
"""

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        nums_index={}
        #记录每个数出现的位置
        for i in range(len(nums)):
            if nums[i] not in nums_index:
                nums_index[nums[i]]=[i]
            else:
                nums_index[nums[i]].append(i)
                
        nums_degree=max([len(nums_index[num]) for num in nums_index])

        min_sub_len=len(nums)
        for num in nums_index:
            subset=nums_index[num]
            if len(subset)==nums_degree:
                min_sub_len= min(min_sub_len,subset[-1]-subset[0]+1)
        
        return min_sub_len
            