#  Remoção de Fundo com FastAPI + Streamlit

Este projeto combina **FastAPI** (backend) e **Streamlit** (frontend) para remover o fundo de imagens usando a biblioteca [rembg](https://github.com/danielgatis/rembg).

---

## Tecnologias utilizadas
- [FastAPI](https://fastapi.tiangolo.com/) — Framework para criação de APIs rápidas em Python
- [Uvicorn](https://www.uvicorn.org/) — Servidor ASGI para rodar o FastAPI
- [rembg](https://github.com/danielgatis/rembg) — Biblioteca para remoção de fundo
- [Pillow (PIL)](https://python-pillow.org/) — Manipulação de imagens
- [Streamlit](https://streamlit.io/) — Interface web simples e interativa

---

## 📦 Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repo.git
   cd seu-repo/backend
2. Crie e ative um ambiente virtual
python -m venv env
source env/bin/activate   # Linux/Mac
env\Scripts\activate      # Windows

3. instale as dependencias
pip install -r requirements.txt

4. Executar o backend
na raiz da pasta backend
uvicorn api.main:app --reload

o servidor esta disponivel em http://127.0.0.1:8000
5. Executando o Frontend (Streamlit)
streamlit run streamlit_app.py

-----------------------------------------------------------
backend/
│
├── api/                # Código da API FastAPI
│   └── main.py
│
├── env/                # Ambiente virtual (ignorado no GitHub)
├── requirements.txt    # Dependências do projeto
├── README.md           # Documentação
└── .gitignore

