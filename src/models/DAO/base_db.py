import json
from json import JSONDecodeError
from  src.infrastructure.services.path_db import PathDB


class BaseDB:

    def __init__(self,file_db:str):
        
        
        self.__path=fr"{PathDB().path}\{file_db}"
        print("testando",self.__path)
        self.__file_db=file_db

    def read_list(self)-> list:
        try:
            with open(self.__path,"r+",encoding="utf-8") as file:
                return json.load(file)
        except JSONDecodeError:
            return []
        except:
            raise ValueError("Erro ao abrir o arquivo:", self.__file_db)

    def save(self,data):
        list_data_base=self.read_list()
        try:
            with open(self.__path,"w",encoding="utf-8") as file:
                list_data_base.append(data)
                json.dump(list_data_base,file,ensure_ascii=False,indent=4)
                print("Salvo com sucesso no banco de dados!")
        except:
            raise ValueError("Erro ao salvar no arquivo:",self.__file_db)

    def save_list(self,lista):
        try:
            with open(self.__path,"w",encoding="utf-8") as file:
                json.dump(lista,file,ensure_ascii=False,indent=4)
                print("Salvo com sucesso no banco de dados!")
        except:
            raise ValueError("Erro ao salvar a lista do paciente deletado:",self.__file_db)
        


if __name__=="__main__":
    testes=BaseDB("paciente.json")