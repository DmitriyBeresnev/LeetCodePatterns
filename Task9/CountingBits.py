

# 338. Counting Bits

'''

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.



Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101



Constraints:

    0 <= n <= 105



Follow up:

    It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
    Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?



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
class Solution:
    def countBits(self, n: int) -> List[int]:
        nums = list(range(1, n+1))
        onesSums = [0]
        for num in nums:
            binNum = list(bin(num)[2:])
            binNum = [int(bit) for bit in binNum]
            onesSums.append(sum(binNum))
        return onesSums


# solution after Vlad's tips (Vlad's solution)
class Solution2:
    def countBits(self, n: int) -> List[int]:
        memo = [0] * (n + 1)
        for i in range(1, n + 1):
            memo[i] = memo[i >> 1] + i % 2

        return memo[:n + 1]


if __name__ == "__main__":
    #
    start = time.perf_counter()
    solution = Solution()
    print(solution.countBits(n = 2)) # 6
    end = time.perf_counter()
    print(f"test 1: {end - start:10.6f} sec")
    #
    start2 = time.perf_counter()
    print(solution.countBits(n = 5)) # 1
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
