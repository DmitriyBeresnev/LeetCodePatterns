

# LeetCode Patterns. Task 13. LeetCode 203. Remove Linked List Elements

'''

203. Remove Linked List Elements
Easy

Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.



Example 1:

Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:

Input: head = [], val = 1
Output: []

Example 3:

Input: head = [7,7,7,7], val = 7
Output: []



Constraints:

    The number of nodes in the list is in the range [0, 104].
    1 <= Node.val <= 50
    0 <= val <= 50




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
    def removeElement(self, prev: ListNode, curr: ListNode) -> ListNode:
        if prev.next == curr.next and prev.val == curr.val:
            return curr.next
        prev.next = curr.next

    def removeElements(self, head: ListNode, val: int) -> ListNode:
        curr = head
        prev = head
        while curr is not None:
            isElementDeleted = False
            if head is not None:
                if head.val == val:
                    head = self.removeElement(prev, head)
                    curr = head
                    prev = head
                    continue
            if curr.val == val:
                self.removeElement(prev, curr)
                isElementDeleted = True
            if not isElementDeleted:
                prev = curr
            curr = curr.next
        return head


# solution after Vlad's tips (Vlad's solution)
class Solution2:
    pass


if __name__ == "__main__":
    #
    start = time.perf_counter()
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    print(solution.removeElements(head, val=2)) # 6
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
