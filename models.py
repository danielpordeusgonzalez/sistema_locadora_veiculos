veiculos = []


class Veiculo:
    def __init__(self, modelo, placa, valor_diaria):
        self.modelo = modelo
        self.placa = placa
        self.valor_diaria = valor_diaria
        self._disponivel = True

    def esta_disponivel(self):
        return self._disponivel

    def alugar(self):
        if not self._disponivel:
            return "Veículo indisponível."

        self._disponivel = False
        return "Veículo alugado com sucesso."

    def devolver(self):
        if self._disponivel:
            return "Veículo já está disponível."

        self._disponivel = True
        return "Veículo devolvido com sucesso."

    def calcular_aluguel(self, dias):
        return self.valor_diaria * dias

    def exibir_informacoes(self):
        disponibilidade = "Sim" if self._disponivel else "Não"
        diaria = f"{self.valor_diaria:.2f}".replace(".", ",")

        return (
            f"Modelo: {self.modelo}\n"
            f"Placa: {self.placa}\n"
            f"Diária: R$ {diaria}\n"
            f"Disponível: {disponibilidade}"
        )


class Carro(Veiculo):
    def __init__(self, modelo, placa, valor_diaria, quantidade_portas):
        super().__init__(modelo, placa, valor_diaria)
        self.quantidade_portas = quantidade_portas

    def calcular_aluguel(self, dias):
        return self.valor_diaria * dias

    def exibir_informacoes(self):
        informacoes = super().exibir_informacoes()
        return f"Carro\n{informacoes}\nPortas: {self.quantidade_portas}"


class Moto(Veiculo):
    def __init__(self, modelo, placa, valor_diaria, cilindradas):
        super().__init__(modelo, placa, valor_diaria)
        self.cilindradas = cilindradas

    def calcular_aluguel(self, dias):
        return self.valor_diaria * dias * 0.9

    def exibir_informacoes(self):
        informacoes = super().exibir_informacoes()
        return f"Moto\n{informacoes}\nCilindradas: {self.cilindradas}"
