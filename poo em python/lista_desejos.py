def exibir_menu():
    print(" MINHA LISTA DE DESEJOS ")
    print("1. Ver minha lista")
    print("2. Adicionar um item")
    print("3. Remover um item")
    print("4. Sair do aplicativo")

def main():
    # Inicializa a lista de desejos vazia
    lista_desejos = []
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-4): ")
        
        if opcao == '1':
            # Exibir itens
            if not lista_desejos:
                print("\nSua lista de desejos está vazia no momento.")
            else:
                print("\nSua Lista:")
                for i, item in enumerate(lista_desejos):
                    print(f"{i + 1}. {item}")
                    
        elif opcao == '2':
            # Adicionar item
            novo_item = input("\nDigite o que você deseja adicionar à lista: ")
            # Evita adicionar itens vazios
            if novo_item.strip(): 
                lista_desejos.append(novo_item.strip())
                print(f"'{novo_item.strip()}' foi adicionado com sucesso!")
            else:
                print("O item não pode estar vazio.")
                
        elif opcao == '3':
            # Remover item
            if not lista_desejos:
                print("\nSua lista já está vazia. Não há nada para remover.")
                continue
                
            print("\nSua Lista atual:")
            for i, item in enumerate(lista_desejos):
                print(f"{i + 1}. {item}")
                
            try:
                indice = int(input("\nDigite o NÚMERO do item que deseja remover: "))
                # Ajusta o índice porque as listas em Python começam em 0, mas mostramos a partir de 1
                indice_real = indice - 1 
                
                if 0 <= indice_real < len(lista_desejos):
                    item_removido = lista_desejos.pop(indice_real)
                    print(f"'{item_removido}' foi removido da sua lista!")
                else:
                    print("Número de item inválido.")
            except ValueError:
                print("Por favor, digite um número válido.")
                
        elif opcao == '4':
            # Sair
            print("\nSaindo do aplicativo...")
            break
            
        else:
            # Tratamento de opção inválida
            print("\nOpção inválida. Por favor, escolha um número de 1 a 4.")

if __name__ == "__main__":
    main()