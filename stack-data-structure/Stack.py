class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def pop(self):
        if self.is_empty():
            return None
        popped_node = self.head
        self.head = self.head.next
        popped_node.next = None
        self.length -= 1
        return popped_node.data

    def peek(self):
        if self.is_empty():
            return None
        return self.head.data

    def size(self):
        return self.length

    def display(self):
        current = self.head
        if current is None:
            print("A pilha está vazia.")
            return
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

