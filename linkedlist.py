class Node:
    def __init__(self,data):
        self.data = data
        self.next=None
        self.random = None

def deepcopier(head):
    d = Node(head.data)
    newhead=d
    map ={}
    curr1 = head
    curr2 = newhead
    while curr1:
        nxt = curr1.next
        if nxt:
            curr2.next=Node(nxt.data)
        map[nxt] = curr2.next
        curr2 =curr2.next
        curr1=curr1.next
    curr1 = head
    curr2 = newhead
    while curr1:
        curr2.random=map[curr1.random]
        curr1=curr1.next
        curr2 = curr2.next
    return newhead

# given that only head node is given in input

