from flet import *
from src.main.constructors.paciente_constructor import paciente_constructor
from src.main.constructors.agendamento_constructor import agendamento_constructor
from src.main.constructors.dashboard_constructor import dashboard_constructor

def app(page: Page):
    page.title = "Medical Clinic"
    def change_route():
        page.views.clear()
        if page.route == "/dashboard":
            page.views.append(dashboard_constructor(page))
        elif page.route == "/pacientes":
            page.views.append(paciente_constructor(page))
        elif page.route == "/agendamentos":
            page.views.append(agendamento_constructor(page))
        page.update()
    page.on_route_change=change_route
    page.go("/dashboard")