from Stack import Stack

# Função para exibir o menu
def exibir_menu():
    print("===== MENU =====")
    print("1. Exibir a pilha")
    print("2. Adicionar um elemento")
    print("3. Remover um elemento")
    print("4. Exibir o elemento do topo")
    print("5. Exibir o tamanho da pilha")
    print("0. Sair")


# Função principal
def main():
    stack = Stack()
    opcao = None

    while opcao != 0:
        exibir_menu()
        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            print("Pilha:")
            stack.display()
        elif opcao == 2:
            elemento = input("Digite o elemento a ser adicionado: ")
            stack.push(elemento)
            print("Elemento adicionado com sucesso.")
        elif opcao == 3:
            elemento_removido = stack.pop()
            if elemento_removido is not None:
                print("Elemento removido:", elemento_removido)
            else:
                print("A pilha está vazia.")
        elif opcao == 4:
            elemento_topo = stack.peek()
            if elemento_topo is not None:
                print("Elemento do topo:", elemento_topo)
            else:
                print("A pilha está vazia.")
        elif opcao == 5:
            print("Tamanho da pilha:", stack.size())
        elif opcao == 0:
            print("Encerrando o programa...")
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()
    