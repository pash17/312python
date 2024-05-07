

class Celular:
    
    def __init__(self, marca:str, modelo:str, qtde_cameras:int, armazenamento:int, preco:float) -> None:
        self.marca = marca
        self.modelo = modelo
        self.qtde_cameras = qtde_cameras
        self.armazenamento = armazenamento
        self.preco = preco


celular1 = Celular(marca="Samsung", modelo="S23 Ultra", qtde_cameras=6, armazenamento=512, preco=6500)
celular2 = Celular(marca="Apple", modelo="Iphone 14 ProMax", qtde_cameras=5, armazenamento=256, preco=8200)
celular3 = Celular(marca="Motorola", modelo="MOTO E", qtde_cameras=2, armazenamento=32, preco=347)


print(f"""
      Marca: {celular1.marca} 
      Modelo: {celular1.modelo}
""")
print(f"""
      Modelo: {celular2.modelo}
      Quantidade de Câmeras: {celular2.qtde_cameras}Gb
      Preço: R${celular2.preco}
""")
print(f"""
      Marca: {celular3.marca} 
      Modelo: {celular3.modelo}
      Armazenamento: {celular3.armazenamento}Gb
      Quantidade de Câmeras: {celular3.qtde_cameras}
      Preço: R${celular3.preco} 
""")




