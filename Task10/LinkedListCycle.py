

# 141. Linked List Cycle

'''

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.



Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.



Constraints:

    The number of the nodes in the list is in the range [0, 104].
    -105 <= Node.val <= 105
    pos is -1 or a valid index in the linked-list.



Follow up: Can you solve it using O(1) (i.e. constant) memory?


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


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# my solution
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slowPointer = head
        fastPointer = head
        while slowPointer is not None:
            slowPointer = slowPointer.next
            # fastPointer = fastPointer.next
            if fastPointer is not None:
                if fastPointer.next is not None:
                    fastPointer = fastPointer.next.next
                else:
                    return False
            if slowPointer == fastPointer and slowPointer is not None and fastPointer is not None:
                return True
        return False


# solution after Vlad's tips (Vlad's solution)
class Solution2:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False

        slow = fast = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False


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
