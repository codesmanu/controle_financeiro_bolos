"""
Fonte única de verdade dos preços pagos nos ingredientes.

Por que este arquivo existe
---------------------------
Antes, cada script (gerar_planilha.py, gerar_dashboard.py, calcular_lucro.py)
tinha sua própria cópia dos preços dos ingredientes, hardcoded. Quando um
preço mudava no mercado era preciso lembrar de editar em vários lugares —
e era fácil esquecer um deles, fazendo os arquivos gerados ficarem com
números diferentes entre si.

Agora existe uma única lista de preços, guardada em precos.json. Todos os
scripts leem os preços daqui (carregar_precos), e o atualizar_planilha.py
é o único que escreve nela (salvar_precos).
"""

import json
import os

CAMINHO_PRECOS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "precos.json")


def carregar_precos():
    """Lê o precos.json e devolve o dicionário de ingredientes."""
    with open(CAMINHO_PRECOS, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_precos(ingredientes):
    """Grava o dicionário de ingredientes de volta no precos.json."""
    with open(CAMINHO_PRECOS, "w", encoding="utf-8") as f:
        json.dump(ingredientes, f, ensure_ascii=False, indent=2)


def preco(chave):
    """Atalho pra pegar só o valor numérico do preço de um ingrediente."""
    return carregar_precos()[chave]["preco"]