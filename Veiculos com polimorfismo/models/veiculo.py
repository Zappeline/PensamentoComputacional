class Veiculo():

    def __init__(self, nome, placa, marca, consumo): 
        self.nome = nome
        self.marca = marca
        self.consumo = consumo
        self.__placa = "" 
        self.set_placa(placa)

    def __eq__(self, value):
        if value.get_placa() == self.__placa:
            print(f"O veiculo: {value.nome} e o {self.nome} possuem a mesma placa!")
        else:
            print(f"O veiculo: {value.nome} e o {self.nome} tem placas diferentes!")

    def get_consumo_by_km(self, kilometros):
        consumo = kilometros / self.consumo
        print(f"Em {kilometros}Km, O consumo do veiculo {self.nome} da marca: {self.marca} é de {consumo} litros")
        return consumo
    
    def get_placa(self):
        return self.__placa
    
    def set_placa(self, placa):
        #Verifica se a placa possui 3 letras e 4 numeros
        if len(placa) == 7 and placa[0:3].isalpha() and placa[3:7].isdigit():
            self.__placa = placa
        else:
            print("Placa fora do padrão brasileiro!")

