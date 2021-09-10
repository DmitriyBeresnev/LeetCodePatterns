

# 234. Palindrome Linked List

'''

234. Palindrome Linked List
Easy

Given the head of a singly linked list, return true if it is a palindrome.



Example 1:

Input: head = [1,2,2,1]
Output: true

Example 2:

Input: head = [1,2]
Output: false



Constraints:

    The number of nodes in the list is in the range [1, 105].
    0 <= Node.val <= 9


Follow up: Could you do it in O(n) time and O(1) space?


'''


import math
import time
import collections
from typing import List, Optional
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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slowPointer = head
        fastPointer = head
        leftSideDigitsList = list()
        rightSideDigitsList = list()
        while fastPointer and fastPointer.next:
            leftSideDigitsList.append(slowPointer.val)
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
        while slowPointer is not None:
            rightSideDigitsList.append(slowPointer.val)
            slowPointer = slowPointer.next
        print(leftSideDigitsList)
        print(rightSideDigitsList)
        if len(leftSideDigitsList) == 0:
            return True
        if len(leftSideDigitsList) == len(rightSideDigitsList)-1:
            if leftSideDigitsList == list(reversed(rightSideDigitsList[1:])):
                return True
        if leftSideDigitsList == list(reversed(rightSideDigitsList)):
            return True
        else:
            return False


# solution after Vlad's tips (Vlad's solution)
class Solution2:
    def middleNode(self, head: ListNode) -> ListNode:
        slowPointer = head
        fastPointer = head
        while fastPointer and fastPointer.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
        return slowPointer

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevPointer = None
        curPointer = head
        while curPointer is not None:
            nextPointer = curPointer.next
            curPointer.next = prevPointer
            prevPointer = curPointer
            curPointer = nextPointer
        return prevPointer

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        middle = self.middleNode(head)
        reversedRightListSideHead = self.reverseList(middle)
        while reversedRightListSideHead is not None:
            if reversedRightListSideHead.val != head.val:
                return False
            head = head.next
            reversedRightListSideHead = reversedRightListSideHead.next
        return True


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
