class Veiculos:
    def __init__(self, modelo, marca, placa, ano, cor, velocidade, latitude, longetude):
        self.modelo = modelo
        self.marca = marca
        self.placa = placa
        self.ano = ano
        self.cor = cor
        self.velocidade = velocidade
        self.latitude = latitude
        self.longetude = longetude
    
    def acelerar(self):
        self.velocidade += 10
        nova_latitude = self.latitude + 1
        self.alterar_latitude(nova_latitude)
        print(f"O carro de placa {self.placa} foi acelerado até {self.velocidade} km/h")
    
    def frear(self):
        if self.velocidade > 0:
            self.velocidade -= 10
            print(f"O veiculo de placa {self.placa} freiou até {self.velocidade} km/h")

    def mostrar_infos(self):
        print(f"O veiculo {self.modelo}, de placa {self.placa} está a {self.velocidade} km/h")
        print(f"Lat: {self.latitude}, Long: {self.longetude}")

    def alterar_placa(self, placa):
        self.placa = placa

    def alterar_ano(self, ano):
        self.ano = ano

    def alterar_cor(self, cor):
        self.cor = cor
    
    def alterar_latitude(self, latitude):
        self.latitude = latitude

    def alterar_longetude(self, longetude):
        self.longetude = longetude
