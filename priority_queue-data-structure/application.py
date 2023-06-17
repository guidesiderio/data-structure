from PriorityQueue import PriorityQueue


def print_menu():
    print("Menu da Fila com Prioridades:")
    print("1. Enfileirar")
    print("2. Desenfileirar")
    print("3. Visualizar Próximo")
    print("4. Imprimir Fila")
    print("5. Sair")


def enqueue(queue):
    item = input("Digite o item: ")
    priority = int(input("Digite a prioridade: "))
    queue.enqueue(item, priority)
    print(f"Enfileirado: ({item}, {priority})")


def dequeue(queue):
    item = queue.dequeue()
    if item is None:
        print("A fila com prioridades está vazia.")
    else:
        print(f"Desenfileirado: {item}")


def peek(queue):
    item = queue.peek()
    if item is None:
        print("A fila com prioridades está vazia.")
    else:
        print(f"Próximo item: {item}")


def print_queue(queue):
    if queue.is_empty():
        print("A fila com prioridades está vazia.")
    else:
        print(queue.__str__())


def main():
    queue = PriorityQueue()

    while True:
        print_menu()
        choice = input("Digite sua escolha: ")

        if choice == "1":
            enqueue(queue)
        elif choice == "2":
            dequeue(queue)
        elif choice == "3":
            peek(queue)
        elif choice == "4":
            print_queue(queue)
        elif choice == "5":
            print("Encerrando...")
            break
        else:
            print("Escolha inválida. Por favor, tente novamente.")

        print()


if __name__ == "__main__":
    main()
