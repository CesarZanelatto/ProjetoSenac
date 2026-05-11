import json
from json import JSONDecodeError

class Gerador_ID:

    def __init__(self,path_file,atributo):
        self.path_file=fr"C:\Users\cesar.ozanelatto\PycharmProjects\ProjetoSenac\src\infrastructure\database\{path_file}"
        self.id_gerado=None
        try:
            with open(self.path_file,"r",encoding="utf-8") as file:
                lista=json.load(file)
                if not lista:
                    self.id_gerado=1
                else:
                    listas_ids = (data[atributo] for data in lista)
                    self.id_gerado = max(listas_ids)+1
        except JSONDecodeError:
            self.id_gerado=1
        except FileNotFoundError:
            self.id_gerado=1

if __name__ == '__main__':
    id_novo=Gerador_ID("produtos.json","id").id_gerado
    print(id_novo)