from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_list = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = new_list
            new_list = curr
            curr = next_node
        
        return new_list

# Função para criar uma lista ligada a partir de uma lista normal
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for num in arr[1:]:
        curr.next = ListNode(num)
        curr = curr.next
    return head

# Função para imprimir uma lista ligada
def print_linked_list(head):
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    print(" -> ".join(vals))

# Teste
head = create_linked_list([1, 2, 3, 4, 5])
sol = Solution()
reversed_head = sol.reverseList(head)
print_linked_list(reversed_head)
