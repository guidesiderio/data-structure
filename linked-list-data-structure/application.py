from LinkedList import LinkedList

def exibir_menu():
    print("Selecione a operação:")
    print("1. Inserir no início da lista")
    print("2. Inserir no final da lista")
    print("3. Remover por valor")
    print("4. Exibir a lista")
    print("5. Sair")


# Função principal da aplicação
def main():
    # Criação da lista encadeada
    linked_list = LinkedList()

    # Loop principal do programa
    while True:
        exibir_menu()
        escolha = input("Opção selecionada: ")

        if escolha == "1":
            data = input("Digite o valor a ser inserido no início da lista: ")
            linked_list.insert_at_beginning(data)
            print("Valor inserido no início da lista.")
        elif escolha == "2":
            data = input("Digite o valor a ser inserido no final da lista: ")
            linked_list.insert_at_end(data)
            print("Valor inserido no final da lista.")
        elif escolha == "3":
            value = input("Digite o valor a ser removido: ")
            linked_list.delete_by_value(value)
        elif escolha == "4":
            linked_list.display()
        elif escolha == "5":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

        print()


# Execução da função principal
if __name__ == "__main__":
    main()
