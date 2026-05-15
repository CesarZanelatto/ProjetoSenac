# 🏥 Medical Clinic

Sistema desenvolvido para gerenciamento de clínicas médicas, permitindo o controle de pacientes, consultas e informações da clínica de forma simples e organizada.

---

# 📋 Sobre o Projeto

O **Medical Clinic** foi criado como projeto acadêmico do **Senac** com o objetivo de facilitar o gerenciamento de clínicas médicas.

O sistema possui uma interface intuitiva e oferece funcionalidades essenciais para o controle administrativo da clínica.

Com o sistema é possível:

* 📊 Visualizar informações da clínica no Dashboard
* 👤 Cadastrar pacientes
* 📅 Realizar agendamentos de consultas
* 🗂️ Organizar atendimentos
* 🔎 Consultar informações rapidamente

---

# 🚀 Funcionalidades

## 📊 Dashboard

A tela principal do sistema apresenta:

* Total de pacientes cadastrados
* Quantidade de consultas agendadas
* Informações gerais da clínica
* Navegação rápida entre as telas

---

## 👤 Cadastro de Pacientes

O usuário pode:

* Adicionar novos pacientes
* Visualizar pacientes cadastrados
* Remover pacientes do sistema
* Organizar informações de atendimento

---

## 📅 Agendamentos

Na tela de agendamentos é possível:

* Selecionar datas no calendário
* Escolher horários de consulta
* Selecionar pacientes
* Definir procedimentos médicos
* Registrar consultas

---

# 🛠️ Tecnologias Utilizadas

O projeto foi desenvolvido utilizando:

* Python
* Flet
* JSON para armazenamento de dados

---

# 📁 Estrutura do Projeto

```bash
ProjetoSenac/
│
├── app.py
├── requirements.txt
│
├── src/
│   ├── controllers/
│   ├── infrastructure/
│   ├── main/
│   ├── models/
│   └── views/
```

---

# ▶️ Como Executar o Projeto

## 1️⃣ Clone o repositório

```bash
https://github.com/CesarZanelatto/SistemaClinica.git
```

---

## 2️⃣ Acesse a pasta do projeto

```bash
cd SistemaClinica
```

---

## 3️⃣ Crie um ambiente virtual

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / MacOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 5️⃣ Execute o sistema

```bash
python app.py
```

---
## 6 Como Buildar o sistema:
Para gerar o executável da aplicação utilizando Flet + PyInstaller:

```powershell
flet pack app.py --add-data "src/infrastructure/database;src/infrastructure/database"

# 📸 Imagens do Sistema

Adicione aqui screenshots do sistema:

* Dashboard
* Cadastro de Pacientes
* Agendamentos

Exemplo:

```md
![Dashboard](./imagens/dashboard.png)
```

---

# 👨‍💻 Integrantes

* Cesar
* Gabriel
* Raissa

---

# 📚 Projeto Acadêmico

Projeto desenvolvido para atividades acadêmicas do **Senac**.

---

# 📄 Licença

Este projeto é destinado para fins educacionais.

