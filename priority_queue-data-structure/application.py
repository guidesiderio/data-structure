from PriorityQueue import PriorityQueue


def print_menu():
    print("Menu da Fila com Prioridades:")
    print("1. Chegada de pessoa para atendimento normal")
    print("2. Chegada de pessoa para atendimento prioritário")
    print("3. Atendimento de uma pessoa")
    print("4. Listar todas as pessoas da fila")
    print("5. Gerar estatísticas parciais")
    print("6. Sair")


def enqueue(queue):
    name = input("Digite o nome: ")
    queue.enqueue(name)
    print(f"Enfileirado: ({name})")


def dequeue(priority_queue, normal_queue):
    if priority_queue.is_empty() and normal_queue.is_empty():
        print("A fila está vazia.")
    elif not priority_queue.is_empty():
        priority = priority_queue.dequeue()
        print(f"Pessoa atendida: {priority}")
    else:
        normal = normal_queue.dequeue()
        print(f"Pessoa atendida: {normal}")


def print_queue(priority_queue, normal_queue):
    if priority_queue.is_empty() and normal_queue.is_empty():
        print("A fila está vazia.")
    else:
        print(f"Fila com prioridades: {priority_queue.__str__()}")
        print(f"Fila normal: {normal_queue.__str__()}")


def gerar_estatisticas_parciais(priority_queue, normal_queue, total_partial_attendances):
    tam_fila_prioritaria = priority_queue.length
    tam_fila_normal = normal_queue.length

    if total_partial_attendances == 0:
        percentagem_fila_prioritaria = 0
        percentagem_fila_normal = 0
    else:
        percentagem_fila_prioritaria = (
            tam_fila_prioritaria / total_partial_attendances) * 100
        percentagem_fila_normal = (tam_fila_normal / total_partial_attendances) * 100

    print("Estatísticas Parciais do Atendimento")
    print("==========================")
    print(
        f"Porcentagem de atendimentos da fila prioritária: {percentagem_fila_prioritaria}%")
    print(
        f"Porcentagem de atendimentos da fila normal: {percentagem_fila_normal}%")
    print(f"Tamanho da fila prioritária: {tam_fila_prioritaria}")
    print(f"Tamanho da fila normal: {tam_fila_normal}")
    print("==========================")


def gerar_estatisticas_finais(len_priority_queue, len_normal_queue, total_attedances):
    if total_attedances == 0:
        percent_priority_attended = 0
        percent_normal_attended = 0
    else:
        percent_priority_attended = (len_priority_queue / total_attedances) * 100
        percent_normal_attended = (len_normal_queue / total_attedances) * 100

    print("Estatísticas Finais do Atendimento")
    print("===============================")
    print(f"Total de pessoas atendidas: {total_attedances}")
    print(f"Total de pessoas atendidas prioritárias: {len_priority_queue}")
    print(f"Total de pessoas atendidas normais: {len_normal_queue}")
    print(f"Porcentagem de pessoas atendidas prioritárias: {percent_priority_attended}%")
    print(f"Porcentagem de pessoas atendidas normais: {percent_normal_attended}%")
    print("===============================")


def main():
    priority_queue = PriorityQueue()
    normal_queue = PriorityQueue()
    total_partial_attendances = 0
    total_attendances = 0
    len_priority_queue = 0
    len_normal_queue = 0

    while True:
        print_menu()
        choice = input("Digite sua opção: ")

        if choice == "1":
            enqueue(normal_queue)
            total_partial_attendances += 1
            total_attendances += 1
            len_normal_queue += 1
        elif choice == "2":
            enqueue(priority_queue)
            total_partial_attendances += 1
            total_attendances += 1
            len_priority_queue += 1
        elif choice == "3":
            dequeue(priority_queue, normal_queue)
            total_partial_attendances -= 1
        elif choice == "4":
            print_queue(priority_queue, normal_queue)
        elif choice == "5":
            gerar_estatisticas_parciais(priority_queue, normal_queue, total_partial_attendances)
        elif choice == "6":
            if priority_queue.is_empty() and normal_queue.is_empty():
                gerar_estatisticas_finais(len_priority_queue, len_normal_queue, total_attendances)
                print("Encerrando...")
                break
            else:
                print("As filas não estão vazias. Continue atendendo as pessoas.")
        else:
            print("Opção inválida. Por favor, tente novamente.")

        print()


if __name__ == "__main__":
    main()

