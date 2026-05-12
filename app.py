from flet import run
from src.main.handle_process import app

import os

# Pega o diretório do arquivo atual
current_file_dir = os.path.dirname(os.path.abspath(__file__))

# Constrói o caminho para src/infrastructure/database
# Dependendo de onde seu arquivo estiver, você pode precisar de mais ".."
# Se este arquivo estiver na raiz, 'src' é direto. Se estiver dentro de outra pasta, use '..'
db_dir = os.path.join(current_file_dir, 'src', 'infrastructure', 'database')

print(os.path.abspath(db_dir))


run(app)