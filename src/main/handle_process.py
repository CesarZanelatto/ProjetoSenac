from flet import *
from src.main.constructors.paciente_constructor import paciente_constructor

def app(page:Page):
    page.title="Controle de Estoque"

    def change_route():
        page.views.clear()
        page.views.append(
            paciente_constructor(page)
        )
        page.update()
    page.on_route_change=change_route
    change_route()