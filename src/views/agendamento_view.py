import calendar
from datetime import datetime
from flet import (
    View, Container, Text, Alignment, Row, MainAxisAlignment,
    Button, Icons, DataTable, DataColumn, DataRow, DataCell,
    Column, FontWeight, Divider, IconButton, TextAlign,
    BoxShadow, ResponsiveRow, ScrollMode, Border,
    TextField, ElevatedButton, Dropdown, SnackBar
)
from flet.controls.material import dropdown
from src.infrastructure.services.gerador_id import Gerador_ID
from src.models.DAO.agendamento_dao import AgendamentoDAO
from src.models.DAO.paciente_dao import PacienteDAO


class AgendamentoView(View):

    def __init__(self):
        super().__init__()

        self.route = "/agendamentos"
        self.agendamento_dao = AgendamentoDAO()
        self.dia_selecionado = 5
        self.mes_atual = 5
        self.ano_atual = 2026

        self.dias_mes = calendar.monthcalendar(
            self.ano_atual,
            self.mes_atual
        )

        self.data_atual = datetime.now()
        self.input_horario = TextField(
            label="Horário",
            hint_text="08:30",
            width=120
        )
        self.input_paciente = Dropdown(
            label="Paciente",
            expand=True,
            options=[
                dropdown.Option(paciente["nome"])
                for paciente in PacienteDAO().ler_paciente()
            ]
        )
        self.input_procedimento = TextField(
            label="Procedimento",
            expand=True
        )
        self.btn_add_agendamento = ElevatedButton(
            "Agendar",
            icon=Icons.ADD,
            bgcolor="#569AA5",
            color="white",
            on_click=self.add_agendamento
        )
        self.texto_consultas_dia = Text(
            f"Consultas do Dia {self.dia_selecionado}",
            size=22,
            weight=FontWeight.BOLD,
            expand=True
        )
        self.btn_novo_agendamento = Button(
            "Novo Agendamento",
            icon=Icons.ADD,
            col=3,
            bgcolor="#569AA5",
            color="white"
        )

        self.tabela_agendamentos = DataTable(
            columns=[
                DataColumn(label=Text("Horário")),
                DataColumn(label=Text("Paciente")),
                DataColumn(label=Text("Procedimento")),
                DataColumn(label=Text("Status")),
                DataColumn(label=Text("Ações"))
            ],
            rows=self.build_rows_agendamentos()
        )
    def build_rows_agendamentos(self):
        return [
            DataRow(
                cells=[
                    DataCell(Text(agendamento["horário"])),
                    DataCell(Text(agendamento["paciente"])),
                    DataCell(Text(agendamento.get("procedimento", "N/A"))),
                    DataCell(Text(agendamento.get("status", "N/A"))),
                    DataCell(
                        IconButton(
                            icon=Icons.DELETE,
                            icon_color="red",
                            data=agendamento,
                            on_click=self.deletar_agendamento
                        )
                    )
                ]
            )
            for agendamento in self.filtrar_agendamentos()
        ]

    def add_agendamento(self):
        if (
                not self.input_horario.value
                or not self.input_paciente.value
                or not self.input_procedimento.value
        ):
            self.page.snack_bar = SnackBar(
                Text("Preencha todos os campos!")
            )
            self.page.snack_bar.open = True
            self.page.update()
            return

        horario = self.input_horario.value
        if len(horario) != 5or horario[2] != ":":
            self.page.snack_bar = SnackBar(
                Text("Horário inválido!")
            )
            self.page.snack_bar.open = True
            self.page.update()
            return

        hora = horario[:2]
        minuto = horario[3:]
        if not hora.isdigit() or not minuto.isdigit():
            self.page.snack_bar = SnackBar(
                Text("Horário inválido!")
            )
            self.page.snack_bar.open = True
            self.page.update()
            return

        hora = int(hora)
        minuto = int(minuto)
        if hora > 23 or minuto > 59:
            self.page.snack_bar = SnackBar(
                Text("Horário inválido!")
            )
            self.page.snack_bar.open = True
            self.page.update()
            return
        novo_agendamento = {
            "id": Gerador_ID("agendamento.json", "id").id_gerado,
            "dia": self.dia_selecionado,
            "horário": self.input_horario.value,
            "paciente": self.input_paciente.value,
            "procedimento": self.input_procedimento.value,
            "status": "Pendente"
        }
        self.agendamento_dao.add_agendamento(novo_agendamento)
        self.tabela_agendamentos.rows = self.build_rows_agendamentos()
        self.input_horario.value = ""
        self.input_paciente.value = ""
        self.input_procedimento.value = ""
        self.update()
        self.page.snack_bar = SnackBar(
            Text("Agendamento criado com sucesso!")
        )
        self.page.snack_bar.open = True
        self.page.update()

    def build_calendario_container(self):
        return Container(
            content=Column(
                controls=[
                    Text("Calendário", size=20, weight=FontWeight.BOLD),
                    Divider(),
                    Row(
                        controls=[
                            IconButton(Icons.ARROW_BACK, on_click=self.mes_anterior),
                            Text(
                                f"{self.nome_mes()} {self.ano_atual}",
                                expand=True,
                                text_align=TextAlign.CENTER,
                                weight=FontWeight.BOLD,
                            ),
                            IconButton(Icons.ARROW_FORWARD, on_click=self.proximo_mes)
                        ]
                    ),
                    Row(
                        controls=[
                            Container(content=Text("SEG", size=10), width=30, alignment=Alignment.CENTER),
                            Container(content=Text("TER", size=10), width=30, alignment=Alignment.CENTER),
                            Container(content=Text("QUA", size=10), width=30, alignment=Alignment.CENTER),
                            Container(content=Text("QUI", size=10), width=30, alignment=Alignment.CENTER),
                            Container(content=Text("SEX", size=10), width=30, alignment=Alignment.CENTER),
                            Container(content=Text("SAB", size=10), width=30, alignment=Alignment.CENTER),
                            Container(content=Text("DOM", size=10), width=30, alignment=Alignment.CENTER)
                        ]
                    ),
                    *self.build_calendario()
                ]
            ),
            bgcolor="#ffffff",
            border_radius=15,
            padding=20,
            border=Border.all(1, "#e5e7eb"),
            shadow=BoxShadow(blur_radius=5, spread_radius=1, color="#d6d6d6")
        )

    def build_calendario(self):
        linhas_calendario = []
        for semana in self.dias_mes:
            linha_semana = []
            for dia in semana:
                dia_atual = (
                    dia == self.data_atual.day and
                    self.mes_atual == self.data_atual.month and
                    self.ano_atual == self.data_atual.year
                )
                linha_semana.append(
                    Container(
                        content=Text("" if dia == 0 else str(dia),
                                     color="white" if dia == self.dia_selecionado else "black"),
                        width=30,
                        height=30,
                        alignment=Alignment.CENTER,
                        border_radius=15,
                        data=dia,
                        on_click=None if dia == 0 else self.selecionar_dia,
                        bgcolor="transparent" if dia == 0 else "#569AA5" if dia == self.dia_selecionado else "#E6F4F5",
                        border=Border.all(2, "#569AA5") if dia_atual else None
                    )
                )
            linhas_calendario.append(Row(controls=linha_semana, alignment=MainAxisAlignment.SPACE_BETWEEN))
        return linhas_calendario

    def nome_mes(self):
        meses = ["", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
                 "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        return meses[self.mes_atual]

    def filtrar_agendamentos(self):
        return [
            agendamento
            for agendamento in self.agendamento_dao.ler_agendamento()
            if agendamento["dia"] == self.dia_selecionado
        ]

    def selecionar_dia(self, e):
        self.dia_selecionado = e.control.data
        self.texto_consultas_dia.value = f"Consultas do Dia {self.dia_selecionado}"
        self.tabela_agendamentos.rows = self.build_rows_agendamentos()
        self.controls[0].content.controls[1].controls[0].content = self.build_calendario_container()
        self.update()

    def proximo_mes(self):
        if self.mes_atual < 12:
            self.mes_atual += 1
        else:
            self.mes_atual = 1
            self.ano_atual += 1
        self.dias_mes = calendar.monthcalendar(self.ano_atual, self.mes_atual)
        self.controls[0].content.controls[1].controls[0].content = self.build_calendario_container()
        self.update()

    def mes_anterior(self):
        if self.mes_atual > 1:
            self.mes_atual -= 1
        else:
            self.mes_atual = 12
            self.ano_atual -= 1
        self.dias_mes = calendar.monthcalendar(self.ano_atual, self.mes_atual)
        self.controls[0].content.controls[1].controls[0].content = self.build_calendario_container()
        self.update()

    def deletar_agendamento(self, e):
        agendamento = e.control.data
        self.agendamento_dao.deletar_agendamento(agendamento["id"])
        self.tabela_agendamentos.rows = self.build_rows_agendamentos()
        self.update()

    def build(self):
        linha_topo = ResponsiveRow(
            controls=[
                Text(
                    "Agendamentos",
                    size=28,
                    weight=FontWeight.BOLD,
                    col=9
                ),
                self.btn_novo_agendamento
            ],
            alignment=MainAxisAlignment.SPACE_BETWEEN
        )
        area_principal = ResponsiveRow(
            controls=[
                Container(
                    content=self.build_calendario_container(),
                    col=3,
                    padding=10
                ),
                Container(
                    content=Column(
                        controls=[
                            Row(
                                controls=[
                                    self.texto_consultas_dia,
                                    Container(
                                        content=Text(
                                            "02 Consultas",
                                            color="#569AA5",
                                            weight=FontWeight.BOLD
                                        ),
                                        bgcolor="#E6F4F5",
                                        padding=10,
                                        border_radius=10
                                    )
                                ]
                            ),
                            Row(
                                controls=[
                                    self.input_horario,
                                    self.input_paciente,
                                    self.input_procedimento,
                                    self.btn_add_agendamento
                                ]
                            ),
                            Divider(),
                            Row(
                                scroll=ScrollMode.AUTO,
                                controls=[
                                    self.tabela_agendamentos
                                ]
                            )
                        ],
                    ),
                    col=9,
                    padding=20,
                    bgcolor="#FFFFFF",
                    border_radius=15,
                    border=Border.all(1, "#e5e7eb"),
                    shadow=BoxShadow(
                        blur_radius=5,
                        spread_radius=1,
                        color="#d6d6d6"
                    )
                )
            ],
            alignment=MainAxisAlignment.SPACE_BETWEEN
        )
        self.controls = [
            Container(
                content=Column(
                    controls=[
                        linha_topo,
                        area_principal
                    ]
                ),
                padding=20
            )
        ]
        return self.controls