from typing import Optional, List
import numpy as np
l1=[2,4,3]
l2 =[5,6,4]
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def add(self,head,val):
        if head==None:
            head=ListNode(val)
            return head
        else:
            curr=head
            while curr.next:
                curr= curr.next
            curr.next =ListNode(val)
            return head

# def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         rl1 = []
#         rl2 = []
#         for i in l1[::-1]:
#             rl1.append(str(i))
#         for i in l2[::-1]:
#             rl2.append(str(i))
#         convertedl1 = ''.join(rl1)
#         convertedl2 = ''.join(rl2)
#         cal = int(convertedl1) + int(convertedl2)
#         converted_ans = [int(i) for i in (list(str(cal))[::-1])]
#         return converted_ans

# print(addTwoNumbers(l1,l2))
# l_1=ListNode(l1)
# l_2=ListNode(l2)
# convertedl2=[(i) for i in l_2.val[::-1]]
# convertedl1=[(i) for i in l_1.val[::-1]]
# a=[[i,v] for i,v in zip(convertedl1,convertedl2)]
# b=np.array(convertedl1)
# c=np.array(convertedl2)
#
# d=list(np.add(b,c))
# ll=ListNode()
# for i in d:
#     ll(i)
# print(ll)

l=ListNode()



