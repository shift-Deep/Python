class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


# Don't change the code above.


def addTwoNumbers(head1: Node, head2: Node) -> Node:
    # Write your code here.
    carry = (head1.data + head2.data)//10
    result = Node((head1.data + head2.data)%10,None)
    head = result
    temp1 = head1.next
    temp2 = head2.next
    while temp1 or temp2:
        if temp1 and temp2:
            result.next = Node((temp1.data + temp2.data + carry)%10)
            carry = (temp1.data + temp2.data + carry)//10
            temp1 = temp1.next
            temp2 = temp2.next
            result = result.next
            # print("hello"+str(carry))
        elif temp1:
            
            if carry == 0:
                result.next = Node(temp1.data)
            else:
                result.next = Node((temp1.data + carry)%10)
                carry = (temp1.data+carry)//10
            temp1 = temp1.next
            result = result.next
        elif temp2:
            if carry == 0:
                result.next = Node(temp2.data)
            else:
                result.next = Node((temp2.data + carry)%10)
                carry = (temp2.data+carry)//10
            temp2 = temp2.next
            result = result.next
        if carry != 0:
            result.next = Node(carry)
    return head