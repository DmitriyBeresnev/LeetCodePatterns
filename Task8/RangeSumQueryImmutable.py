

# 303. Range Sum Query - Immutable

'''

Range Sum Query - Immutable

Given an integer array nums, handle multiple queries of the following type:

    Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

Implement the NumArray class:

    NumArray(int[] nums) Initializes the object with the integer array nums.
    int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).



Example 1:

Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3



Constraints:

    1 <= nums.length <= 104
    -105 <= nums[i] <= 105
    0 <= left <= right < nums.length
    At most 104 calls will be made to sumRange.



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
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])


# solution after Vlad's tips (Vlad's solution)
class NumArray2:
    def __init__(self, nums: List[int]):
        self.sums = list()
        curSum = 0
        for i, num in enumerate(nums):
            curSum += num
            self.sums.append(curSum)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sums[right]
        return self.sums[right] - self.sums[left-1]


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
