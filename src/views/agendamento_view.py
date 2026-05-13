import calendar
from datetime import datetime

from flet import (
    View, Container, Text, Alignment, Row, MainAxisAlignment,
    Button, Icons, DataTable, DataColumn,
    Column, FontWeight, Divider, IconButton, TextAlign,
    BoxShadow, ResponsiveRow, ScrollMode, Border,
    TextField, ElevatedButton, Dropdown, Icon, CrossAxisAlignment
)

from flet.controls.material import dropdown
from src.models.DAO.agendamento_dao import AgendamentoDAO
from src.models.DAO.paciente_dao import PacienteDAO


class AgendamentoView(View):

    def __init__(self,page):
        super().__init__()
        self.pagina=page
        self.route = "/agendamentos"
        self.controller = None
        self.agendamento_dao = AgendamentoDAO()

        self.dia_selecionado = 5
        self.mes_atual = 5
        self.ano_atual = 2026

        self.dias_mes = calendar.monthcalendar(
            self.ano_atual,
            self.mes_atual
        )
        self.data_atual = datetime.now()
        # =========================
        # CONFIG BOTÕES SIDEBAR
        # =========================
        config_btn=12
        # =========================
        # SIDEBAR
        # =========================
        btn_dashboard = Button(
            "Dashboard",
            icon=Icons.DASHBOARD,
            col=config_btn,
            color="Black",
            bgcolor="#FFFFFF",
            height=55,
            width=212,
        )
        btn_pacientes = Button(
            "Pacientes",
            icon=Icons.PEOPLE,
            col=config_btn,
            color="Black",
            bgcolor="#FFFFFF",
            height=55,
            width=212,
        )
        btn_agendamentos = Button(
            "Agendamentos",
            icon=Icons.CALENDAR_TODAY_OUTLINED,
            col=config_btn,
            color="Black",
            bgcolor="#D1EAEA",
            height=55,
            width=212,
        )
        btn_pacientes.on_click=(lambda e: self.pagina.go("/pacientes"))
        btn_agendamentos.on_click=(lambda e: self.pagina.go("/agendamentos"))
        btn_dashboard.on_click=(lambda e: self.pagina.go("/dashboard"))

        self.sidebar = Container(
            bgcolor="#FFFFFF",
            padding=20,
            width=250,
            shadow=BoxShadow(
                blur_radius=30,
                color="Grey"
            ),
            content=Column(
                expand=True,
                controls=[
                    Row(
                        controls=[
                            Icon(
                                Icons.LOCAL_HOSPITAL,
                                color="Black"
                            ),
                            Text(
                                "Medical Clinic",
                                color="Black",
                                size=20,
                                weight=FontWeight.BOLD
                            )
                        ]
                    ),
                    Container(height=20),
                    btn_dashboard,
                    btn_pacientes,
                    btn_agendamentos
                ]
            )
        )
        # =========================
        # CAMPOS
        # =========================
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

        self.input_status = Dropdown(
            label="Status",
            width=180,
            value="Pendente",
            options=[
                dropdown.Option("Pendente"),
                dropdown.Option("Fila de Espera"),
                dropdown.Option("Confirmado"),
                dropdown.Option("Finalizado")
            ]
        )
        self.btn_add_agendamento = ElevatedButton(
            "Agendar",
            icon=Icons.ADD,
            bgcolor="#569AA5",
            color="white",
            on_click=None
        )
        self.texto_consultas_dia = Text(
            f"Consultas do Dia {self.dia_selecionado}",
            size=22,
            weight=FontWeight.BOLD,
            expand=True
        )
        # =========================
        # CONTAINER CALENDÁRIO
        # =========================
        self.calendario_container = Container(
            content=self.build_calendario_container(),
            col=4,
            padding=10
        )
        # =========================
        # TABELA
        # =========================
        self.tabela_agendamentos = DataTable(
            columns=[
                DataColumn(label=Text("Horário")),
                DataColumn(label=Text("Paciente")),
                DataColumn(label=Text("Procedimento")),
                DataColumn(label=Text("Status")),
                DataColumn(label=Text("Ações"))
            ],
            rows=[]
        )
    # ==================================================
    # CALENDÁRIO
    # ==================================================
    def build_calendario_container(self):

        return Container(
            content=Column(
                controls=[
                    Text(
                        "Calendário",
                        size=20,
                        weight=FontWeight.BOLD
                    ),
                    Divider(),
                    Row(
                        controls=[
                            IconButton(
                                Icons.ARROW_BACK,
                                on_click=self.mes_anterior
                            ),
                            Text(
                                f"{self.nome_mes()} {self.ano_atual}",
                                expand=True,
                                text_align=TextAlign.CENTER,
                                weight=FontWeight.BOLD,
                            ),
                            IconButton(
                                Icons.ARROW_FORWARD,
                                on_click=self.proximo_mes
                            )
                        ]
                    ),
                    ResponsiveRow(
                        controls=[
                            Container(
                                content=Text("SEG", size=12),
                                width=35,
                                alignment=Alignment.CENTER,
                                col=1
                            ),
                            Container(
                                content=Text("TER", size=12),
                                width=35,
                                alignment=Alignment.CENTER,
                                col=1
                            ),
                            Container(
                                content=Text("QUA", size=12),
                                width=35,
                                alignment=Alignment.CENTER,
                                col=1
                            ),
                            Container(
                                content=Text("QUI", size=12),
                                width=35,
                                alignment=Alignment.CENTER,
                                col=1
                            ),
                            Container(
                                content=Text("SEX", size=12),
                                width=35,
                                alignment=Alignment.CENTER,
                                col=1

                            ),
                            Container(
                                content=Text("SAB", size=12),
                                width=35,
                                alignment=Alignment.CENTER,
                                col=1
                            ),
                            Container(
                                content=Text("DOM", size=12),
                                width=35,
                                alignment=Alignment.CENTER,
                                col=1
                            )
                        ], alignment=MainAxisAlignment.SPACE_AROUND
                    ),
                    *self.build_calendario()
                ]
            ),
            bgcolor="#ffffff",
            border_radius=15,
            padding=20,
            border=Border.all(1, "#e5e7eb"),
            shadow=BoxShadow(
                blur_radius=5,
                spread_radius=1,
                color="#d6d6d6"
            )
        )

    def build_calendario(self):
        linhas_calendario = []
        for semana in self.dias_mes:
            linha_semana = []
            for dia in semana:
                dia_atual = (
                        dia == self.data_atual.day
                        and self.mes_atual == self.data_atual.month
                        and self.ano_atual == self.data_atual.year
                )
                linha_semana.append(
                    Container(
                        content=Text(
                            "" if dia == 0 else str(dia),
                            color="white"
                            if dia == self.dia_selecionado
                            else "black"
                        ),
                        width=28,
                        height=28,
                        alignment=Alignment.CENTER,
                        border_radius=14,
                        data=dia,
                        on_click=None
                        if dia == 0
                        else self.selecionar_dia,

                        bgcolor="transparent"
                        if dia == 0
                        else "#569AA5"
                        if dia == self.dia_selecionado
                        else "#E6F4F5",

                        border=Border.all(2, "#569AA5")
                        if dia_atual
                        else None
                    )
                )
            linhas_calendario.append(
                Row(
                    controls=linha_semana,
                    alignment=MainAxisAlignment.SPACE_AROUND
                )
            )
        return linhas_calendario
    # ==================================================
    # AUXILIARES
    # ==================================================
    def nome_mes(self):
        meses = [
            "",
            "Janeiro",
            "Fevereiro",
            "Março",
            "Abril",
            "Maio",
            "Junho",
            "Julho",
            "Agosto",
            "Setembro",
            "Outubro",
            "Novembro",
            "Dezembro"
        ]
        return meses[self.mes_atual]

    def filtrar_agendamentos(self):
        return [agendamento for agendamento in self.agendamento_dao.ler_agendamento() if agendamento["dia"] == self.dia_selecionado]
    # ==================================================
    # EVENTOS
    # ==================================================
    def selecionar_dia(self, e):
        self.dia_selecionado = e.control.data
        self.texto_consultas_dia.value=f"Consultas do Dia {self.dia_selecionado}"
        self.calendario_container.content=(self.build_calendario_container())
        self.controller.listar_agendamentos()
        self.update()

    def proximo_mes(self):
        if self.mes_atual < 12:
            self.mes_atual += 1
        else:
            self.mes_atual = 1
            self.ano_atual += 1
        self.dias_mes=calendar.monthcalendar(self.ano_atual,self.mes_atual)
        self.calendario_container.content=(self.build_calendario_container())
        self.update()

    def mes_anterior(self):
        if self.mes_atual > 1:
            self.mes_atual -= 1
        else:
            self.mes_atual = 12
            self.ano_atual -= 1

        self.dias_mes=calendar.monthcalendar(self.ano_atual,self.mes_atual)
        self.calendario_container.content=(self.build_calendario_container())
        self.update()
    # ==================================================
    # BUILD
    # ==================================================
    def build(self):

        linha_topo = ResponsiveRow(
            controls=[
                Text(
                    "Agendamentos",
                    size=28,
                    weight=FontWeight.BOLD,
                    col=12
                )
            ]
        )
        area_principal = ResponsiveRow(
            controls=[

                # CALENDÁRIO
                self.calendario_container,

                # ÁREA DIREITA
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
                                    self.input_status,
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
                        ]
                    ),
                    col=8,
                    padding=20,
                    bgcolor="#FFFFFF",
                    border_radius=15,
                    border=Border.all(
                        1,
                        "#e5e7eb"
                    ),
                    shadow=BoxShadow(
                        blur_radius=5,
                        spread_radius=1,
                        color="#d6d6d6"
                    )
                )
            ]
        )
        # ==================================================
        # LAYOUT FINAL COM SIDEBAR
        # ==================================================
        layout = Row(
            expand=True,
            spacing=0,
            vertical_alignment=CrossAxisAlignment.STRETCH,
            controls=[
                self.sidebar,
                Container(
                    expand=True,
                    padding=20,
                    content=Column(
                        controls=[
                            linha_topo,
                            area_principal
                        ]
                    )
                )
            ]
        )
        self.controls=[layout]
        return self.controls