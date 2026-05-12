from src.views.paciente_view import PacienteView
from src.controllers.paciente_controller import PacienteController

def paciente_constructor(page):
    view_paciente=PacienteView()
    PacienteController(page, view_paciente)
    return view_paciente