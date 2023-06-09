class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete_by_value(self, value):
        if self.is_empty():
            print("A lista está vazia.")
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next

        print(f"O valor {value} não foi encontrado na lista.")
        

    def insert_ordered(self, data):
        new_node = Node(data)

        # Caso a lista esteja vazia
        if self.head is None:
            self.head = new_node
        # Caso o novo elemento seja menor que o primeiro elemento da lista
        elif data < self.head.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head

            # Encontrar o local correto para inserir o novo elemento
            while current.next is not None and current.next.data < data:
                current = current.next

            new_node.next = current.next
            current.next = new_node


    def display(self):
        if self.is_empty():
            print("A lista está vazia.")
        else:
            current = self.head
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")
