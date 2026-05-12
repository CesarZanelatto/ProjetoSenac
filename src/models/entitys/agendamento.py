
class Agendamento:

    def __init__(self,id:int,id_paciente:int,data:str,horario:str,procedimento:str,status:str):
        self.__id=id
        self.__id_paciente=id_paciente
        self.__data=data
        self.__horario=horario
        self.__procedimento=procedimento
        self.__status=status

    @property
    def id(self):
        return self.__id

    @property
    def id_paciente(self):
        return self.__id_paciente

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def horario(self):
        return self.__horario

    @horario.setter
    def horario(self, horario):
        self.__horario = horario

    @property
    def procedimento(self):
        return self.__procedimento

    @procedimento.setter
    def procedimento(self, procedimento):
        self.__status = procedimento

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    def to_dict(self):
        return {
            "id": self.__id,
            "id_paciente":self.__id_paciente,
            "data": self.__data,
            "horario": self.__horario,
            "procedimento": self.__procedimento,
            "status": self.__status
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