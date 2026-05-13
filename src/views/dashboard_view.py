from flet import *

class DashboardView(View):

    def __init__(self, page):
        super().__init__()
        self.pagina = page
        self.route = "/dashboard"
        self.controller = None

        self.expand = True
        self.bgcolor = "#E6F4F5"

        config_btn = 12

        self.txt_total_pacientes = Text(
            "0",
            size=28,
            weight=FontWeight.BOLD,
            color="Black"
        )

        self.txt_total_agendamentos = Text(
            "0",
            size=28,
            weight=FontWeight.BOLD,
            color="Black"
        )

        self.txt_total_fila_espera = Text(
            "0",
            size=28,
            weight=FontWeight.BOLD,
            color="Black"
        )

        btn_dashboard = Button(
            "Dashboard",
            icon=Icons.DASHBOARD,
            col= config_btn,
            color="Black",
            bgcolor="#FFFFFF",
            height=55,
            width=212
        )

        btn_pacientes = Button(
            "Pacientes",
            icon=Icons.PEOPLE,
            col= config_btn,
            color="Black",
            bgcolor="#FFFFFF",
            height=55,
            width=212
        )

        btn_agendamentos = Button(
            "Agendamentos",
            icon=Icons.CALENDAR_TODAY_OUTLINED,
            col=config_btn,
            color="Black",
            bgcolor="#FFFFFF",
            height=55,
            width=212
        )

        btn_pacientes.on_click = (lambda e: self.pagina.go("/pacientes"))
        btn_agendamentos.on_click = (lambda e: self.pagina.go("/agendamentos"))
        btn_dashboard.on_click = (lambda e: self.pagina.go("/dashboard"))

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
                    Row([
                        Icon(Icons.LOCAL_HOSPITAL, color="Black"),
                        Text(
                            "Medical Clinic",
                            color="Black",
                            size=20,
                            weight=FontWeight.BOLD
                        )
                    ]),
                    Container(height=20),

                    btn_dashboard,
                    btn_pacientes,
                    btn_agendamentos
                ]
            )
        )

        self.input_pesquisa = TextField(
            icon=Icons.SEARCH,
            label="Pesquisar",
            label_style=TextStyle(color="Black"),
            color="Black",
            bgcolor="#E6F4F5",
            width=363,
            height=56,
            border_radius=10
        )

        self.caixa_superior = Container(
            bgcolor="#FFFFFF",
            padding=20,
            content=Row(
                controls=[
                    self.input_pesquisa
                ],
                spacing=0,
                alignment=MainAxisAlignment.SPACE_BETWEEN
            )
        )

        self.cards = Row(
            spacing=10,
            controls=[
                self.criar_card(
                    "Total de\nPacientes:",
                    self.txt_total_pacientes,
                    "#D1EAEA"
                ),

                self.criar_card(
                    "Total de\nAgendamentos:",
                    self.txt_total_agendamentos,
                    "#F2D1C2"
                ),

                self.criar_card(
                    "Total Fila de\nEspera:",
                    self.txt_total_fila_espera,
                    "#F2D1C2"
                ),
            ]
        )

        self.conteudo_meio = Container(
            bgcolor="White",
            padding=15,
            border_radius=15,
            content=self.cards
        )

        self.container_fila_espera = Column(
            spacing=10,
            scroll=ScrollMode.AUTO
        )

        self.fila_espera = Container(
            bgcolor="White",
            padding=15,
            border_radius=15,
            expand=True,
            content=Column(
                controls=[
                    Row(
                        [
                            Text(
                                "Fila de Espera",
                                color="Black",
                                weight=FontWeight.BOLD
                            ),
                            Icon(Icons.MORE_HORIZ)
                        ],
                        alignment=MainAxisAlignment.SPACE_BETWEEN
                    ),

                    self.container_fila_espera
                ]
            )
        )

        self.coluna_principal = Column(
            expand=True,
            spacing=20,
            controls=[
                Text(
                    "Dashboard",
                    size=28,
                    color="Black",
                    weight=FontWeight.BOLD
                ),

                self.conteudo_meio,
                self.fila_espera
            ]
        )

        self.conteudo_direita = Column(
            expand=True,
            spacing=20,
            controls=[
                self.caixa_superior,

                Container(
                    padding=15,
                    content=self.coluna_principal
                )
            ]
        )

        self.controls = [
            Row(
                expand=True,
                spacing=0,
                controls=[
                    self.sidebar,
                    self.conteudo_direita
                ]
            )
        ]



    def criar_card(self, texto, valor, cor):

        return Container(
            content=Column(
                [
                    Text(
                        texto,
                        color="Black",
                        size=12
                    ),

                    valor
                ]
            ),

            bgcolor=cor,
            padding=15,
            border_radius=10,
            width=180,
            height=120,
        )

    def criar_card_fila_espera(self, agendamento):

        nome = agendamento.get("nome", "Paciente")

        return Container(
            bgcolor="#E6F4F5",
            padding=10,
            border_radius=10,

            content=Row(
                [
                    Icon(Icons.PERSON),

                    Text(
                        nome,
                        color="Black",
                        size=11
                    )
                ]
            )
        )