from flet import *
from src.main.constructors.paciente_constructor import paciente_constructor
from src.main.constructors.agendamento_constructor import agendamento_constructor

def app(page:Page):
    page.title="Controle de Estoque"

    # def change_route():
    #     page.views.clear()
    #     page.views.append(
    #         paciente_constructor(page)
    #     )
    #     page.update()
    # page.on_route_change=change_route
    # change_route()

    def change_route():
        page.views.clear()
        page.views.append(
            agendamento_constructor(page)
        )
        page.update()
    page.on_route_change=change_route
    change_route()