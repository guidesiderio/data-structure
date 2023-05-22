from CircularLinkedList import CircularLinkedList

def display_menu():
    print("Menu de Opções:")
    print("1. Inserir nome no final da lista")
    print("2. Inserir nome no início da lista")
    print("3. Excluir nome")
    print("4. Exibir nomes")
    print("5. Exibir nomes em ordem inversa")
    print("6. Sair")

# Função principal
def main():
    clist = CircularLinkedList()

    while True:
        display_menu()
        choice = input("Digite o número da opção desejada: ")

        if choice == "1":
            nome = input("Digite o nome a ser inserido no final: ")
            clist.insert_at_end(nome)
        elif choice == "2":
            nome = input("Digite o nome a ser inserido no início: ")
            clist.insert_at_beginning(nome)
        elif choice == "3":
            nome = input("Digite o nome a ser excluído: ")
            clist.delete_node(nome)
        elif choice == "4":
            clist.display()
        elif choice == "5":
            clist.display_reverse()
        elif choice == "6":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

        print()

# Executar o programa
if __name__ == "__main__":
    main()
