

# 448. Find All Numbers Disappeared in an Array

'''

Find All Numbers Disappeared in an Array

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.



Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:

Input: nums = [1,1]
Output: [2]



Constraints:

    n == nums.length
    1 <= n <= 105
    1 <= nums[i] <= n



Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.


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
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        resList = list()
        sortedNums = list(set(sorted(nums)))
        nSortedArr = len(sortedNums)
        if nSortedArr == 1:
            if nums[0] == 1:
                return [2]
            else:
                return [nums[0] - 1]
        if n > 1:
            for i in range(0, nSortedArr - 1):
                if sortedNums[i + 1] - sortedNums[i] > 1:
                    for num in range(sortedNums[i], sortedNums[i + 1]-1):
                        resList.append(num+1)
            minVal = sortedNums[0]
            maxVal = sortedNums[nSortedArr-1]
            if minVal == 1 and nSortedArr == n:
                return resList
            else:
                for num in range(1, minVal):
                    resList.append(num)
                for num in range(maxVal, n):
                    resList.append(num + 1)
                return sorted(resList)


# solution after Vlad's tips
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # special sort (cyclic sort)
        i = 0
        n = len(nums)
        while i < n:
            # save correct pos of cur num
            pos = nums[i] - 1
            if nums[i] != nums[pos]:
                nums[i], nums[pos] = nums[pos], nums[i]
            else:
                i += 1
        resList = list()
        for i in range(0, n):
            if nums[i] != i+1:
                resList.append(i+1)
        return resList


if __name__ == "__main__":
    #
    start = time.perf_counter()
    solution = Solution()
    print(solution.findDisappearedNumbers(nums = [4,3,2,7,8,2,3,1]))
    end = time.perf_counter()
    print(f"test 1: {end - start:10.6f} sec")
    #
    start2 = time.perf_counter()
    print(solution.findDisappearedNumbers(nums = [1,1]))
    end2 = time.perf_counter()
    print(f"test 2: {end2 - start2:10.6f} sec")
    #
    start3 = time.perf_counter()
    print(solution.findDisappearedNumbers(nums = [1,1,2,2]))
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
