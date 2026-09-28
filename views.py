from math import isfinite


def exibir_mensagem(mensagem):
    print(mensagem)


def exibir_menu_principal():
    print("===== LOCADORA DE VEÍCULOS =====")
    print("1 - Cadastrar veículo")
    print("2 - Listar veículos")
    print("3 - Alugar veículo")
    print("4 - Devolver veículo")
    print("0 - Sair")


def exibir_tipos_veiculos():
    print("1 - Carro")
    print("2 - Moto")


def exibir_veiculos(veiculos):
    for veiculo in veiculos:
        print(veiculo.exibir_informacoes())
        print()


def exibir_resumo_aluguel(modelo, dias, valor_total):
    valor_formatado = f"{valor_total:.2f}".replace(".", ",")
    print(f"Veículo: {modelo}")
    print(f"Quantidade de dias: {dias}")
    print(f"Valor do aluguel: R$ {valor_formatado}")


def ler_texto(mensagem):
    return input(mensagem).strip()


def ler_inteiro_positivo(mensagem):
    while True:
        try:
            valor = int(ler_texto(mensagem))
        except ValueError:
            exibir_mensagem("Digite um número inteiro maior que zero.")
            continue

        if valor > 0:
            return valor

        exibir_mensagem("Digite um número inteiro maior que zero.")


def ler_valor_positivo(mensagem):
    while True:
        try:
            valor = float(ler_texto(mensagem).replace(",", "."))
        except ValueError:
            exibir_mensagem("Digite um valor numérico maior que zero.")
            continue

        if isfinite(valor) and valor > 0:
            return valor

        exibir_mensagem("Digite um valor numérico maior que zero.")
