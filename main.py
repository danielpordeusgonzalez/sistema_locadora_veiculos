import controllers
import views


def main():
    while True:
        views.exibir_menu_principal()
        opcao = views.ler_texto("Escolha uma opção: ")

        if opcao == "1":
            controllers.cadastrar_veiculo()
        elif opcao == "2":
            controllers.listar_veiculos()
        elif opcao == "3":
            controllers.alugar_veiculo()
        elif opcao == "4":
            controllers.devolver_veiculo()
        elif opcao == "0":
            break
        else:
            views.exibir_mensagem("Opção inválida.")


if __name__ == "__main__":
    main()
