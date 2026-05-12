from src.views.agendamento_view import AgendamentoView
from src.controllers.agendamento_controller import AgendamentoController


def agendamento_constructor(page):
    view_agendamento=AgendamentoView()
    AgendamentoController(page,view_agendamento)
    return view_agendamento