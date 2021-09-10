

# 268. Missing Number

'''

268. Missing Number

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?



Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

Example 4:

Input: nums = [0]
Output: 1
Explanation: n = 1 since there is 1 number, so all numbers are in the range [0,1]. 1 is the missing number in the range since it does not appear in nums.



Constraints:

    n == nums.length
    1 <= n <= 104
    0 <= nums[i] <= n
    All the numbers of nums are unique.



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
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sortedNums = None
        if n == 1:
            if nums[0] == 0:
                return nums[0] + 1
            else:
                return nums[0] - 1
        if n > 1:
            sortedNums = sorted(nums)
            for i in range(0, n-1):
                if sortedNums[i+1] - sortedNums[i] > 1:
                    return sortedNums[i] + 1
            minVal = sortedNums[0]
            if minVal == 0:
                return sortedNums[n-1] + 1
            else:
                return minVal-1

# solution after Vlad's tips (use ariphmetic progression sum, n+1 - sum of ideal sequence from 0 till n)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n*(n+1) // 2 - sum(nums)


if __name__ == "__main__":
    #
    start = time.perf_counter()
    solution = Solution()
    print(solution.missingNumber(nums = [3,0,1]))
    end = time.perf_counter()
    print(f"test 1: {end - start:10.6f} sec")
    #
    start2 = time.perf_counter()
    print(solution.missingNumber([0,1]))
    end2 = time.perf_counter()
    print(f"test 2: {end2 - start2:10.6f} sec")
    #
    start3 = time.perf_counter()
    print(solution.missingNumber(nums = [9,6,4,2,3,5,7,0,1]))
    end3 = time.perf_counter()
    print(f"test 3: {end3 - start3:10.6f} sec")
    #
    start4 = time.perf_counter()
    print(solution.missingNumber(nums = [0]))
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
