from flet import *
from src.models.DAO.paciente_dao import PacienteDAO
from src.infrastructure.services.gerador_id import Gerador_ID

class PacienteView(View):

    def __init__(self):
        super().__init__()
        self.route="/pacientes"
        self.paciente_dao=PacienteDAO()
        self.lista_pacientes=self.paciente_dao.ler_paciente()
        self.bgcolor="#E6F4F5"
        self.spacing=0
        self.padding=0
        self.input_nome=TextField(
            label="Nome",
            expand=True
        )
        self.input_telefone=TextField(
            label="Telefone",
            expand=True
        )
        self.input_data_nascimento=TextField(
            label="Data de nascimento",
            hint_text="dd/mm/aaaa",
            expand=True
        )
        self.btn_cadastrar=Button(
            "Cadastrar Paciente",
            icon=Icons.ADD,
            bgcolor="#569AA5",
            color="white",
            on_click=self.cadastrar_paciente
        )

        config_btn = 12

        btn1 = Button(
            "Dashboard",
            icon=Icons.DASHBOARD,
            col=config_btn,
            color="Black",
            bgcolor="#FFFFFF",
            height=55,
            width=212
        )

        btn2 = Button(
            "Pacientes",
            icon=Icons.PEOPLE,
            col=config_btn,
            color="Black",
            bgcolor="#FFFFFF",
            height=55,
            width=212
        )

        btn3 = Button(
            "Agendamentos",
            icon=Icons.CALENDAR_TODAY_OUTLINED,
            col=config_btn,
            color="Black",
            bgcolor="#FFFFFF",
            height=55,
            width=212
        )

        sidebar = Container(
            bgcolor="#FFFFFF",
            padding=20,
            width=250,
            shadow=BoxShadow(blur_radius=30, color="Grey"),
            content=Column(
                expand=True,
                controls=[
                    Row([
                        Icon(Icons.LOCAL_HOSPITAL, color="Black"),
                        Text("Medical Clinic",
                             color="Black",
                             size=20,
                             weight=FontWeight.BOLD)
                    ]),
                    Container(height=20),
                    btn1,
                    btn2,
                    btn3
                ]
            )
        )

        self.controls = [
            Row(
                expand=True,
                spacing=0,
                controls=[
                    sidebar,
                    Container(
                        expand=True,
                        padding=20,
                        content=Column(
                            controls=[
                                Text("Pacientes Cadastrados", size=28, weight=FontWeight.BOLD),
                                Row(
                                    controls=[
                                        self.input_nome,
                                        self.input_telefone,
                                        self.input_data_nascimento,
                                        self.btn_cadastrar
                                    ]
                                ),
                                Divider(),
                                Container(
                                    expand=True,
                                    bgcolor="#FFFFFF",
                                    border_radius=15,
                                    padding=20,
                                    border=Border.all(1, "#E5E7EB"),
                                    content=Column(
                                        scroll=ScrollMode.AUTO,
                                        controls=[
                                            self.criar_card_paciente(paciente)
                                            for paciente in self.lista_pacientes
                                        ]
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        ]

    def criar_card_paciente(self, paciente: dict):

        return Container(
            margin=Margin.only(bottom=15),
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
                                f"Telefone: {paciente['telefone']}"
                            ),
                            Text(
                                f"Nascimento: {paciente['data_nascimento']}"
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
                                on_click=lambda e: self.deletar_paciente(
                                    paciente["id"]
                                )
                            )
                        ]
                    ),
                ]
            )
        )

    def deletar_paciente(self, id_paciente):
        self.paciente_dao.deletar_paciente(id_paciente)
        self.lista_pacientes=(self.paciente_dao.ler_paciente())
        self.renderizar_pacientes()

    def cadastrar_paciente(self):
        novo_paciente={
            "id": Gerador_ID("paciente.json","id").id_gerado,
            "nome":self.input_nome.value,
            "telefone":self.input_telefone.value,
            "data_nascimento":self.input_data_nascimento.value
        }
        self.paciente_dao.add_paciente(novo_paciente)
        self.lista_pacientes=(self.paciente_dao.ler_paciente())
        self.input_nome.value=""
        self.input_telefone.value=""
        self.input_data_nascimento.value=""
        self.renderizar_pacientes()

    def renderizar_pacientes(self):
        lista_container=[self.criar_card_paciente(paciente)for paciente in self.lista_pacientes]
        self.controls[0].controls[1].content.controls[3].content.controls = lista_container
        self.update()