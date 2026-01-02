class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def print(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while current.next is not None:
            print(current.value, "-->", end=" ")
            current = current.next
        print(current.value)

    def reverse(self):
        if self.head is None:
            print("List is empty")
            return
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


def main():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.print()
    ll.reverse()
    ll.print()

if __name__ == "__main__":
    main()
