class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.head = None
        self.length = 0


    def is_empty(self):
        return self.head is None

    def length(self):
        return self.length


    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1    


    def dequeue(self):
        if self.is_empty():
            return None

        item = self.head.item
        self.head = self.head.next
        self.length -= 1
        return item


    def peek(self):
        if self.is_empty():
            return None
        return self.head.item


    def __str__(self):
        current = self.head
        queue_str = ""
        while current is not None:
            queue_str += f"({current.item}) "
            current = current.next
        return queue_str
