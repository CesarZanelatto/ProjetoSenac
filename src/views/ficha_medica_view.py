from flet import (
    View, Container, Text, Row, MainAxisAlignment,
    Button, Icons, Column, FontWeight, Divider,
    IconButton, BoxShadow, ResponsiveRow,
    ScrollMode, Border, ResponsiveRowBreakpoint,
    Icon, CrossAxisAlignment
)

from src.models.DAO.paciente_dao import PacienteDAO


class FichaMedicaView(View):

    def __init__(self):
        super().__init__()

        self.route = "/pacientes"

        self.paciente_dao = PacienteDAO()

        self.lista_pacientes = (
            self.paciente_dao.ler_paciente()
        )

        # ==================================================
        # CONFIG BOTÕES SIDEBAR
        # ==================================================
        self.configBtn = {
            ResponsiveRowBreakpoint.XS: 10,
            ResponsiveRowBreakpoint.SM: 6,
            ResponsiveRowBreakpoint.LG: 3
        }

        # ==================================================
        # SIDEBAR
        # ==================================================
        self.btn_dashboard = Button(
            "Dashboard",
            icon=Icons.DASHBOARD,
            col=self.configBtn,
            color="Black",
            bgcolor="#FFFFFF",
            height=55,
            width=212,
        )

        self.btn_pacientes = Button(
            "Pacientes",
            icon=Icons.PEOPLE,
            col=self.configBtn,
            color="Black",
            bgcolor="#D1EAEA",
            height=55,
            width=212,
        )

        self.btn_agendamentos = Button(
            "Agendamentos",
            icon=Icons.CALENDAR_TODAY_OUTLINED,
            col=self.configBtn,
            color="Black",
            bgcolor="#FFFFFF",
            height=55,
            width=212,
        )

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

                    self.btn_dashboard,
                    self.btn_pacientes,
                    self.btn_agendamentos
                ]
            )
        )

        # ==================================================
        # LISTA DE CARDS
        # ==================================================
        self.lista_cards = Column(
            scroll=ScrollMode.AUTO,

            controls=[

                self.mostrar_card_paciente(paciente)

                for paciente in self.lista_pacientes
            ]
        )

    # ==================================================
    # CARD PACIENTE
    # ==================================================
    def mostrar_card_paciente(self, paciente: dict):

        return Container(
            margin={"bottom": 15},
            padding=15,
            border_radius=12,
            bgcolor="#F9FAFB",
            border=Border.all(1, "#E5E7EB"),

            content=Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,

                controls=[

                    Column(
                        spacing=5,

                        controls=[

                            Text(
                                paciente["nome"],
                                size=18,
                                weight=FontWeight.BOLD
                            ),

                            Text(
                                f"ID: {paciente['id']}"
                            ),

                            Text(
                                f"Telefone: "
                                f"{paciente['telefone']}"
                            ),

                            Text(
                                f"Nascimento: "
                                f"{paciente['data_nascimento']}"
                            )
                        ]
                    ),

                    Row(
                        controls=[

                            Icon(
                                Icons.PERSON,
                                size=40,
                                color="#569AA5"
                            ),

                            IconButton(
                                icon=Icons.DELETE,
                                icon_color="red",

                                on_click=lambda e:
                                self.deletar_paciente(
                                    paciente["id"]
                                )
                            )
                        ]
                    ),
                ]
            )
        )

    # ==================================================
    # DELETAR PACIENTE
    # ==================================================
    def deletar_paciente(self, id_paciente):

        self.paciente_dao.deletar_paciente(
            id_paciente
        )

        self.lista_pacientes = (
            self.paciente_dao.ler_paciente()
        )

        self.renderizar_pacientes()

    # ==================================================
    # RENDERIZAR PACIENTES
    # ==================================================
    def renderizar_pacientes(self):

        self.lista_cards.controls = [

            self.mostrar_card_paciente(paciente)

            for paciente in self.lista_pacientes
        ]

        self.update()

    # ==================================================
    # BUILD
    # ==================================================
    def build(self):

        linha_topo = ResponsiveRow(
            controls=[
                Text(
                    "Ficha Médica",
                    size=28,
                    weight=FontWeight.BOLD,
                    col=12
                )
            ]
        )

        area_principal = ResponsiveRow(
            controls=[

                Container(
                    col=12,
                    padding=20,
                    bgcolor="#FFFFFF",
                    border_radius=15,
                    border=Border.all(
                        1,
                        "#E5E7EB"
                    ),

                    shadow=BoxShadow(
                        blur_radius=5,
                        spread_radius=1,
                        color="#D6D6D6"
                    ),

                    content=Column(
                        controls=[

                            Row(
                                controls=[

                                    Text(
                                        "Pacientes Cadastrados",
                                        size=22,
                                        weight=FontWeight.BOLD
                                    ),

                                    Container(
                                        content=Text(
                                            f"{len(self.lista_pacientes)} Pacientes",
                                            color="#569AA5",
                                            weight=FontWeight.BOLD
                                        ),

                                        bgcolor="#E6F4F5",
                                        padding=10,
                                        border_radius=10
                                    )
                                ],

                                alignment=MainAxisAlignment.SPACE_BETWEEN
                            ),

                            Divider(),

                            self.lista_cards
                        ]
                    )
                )
            ]
        )

        # ==================================================
        # LAYOUT FINAL
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

        self.controls = [layout]

        return self.controls