
class Paciente:

    def __init__(self,id:int,nome:str,telefone:str,data_nascimento:str):
        self.__id=id
        self.__nome=nome
        self.__telefone=telefone
        self.__data_nascimento=data_nascimento

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    def to_dict(self):
        return {
            "id": self.__id,
            "nome": self.__nome,
            "telefone": self.__telefone,
            "data_nascimento": self.__data_nascimento
        }

    @staticmethod
    def dict_to_object(data):
        return Paciente(
            data["id"],
            data["nome"],
            data["telefone"],
            data["data_nascimento"]
        )