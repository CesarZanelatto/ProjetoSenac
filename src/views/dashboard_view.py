from flet import *

configBtn = {
    ResponsiveRowBreakpoint.XS: 10,
    ResponsiveRowBreakpoint.SM: 6,
    ResponsiveRowBreakpoint.LG: 3
}

pacientes = []
fila_atendimento = []


def main(page: Page):
    page.title = "Sistema Clínica Simples"
    page.window.height = 1100
    page.window.width = 850
    page.bgcolor = "#E6F4F5"
    page.padding = 0
    page.spacing = 0

    btn1 = Button("Dashboard",
                  icon=Icons.DASHBOARD,
                  col=configBtn,
                  color="Black",
                  bgcolor="#FFFFFF",
                  height=55,
                  width=212)

    btn2 = Button("Pacientes",
                  icon=Icons.PEOPLE,
                  col=configBtn,
                  color="Black",
                  bgcolor="#FFFFFF",
                  height=55,
                  width=212)

    btn3 = Button("Agendamentos",
                  icon=Icons.CALENDAR_TODAY_OUTLINED,
                  col=configBtn,
                  color="Black",
                  bgcolor="#FFFFFF",
                  height=55,
                  width=212)

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

    pesquisa = TextField(
        icon=Icons.SEARCH,
        label="Pesquisar",
        label_style=TextStyle(color="Black"),
        color="Black",
        bgcolor="#E6F4F5",
        width=363,
        height=56,
        border_radius=10
    )

    caixa_superior = Container(
        bgcolor="#FFFFFF",
        padding=20,
        content=Row(
            controls=[pesquisa],
            spacing=0,
            alignment=MainAxisAlignment.SPACE_BETWEEN
        )
    )

    def card(texto, valor, cor):
        return Container(
            content=Column([
                Text(texto, font_family="Bold", color="Black", size=12),
                Text(valor, size=28, weight=FontWeight.BOLD, color="Black")
            ]),
            bgcolor=cor,
            padding=15,
            border_radius=10,
            width=180,
            height=120,
        )

    cards = Row(
        spacing=10,
        controls=[
            card("Total de\nPacientes:", "", "#D1EAEA", ),
            card("Total de\nAgendamentos:", "", "#F2D1C2"),
            card("Total Fila de\nEspera:", "", "#F2D1C2"),

        ]
    )

    fila_espera = Container(
        bgcolor="White",
        padding=15,
        border_radius=15,
        expand=True,
        content=Column(scroll=ScrollMode.AUTO,
                       controls=[
                           Row([
                               Text("Fila de Espera",
                                    color="Black",
                                    weight=FontWeight.BOLD),
                               Icon(Icons.MORE_HORIZ)
                           ], spacing=50),
                           Container(bgcolor="#E6F4F5",
                                     padding=10,
                                     border_radius=10,
                                     content=Row([Icon(Icons.PERSON),
                                                  Text("Alguém",
                                                       color="Black",
                                                       size=11)])),
                           Container(bgcolor="#E6F4F5",
                                     padding=10,
                                     border_radius=10,
                                     content=Row([Icon(Icons.PERSON),
                                                  Text("Alguém",
                                                       color="Black",
                                                       size=11)]))
                       ])
    )

    conteudo_meio = Container(
        bgcolor="White",
        padding=15,
        border_radius=15,
        content=cards
    )

    coluna_principal = Column(
        expand=True,
        spacing=20,
        controls=[
            Text(
                "Dashboard",
                size=28,
                color="Black",
                weight=FontWeight.BOLD
            ),
            conteudo_meio,
            fila_espera
        ]
    )

    conteudo_direita = Column(
        expand=True,
        spacing=20,
        controls=[
            caixa_superior,
            Container(padding=15, content=coluna_principal)
        ]
    )

    layout = Row(
        expand=True,
        spacing=0,
        controls=[
            sidebar,
            conteudo_direita
        ]
    )

    page.add(layout)


if __name__ == '__main__':
    run(main)
