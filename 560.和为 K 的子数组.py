# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 00:04:40 2021

@author: ytgao
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d={}
        nums_sum=0
        count=0
        for n in nums:
            nums_sum+=n
            # 和直接等于k
            if nums_sum ==k:
                count+=1
            # 前缀和等于k
            if nums_sum-k in d:
                count+=d[nums_sum-k]
            d[nums_sum]=d.get(nums_sum,0)+1
        return count