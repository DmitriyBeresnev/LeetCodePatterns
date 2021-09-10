

# 136. Single Number

'''

Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.



Example 1:

Input: nums = [2,2,1]
Output: 1

Example 2:

Input: nums = [4,1,2,1,2]
Output: 4

Example 3:

Input: nums = [1]
Output: 1



Constraints:

    1 <= nums.length <= 3 * 104
    -3 * 104 <= nums[i] <= 3 * 104
    Each element in the array appears twice except for one element which appears only once.



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


# my solution
class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        originalSum = sum(nums)
        uniqueArr = list(set(nums))
        idealSum = 0
        for num in uniqueArr:
            idealSum += num + num
        return idealSum - originalSum


# solution after Vlad's tips
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        resMask = 0
        for num in nums:
            resMask ^= num
        return resMask


if __name__ == "__main__":
    #
    start = time.perf_counter()
    solution = Solution()
    print(solution.singleNumber(nums = [2,2,1]))
    end = time.perf_counter()
    print(f"test 1: {end - start:10.6f} sec")
    #
    start2 = time.perf_counter()
    print(solution.singleNumber(nums = [4,1,2,1,2]))
    end2 = time.perf_counter()
    print(f"test 2: {end2 - start2:10.6f} sec")
    #
    start3 = time.perf_counter()
    print(solution.singleNumber(nums = [1]))
    end3 = time.perf_counter()
    print(f"test 3: {end3 - start3:10.6f} sec")
    #
    start4 = time.perf_counter()
    print(solution.findDisappearedNumbers(nums = [5,4,6,7,9,3,10,9,5,6]))
    end4 = time.perf_counter()
    print(f"test 4: {end4 - start4:10.6f} sec")
    #
    start5 = time.perf_counter()
    print(solution.missingNumber(nums = [1]))
    end5 = time.perf_counter()
    print(f"test 5: {end5 - start5:10.6f} sec")
    #
    start6 = time.perf_counter()
    print(solution.firstMissingPositive([1, 1]))
    end6 = time.perf_counter()
    print(f"test 6: {end6 - start6:10.6f} sec")
