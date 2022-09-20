from typing import Optional

class ListNode:

    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:


    def make_answer(self,answer):
        main = ListNode()
        cur = main
        count = 1
        for i in answer:
            cur.val = i
            if count == len(answer):
                cur.next = None
            else:
                cur.next = ListNode()
            cur = cur.next
            count = count + 1
        return main

    def convert(self,linked):
        cur = linked
        simple = []
        while cur.next is not None:
            simple.append(cur.val)
            cur = cur.next
        simple.append(cur.val)
        return simple

    def __adder(self,l1,l2):
        answer = []
        in_my_fucking_mind = 0
        for i in range(len(l2)):
            current = l1[i] + l2[i] + in_my_fucking_mind
            if current >= 10:
                answer.append(int(str(current)[1]))
                in_my_fucking_mind = int(str(current)[0])
            else:
                in_my_fucking_mind = 0
                answer.append(current)
        for i in range(len(l2),len(l1)):
            current = l1[i] + in_my_fucking_mind
            if current >= 10:
                answer.append(int(str(current)[1]))
                in_my_fucking_mind = int(str(current)[0])
            else:
                in_my_fucking_mind = 0
                answer.append(current)
        if in_my_fucking_mind != 0:
            answer.append(in_my_fucking_mind)

        return self.make_answer(answer)

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        lis1 = self.convert(l1)
        lis2 = self.convert(l2)

        if len(lis1) > len(lis2):
            return self.__adder(lis1,lis2)
        else:
            return self.__adder(lis2, lis1)

#l1 = [2,4,3], l2 = [5,6,4]
obj = Solution()
#
l1 = ListNode(2,ListNode(4,ListNode(3)))
l2 = ListNode(5,ListNode(6,ListNode(4)))
#
answer = obj.addTwoNumbers(l1,l2)
print(answer)