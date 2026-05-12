from flet import *

from src.models.entitys.agendamento import Agendamento
from src.models.DAO.agendamento_dao import AgendamentoDAO
from src.infrastructure.services.gerador_id import Gerador_ID
from src.views.agendamento_view import AgendamentoView


class AgendamentoController:

    def __init__(self, page, tela: AgendamentoView):
        self.dao = AgendamentoDAO()
        self.page = page
        self.tela = tela
        self.tela.btn_add_agendamento.on_click = self.handle_add_agendamento
        self.listar_agendamentos()

    def listar_agendamentos(self):

        self.tela.tabela_agendamentos.rows.clear()

        for agendamento in self.tela.filtrar_agendamentos():

            linha = DataRow(
                cells=[
                    DataCell(Text(agendamento["horário"])),
                    DataCell(Text(agendamento["paciente"])),
                    DataCell(
                        Text(
                            agendamento.get(
                                "procedimento",
                                "N/A"
                            )
                        )
                    ),
                    DataCell(
                        Text(
                            agendamento.get(
                                "status",
                                "N/A"
                            )
                        )
                    ),
                    DataCell(
                        IconButton(
                            icon=Icons.DELETE,
                            icon_color="red",
                            data=agendamento["id"],
                            on_click=self.handle_delete_agendamento
                        )
                    )
                ]
            )
            self.tela.tabela_agendamentos.rows.append(linha)
        self.page.update()

    def handle_add_agendamento(self, e):
        a = Agendamento(Gerador_ID("agendamento.json","id").id_gerado,
            self.tela.input_paciente.value,
            str(self.tela.dia_selecionado),
            self.tela.input_horario.value,
            self.tela.input_procedimento.value,
            "Pendente"
        )
        try:
            novo_agendamento = {
                "id": a.id,
                "dia": self.tela.dia_selecionado,
                "horário": a.horario,
                "paciente": a.id_paciente,
                "procedimento": a.procedimento,
                "status": a.status
            }
            self.dao.add_agendamento(
                novo_agendamento
            )
            self.tela.input_horario.value = ""
            self.tela.input_paciente.value = ""
            self.tela.input_procedimento.value = ""
            self.tela.input_horario.update()
            self.tela.input_paciente.update()
            self.tela.input_procedimento.update()
            self.listar_agendamentos()
        except Exception as e:
            print(e)

    def handle_delete_agendamento(self, e):
        id_agendamento = e.control.data
        try:
            self.dao.deletar_agendamento(id_agendamento)
            self.listar_agendamentos()
        except Exception as e:
            print(e)