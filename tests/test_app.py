import sys
import os

# Adiciona a pasta src ao caminho para importar o app
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from app import app


def test_pagina_inicial():
    """
    Verifica se a página inicial abre corretamente.
    """
    cliente = app.test_client()

    resposta = cliente.get("/")

    assert resposta.status_code == 200