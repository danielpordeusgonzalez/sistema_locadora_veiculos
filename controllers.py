import views
from models import Carro, Moto, veiculos


def cadastrar_veiculo():
    views.exibir_tipos_veiculos()
    tipo = views.ler_texto("Tipo de veículo: ")

    if tipo not in ("1", "2"):
        views.exibir_mensagem("Opção inválida.")
        return

    modelo = views.ler_texto("Modelo: ")
    placa = views.ler_texto("Placa: ").upper()

    if not modelo or not placa:
        views.exibir_mensagem("Modelo e placa não podem ficar vazios.")
        return

    if buscar_veiculo_por_placa(placa) is not None:
        views.exibir_mensagem("Já existe um veículo cadastrado com essa placa.")
        return

    valor_diaria = views.ler_valor_positivo("Valor da diária: ")

    if tipo == "1":
        quantidade_portas = views.ler_inteiro_positivo("Quantidade de portas: ")
        veiculo = Carro(modelo, placa, valor_diaria, quantidade_portas)
    else:
        cilindradas = views.ler_inteiro_positivo("Cilindradas: ")
        veiculo = Moto(modelo, placa, valor_diaria, cilindradas)

    veiculos.append(veiculo)
    views.exibir_mensagem("Veículo cadastrado com sucesso.")


def listar_veiculos():
    if not veiculos:
        views.exibir_mensagem("Nenhum veículo cadastrado.")
        return

    views.exibir_veiculos(veiculos)


def buscar_veiculo_por_placa(placa):
    placa = placa.strip().upper()

    for veiculo in veiculos:
        if veiculo.placa == placa:
            return veiculo

    return None


def alugar_veiculo():
    if not veiculos:
        views.exibir_mensagem("Nenhum veículo cadastrado.")
        return

    placa = views.ler_texto("Placa do veículo: ")
    dias = views.ler_inteiro_positivo("Quantidade de dias: ")
    veiculo = buscar_veiculo_por_placa(placa)

    if veiculo is None:
        views.exibir_mensagem("Veículo não encontrado.")
        return

    if veiculo.esta_disponivel():
        valor_total = veiculo.calcular_aluguel(dias)
        views.exibir_resumo_aluguel(veiculo.modelo, dias, valor_total)

    views.exibir_mensagem(veiculo.alugar())


def devolver_veiculo():
    if not veiculos:
        views.exibir_mensagem("Nenhum veículo cadastrado.")
        return

    placa = views.ler_texto("Placa do veículo: ")
    veiculo = buscar_veiculo_por_placa(placa)

    if veiculo is None:
        views.exibir_mensagem("Veículo não encontrado.")
        return

    views.exibir_mensagem(veiculo.devolver())
