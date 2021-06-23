# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 00:03:17 2021

@author: ytgao
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
    # method 1
        #准备空的进位
        digits=[0]+digits
        for i in range(len(digits)-1,-1,-1):
            #末尾不是9
            if digits[i]!=9:
                digits[i]+=1
                break
             #末尾是9
            else:
                 digits[i]=0
        #如果进位没有用到
        if digits[0]==0:
            digits=digits[1:]
        return digits