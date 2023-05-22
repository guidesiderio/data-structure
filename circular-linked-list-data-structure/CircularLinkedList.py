class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_end(self, data):
        if self.is_empty():
            new_node = Node(data)
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                if current.data == data:
                    print("Nome repetido. Não é possível inserir.")
                    return
                current = current.next
            if current.data == data:  # Verificar último nó
                print("Nome repetido. Não é possível inserir.")
                return

            new_node = Node(data)
            current.next = new_node
            new_node.next = self.head

    def insert_at_beginning(self, data):
        if self.is_empty():
            new_node = Node(data)
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                if current.next.data == data:
                    print("Nome repetido. Não é possível inserir.")
                    return
                current = current.next
            if current.next.data == data:  # Verificar primeiro nó
                print("Nome repetido. Não é possível inserir.")
                return

            new_node = Node(data)
            new_node.next = self.head
            current.next = new_node
            self.head = new_node

    def delete_node(self, key):
        if self.is_empty():
            print("A lista está vazia.")
            return

        if self.head.data == key:
            if self.head.next == self.head:  # Verifica se é o único elemento da lista
                self.head = None
            else:
                current = self.head
                while current.next != self.head:
                    current = current.next
                current.next = self.head.next
                self.head = self.head.next
        else:
            current = self.head
            prev = None
            while current.next != self.head:
                prev = current
                current = current.next
                if current.data == key:
                    prev.next = current.next
                    break
            if current.next == self.head:
                print("O elemento", key, "não foi encontrado na lista.")

    def display(self):
        if self.is_empty():
            print("A lista está vazia.")
        else:
            current = self.head
            count = 0
            while True:
                print(current.data, end=" ")
                count += 1
                current = current.next
                if current == self.head:
                    break
            print("\nQuantidade de nomes:", count)

    def display_reverse(self):
        if self.is_empty():
            print("A lista está vazia.")
        else:
            names = []
            current = self.head
            while True:
                names.append(current.data)
                current = current.next
                if current == self.head:
                    break
            names.reverse()
            for name in names:
                print(name, end=" ")
            print()
