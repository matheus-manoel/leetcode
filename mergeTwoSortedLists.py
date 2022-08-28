# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
def mergeTwoLists(list1, list2):
    pointer_1 = list1
    pointer_2 = list2
    pointer_3 = None
    new_list_head = None

    while pointer_1 or pointer_2:
        if (pointer_1 and pointer_2 and pointer_1.val < pointer_2.val) or (
                pointer_1 and not pointer_2):
            if new_list_head is None:
                pointer_3 = pointer_1
                new_list_head = pointer_3
            else:
                pointer_3.next = pointer_1
                pointer_3 = pointer_1
            pointer_1 = pointer_1.next
        elif (pointer_1 and pointer_2 and pointer_2.val <= pointer_1.val) or (
                pointer_2 and not pointer_1):
            if new_list_head is None:
                pointer_3 = pointer_2
                new_list_head = pointer_3
            else:
                pointer_3.next = pointer_2
                pointer_3 = pointer_2
            pointer_2 = pointer_2.next

    return new_list_head
'''


def mergeTwoLists(list1, list2):
    dummy = ListNode()
    list3 = dummy

    while list1 and list2:
        if list1.val < list2.val:
            list3.next = list1
            list1 = list1.next
        else:
            list3.next = list2
            list2 = list2.next
        list3 = list3.next

    if list1:
        list3.next = list1
    if list2:
        list3.next = list2

    return dummy.next


c = ListNode(8)
b = ListNode(5, c)
a = ListNode(1, b)

d2 = ListNode(9)
c2 = ListNode(8, d2)
b2 = ListNode(3, c2)
a2 = ListNode(1, b2)

result = mergeTwoLists(a, a2)

while (result is not None):
    print(result.val)
    result = result.next
