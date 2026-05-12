from src.models.entitys.paciente import Paciente
from src.models.DAO.paciente_dao import PacienteDAO
from src.infrastructure.services.gerador_id import Gerador_ID
from src.views.paciente_view import PacienteView


class PacienteController:

    def __init__(self, page, tela: PacienteView):
        self.dao = PacienteDAO()
        self.page = page
        self.tela = tela
        self.tela.btn_cadastrar.on_click = self.handle_add_paciente
        self.listar_pacientes()

    def listar_pacientes(self) -> None:
        self.tela.lista_pacientes = self.dao.ler_paciente()
        # recria os cards conectando o delete ao controller
        lista_container = []
        for paciente in self.tela.lista_pacientes:
            card = self.tela.criar_card_paciente(paciente)
            delete_button = card.content.controls[1].controls[1]
            delete_button.on_click = lambda e, paciente_id=paciente["id"]: self.handle_delete_paciente(paciente_id)
            lista_container.append(card)

        self.tela.controls[0].controls[1].content.controls[3].content.controls = lista_container
        self.page.update()

    def buscar_paciente_id(self, id: int):
        try:
            return self.dao.buscar_por_ID(id)
        except Exception as e:
            return e

    def handle_add_paciente(self):
        p = Paciente(
            Gerador_ID("paciente.json", "id").id_gerado,
            self.tela.input_nome.value,
            self.tela.input_data_nascimento.value,
            self.tela.input_telefone.value
        )

        try:
            self.dao.add_paciente(p.to_dict())
            self.tela.input_nome.value = ""
            self.tela.input_data_nascimento.value = ""
            self.tela.input_telefone.value = ""
            self.tela.input_nome.update()
            self.tela.input_data_nascimento.update()
            self.tela.input_telefone.update()
            self.listar_pacientes()
        except Exception as e:
            print(e)

    def handle_delete_paciente(self, id_paciente: int):
        try:
            self.dao.deletar_paciente(id_paciente)
            self.listar_pacientes()
        except Exception as e:
            print(e)
