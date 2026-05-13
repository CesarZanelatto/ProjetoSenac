from src.models.DAO.base_db import BaseDB

class DashboardDAO:

    def __init__(self):
        self.__conn=BaseDB("dashboard.json")

    def add_dashboard(self,data:dict):
        try:
            self.__conn.save(data)
            return "Dashboard adicionado com sucesso!"
        except Exception:
            raise ValueError("Não foi possível salvar no dashboard")

    def ler_dashboard(self):
        return self.__conn.read_list()

    def deletar_dashboard(self, id_dashboard):
        nova_lista=[dashboard for dashboard in self.ler_dashboard() if dashboard["id"] != id_dashboard]
        if len(nova_lista)==len(self.ler_dashboard()):
            raise ValueError("Nenhum dashboard encontrado com esse ID")
        self.__conn.save_list(nova_lista)
        print("Deletado com Sucesso!")

    def buscar_por_ID(self,id):
        try:
            dashboard_encontrado=[dashboard for dashboard in self.ler_dashboard() if dashboard["id"] == id][0]
            return dashboard_encontrado
        except IndexError as e:
            raise ValueError("Dashboard não existe no Sistema",e)