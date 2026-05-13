from src.models.DAO.paciente_dao import PacienteDAO
from src.models.DAO.agendamento_dao import AgendamentoDAO
from src.views.dashboard_view import DashboardView

class DashboardController:

    def __init__(self, page, tela: DashboardView):
        self.page = page
        self.tela = tela

        self.paciente_dao = PacienteDAO()
        self.agendamento_dao = AgendamentoDAO()

        self.carregar_dashboard()

    def carregar_dashboard(self):
        self.carregar_totais()
        self.carregar_fila_espera()

    def carregar_totais(self):
        try:
            pacientes = self.paciente_dao.ler_paciente()
            agendamentos = self.agendamento_dao.ler_agendamento()

            total_pacientes = len(pacientes)
            total_agendamentos = len(agendamentos)

            fila_espera = [
                agendamento
                for agendamento in agendamentos
                if agendamento["status"] == "Fila de Espera"
            ]

            total_fila_espera = len(fila_espera)

            self.tela.txt_total_pacientes.value = str(total_pacientes)
            self.tela.txt_total_agendamentos.value = str(total_agendamentos)
            self.tela.txt_total_fila_espera.value = str(total_fila_espera)

            self.tela.txt_total_pacientes.update()
            self.tela.txt_total_agendamentos.update()
            self.tela.txt_total_fila_espera.update()

        except Exception as e:
            print(e)

    def carregar_fila_espera(self):
        try:
            agendamentos = self.agendamento_dao.ler_agendamento()

            fila = [
                agendamento
                for agendamento in agendamentos
                if agendamento["status"] == "Fila de Espera"
            ]

            lista_fila = []

            for agendamento in fila:
                card = self.tela.criar_card_fila_espera(agendamento)
                lista_fila.append(card)

            self.tela.container_fila_espera.controls = lista_fila
            self.tela.container_fila_espera.update()

        except Exception as e:
            print(e)

    def atualizar_dashboard(self):
        self.carregar_dashboard()