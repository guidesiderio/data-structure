class Node:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, item, priority):
        new_node = Node(item, priority)

        if self.is_empty() or priority < self.head.priority:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and priority >= current.next.priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def dequeue(self):
        if self.is_empty():
            return None

        item = self.head.item
        self.head = self.head.next
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.head.item

    def __str__(self):
        current = self.head
        queue_str = ""
        while current is not None:
            queue_str += f"({current.item}, {current.priority}) "
            current = current.next
        return queue_str
