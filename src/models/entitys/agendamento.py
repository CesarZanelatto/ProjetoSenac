
class Agendamento:

    def __init__(self,id:int,id_paciente:int,data:str,horario:str,procedimento:str,status:str):
        self.id=id
        self.id_paciente=id_paciente
        self.data=data
        self.horario=horario
        self.procedimento=procedimento
        self.status=status

    def to_dict(self):
        return {
            "id": self.id,
            "id_paciente":self.id_paciente,
            "data": self.data,
            "horario": self.horario,
            "procedimento": self.procedimento,
            "status": self.status
        }

    @staticmethod
    def dict_to_object(data):
        return Agendamento(
            data["id"],
            data["id_paciente"],
            data["data"],
            data["horario"],
            data["procedimento"],
            data["status"]
        )