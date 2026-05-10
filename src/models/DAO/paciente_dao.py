from src.models.DAO.base_db import BaseDB

class PacienteDAO:

    def __init__(self):
        self.__conn=BaseDB("paciente.json")

    def add_paciente(self,data:dict):
        try:
            self.__conn.save(data)
            return "Paciente adicionado com sucesso!"
        except Exception:
            raise ValueError("Não foi possível salvar o paciente")

    def ler_paciente(self):
        return self.__conn.read_list()

    def deletar_paciente(self, id_paciente):
        nova_lista=[paciente for paciente in self.ler_paciente() if paciente["id"] != id_paciente]
        if len(nova_lista)==len(self.ler_paciente()):
            raise ValueError("Nenhum paciente encontrado com esse ID")
        self.__conn.save_list(nova_lista)
        print("Deletado com Sucesso!")

    def buscar_por_ID(self,id):
        try:
            paciente_encontrado=[paciente for paciente in self.ler_paciente() if paciente["id"] == id][0]
            return paciente_encontrado
        except IndexError as e:
            raise ValueError("Paciente não existe no Sistema",e)