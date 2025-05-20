class Frota:
    """
    Classe para gerenciar uma frota de veículos.
    """
    def __init__(self):
        self.__veiculos = []  # Lista privada para armazenar os veículos

    def adicionar_veiculo(self, veiculo):
        """
        Adiciona um veículo à frota.
        """
        if isinstance(veiculo, Veiculo):
            self.__veiculos.append(veiculo)
            print(f"Veículo '{veiculo.marca} {veiculo.modelo}' adicionado à frota.")
        else:
            print("Erro: O objeto não é um Veículo ou subclasse de Veículo.")

    def listar_veiculos(self):
        """
        Lista todos os veículos da frota.
        """
        if not self.__veiculos:
            print("A frota está vazia.")
            return

        print("\n--- Veículos na Frota ---")
        for i, veiculo in enumerate(self.__veiculos):
            print(f"{i+1}. {veiculo}")
        print("------------------------")

    def calcular_consumo_total_frota(self, distancia):
        """
        Calcula o consumo total de combustível da frota para uma distância informada.
        """
        if not self.__veiculos:
            print("A frota está vazia, não é possível calcular o consumo.")
            return 0.0

        consumo_total = 0.0
        for veiculo in self.__veiculos:
            consumo_total += veiculo.calcular_consumo(distancia)
        return consumo_total