
class Paciente:

    def __init__(self,id:int,nome:str,data_nascimento:str,telefone:str):
        self.id=id
        self.nome=nome
        self.data_nascimento=data_nascimento
        self.telefone=telefone

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "telefone": self.telefone,
            "data_nascimento": self.data_nascimento
        }

    @staticmethod
    def dict_to_object(data):
        return Paciente(
            data["id"],
            data["nome"],
            data["telefone"],
            data["data_nascimento"]
        )