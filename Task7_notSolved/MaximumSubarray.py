

# 53. Maximum Subarray

'''

Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:

Input: nums = [1]
Output: 1

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23



Constraints:

    1 <= nums.length <= 3 * 104
    -105 <= nums[i] <= 105



Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


'''


import math
import time
import collections
from typing import List
import numpy as np
import random as rnd
import itertools as it
from collections import defaultdict, Counter
import re
from functools import reduce
from bisect import bisect, bisect_left


# my solution (see discussion section of leetcode, Kadane's algorithm)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        curSum = 0
        bestSum = nums[0]
        for i in range(0, n):
            curSum = max(curSum + nums[i], nums[i])
            bestSum = max(bestSum, curSum)
        return bestSum


# solution after Vlad's tips (Vlad's solution)
class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        pass


if __name__ == "__main__":
    #
    start = time.perf_counter()
    solution = Solution()
    print(solution.maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4])) # 6
    end = time.perf_counter()
    print(f"test 1: {end - start:10.6f} sec")
    #
    start2 = time.perf_counter()
    print(solution.maxSubArray(nums = [1])) # 1
    end2 = time.perf_counter()
    print(f"test 2: {end2 - start2:10.6f} sec")
    #
    start3 = time.perf_counter()
    print(solution.maxSubArray(nums = [5,4,-1,7,8])) # 23
    end3 = time.perf_counter()
    print(f"test 3: {end3 - start3:10.6f} sec")
    #
    start4 = time.perf_counter()
    print(solution.maxProfit(prices = [2,1,2,1,0,1,2])) #
    end4 = time.perf_counter()
    print(f"test 4: {end4 - start4:10.6f} sec")
    #
    start5 = time.perf_counter()
    print(solution.maxProfit(prices = [3,3,5,0,0,3,1,4])) #
    end5 = time.perf_counter()
    print(f"test 5: {end5 - start5:10.6f} sec")
    #
    start6 = time.perf_counter()
    print(solution.firstMissingPositive([1, 1]))
    end6 = time.perf_counter()
    print(f"test 6: {end6 - start6:10.6f} sec")
