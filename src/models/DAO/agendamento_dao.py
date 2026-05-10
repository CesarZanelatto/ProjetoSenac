from src.models.DAO.base_db import BaseDB

class AgendamentoDAO:

    def __init__(self):
        self.__conn=BaseDB("agendamento.json")

    def add_agendamento(self,data:dict):
        try:
            self.__conn.save(data)
            return "Paciente adicionado com sucesso!"
        except Exception:
            raise ValueError("Não foi possível salvar o agendamento")

    def ler_agendamento(self):
        return self.__conn.read_list()

    def deletar_agendamento(self, id_agendamento):
        nova_lista=[agendamento for agendamento in self.ler_agendamento() if agendamento["id"] != id_agendamento]
        if len(nova_lista)==len(self.ler_agendamento()):
            raise ValueError("Nenhum agendamento encontrado com esse ID")
        self.__conn.save_list(nova_lista)
        print("Deletado com Sucesso!")

    def buscar_por_ID(self,id):
        try:
            agendamento_encontrado=[agendamento for agendamento in self.ler_agendamento() if agendamento["id"] == id][0]
            return agendamento_encontrado
        except IndexError as e:
            raise ValueError("Paciente não existe no Sistema",e)