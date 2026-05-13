from flet import *

from src.models.entitys.agendamento import Agendamento
from src.models.DAO.agendamento_dao import AgendamentoDAO
from src.models.DAO.paciente_dao import PacienteDAO
from src.infrastructure.services.gerador_id import Gerador_ID
from src.views.agendamento_view import AgendamentoView


class AgendamentoController:

    def __init__(self, page, tela: AgendamentoView):

        self.dao = AgendamentoDAO()
        self.paciente_dao = PacienteDAO()
        self.page = page
        self.tela = tela

        # REFERÊNCIA DO CONTROLLER NA VIEW
        self.tela.controller = self

        # =========================
        # EVENTOS
        # =========================
        self.tela.btn_add_agendamento.on_click=self.handle_add_agendamento

        self.listar_agendamentos()

    # ==================================================
    # LISTAR AGENDAMENTOS
    # ==================================================
    def listar_agendamentos(self):
        self.tela.tabela_agendamentos.rows.clear()
        for agendamento in self.tela.filtrar_agendamentos():
            linha = DataRow(
                cells=[
                    DataCell(
                        Text(
                            str(
                                agendamento.get(
                                    "horario",
                                    "N/A"
                                )
                            )
                        )
                    ),
                    DataCell(
                        Text(
                            str(
                                agendamento.get(
                                    "paciente",
                                    "N/A"
                                )
                            )
                        )
                    ),
                    DataCell(
                        Text(
                            str(
                                agendamento.get(
                                    "procedimento",
                                    "N/A"
                                )
                            )
                        )
                    ),
                    DataCell(
                        Text(
                            str(
                                agendamento.get(
                                    "status",
                                    "N/A"
                                )
                            )
                        )
                    ),
                    DataCell(
                        IconButton(
                            icon=Icons.DELETE,
                            icon_color="red",
                            data=agendamento.get("id"),
                            on_click=lambda e,
                            id_agendamento=agendamento.get("id"):
                            self.handle_delete_agendamento(
                                id_agendamento
                            )
                        )
                    )
                ]
            )
            self.tela.tabela_agendamentos.rows.append(linha)
        self.page.update()

    # ==================================================
    # BUSCAR AGENDAMENTO
    # ==================================================
    def buscar_agendamento_id(self, id: int):
        try:
            return self.dao.buscar_por_ID(id)
        except Exception as e:
            print(e)
            return None

    # ==================================================
    # ADICIONAR AGENDAMENTO
    # ==================================================
    def handle_add_agendamento(self):

        try:
            paciente_nome=self.tela.input_paciente.value
            pacientes = [p for p in self.paciente_dao.ler_paciente() if p["nome"] == paciente_nome]
            if not pacientes:
                print("Paciente não encontrado")
                return
            paciente = pacientes[0]

            agendamento = Agendamento(
                Gerador_ID("agendamento.json", "id").id_gerado,
                paciente["id"],
                f"{self.tela.dia_selecionado}/"
                f"{self.tela.mes_atual}/"
                f"{self.tela.ano_atual}",
                self.tela.input_horario.value,
                self.tela.input_procedimento.value,
                self.tela.input_status.value
            )

            novo_agendamento = agendamento.to_dict()

            novo_agendamento["paciente"]=(paciente["nome"])

            novo_agendamento["dia"]=self.tela.dia_selecionado

            self.dao.add_agendamento(novo_agendamento)

            # LIMPAR CAMPOS
            self.tela.input_horario.value = ""
            self.tela.input_paciente.value = None
            self.tela.input_procedimento.value = ""
            self.tela.input_status.value = "Pendente"

            self.tela.input_horario.update()
            self.tela.input_paciente.update()
            self.tela.input_procedimento.update()

            self.listar_agendamentos()
        except Exception as e:
            print(e)

    # ==================================================
    # DELETAR AGENDAMENTO
    # ==================================================
    def handle_delete_agendamento(self,id_agendamento:int):
        try:
            self.dao.deletar_agendamento(id_agendamento)
            self.listar_agendamentos()
        except Exception as e:
            print(e)