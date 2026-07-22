"""
Calcula os custos de produção e simula lucro de vendas do bolo de pote.

Os preços dos ingredientes vêm do precos.json (via precos.py) — a mesma
fonte usada pelo gerar_planilha.py e pelo gerar_dashboard.py. Pra mudar um
preço, rode atualizar_planilha.py; não edite os números aqui.
"""

from precos import carregar_precos


def calcular_custos():
    """Calcula o custo de produção por bolo e devolve um dicionário com
    todos os valores intermediários, pra outros scripts (como o
    gerar_pdf.py) reaproveitarem sem duplicar a conta."""
    ingredientes = carregar_precos()

    def preco(chave):
        return ingredientes[chave]["preco"]

    # --- Custo da Massa (Rendimento: 21 bolos) ---
    custo_trigo = (360 / 1000) * preco("farinha_trigo")     # 3 xícaras (120g cada)
    custo_acucar = (240 / 1000) * preco("acucar")           # 1,5 xícara (160g cada)
    custo_margarina = (100 / 250) * preco("margarina")      # 100g
    custo_leite = (300 / 1000) * preco("leite_liquido")     # 300ml
    custo_fermento = (10 / 100) * preco("fermento")         # 10g
    custo_ovos = 3 * preco("ovos")                          # 3 ovos

    total_massa = custo_trigo + custo_acucar + custo_margarina + custo_leite + custo_fermento + custo_ovos
    custo_massa_unitario = total_massa / 21

    # --- Custo dos Recheios (Rendimento: 11 bolos) ---
    # Leite condensado e creme de leite são comprados em kits de 3 caixas.
    # Cada receita de recheio (brigadeiro, coco, ninho) usa 1 caixa de cada,
    # por isso dividimos o preço do kit de 3 por 3.
    preco_leite_condensado_1un = preco("leite_condensado") / 3
    preco_creme_leite_1un = preco("creme_de_leite") / 3

    custo_brigadeiro = preco_leite_condensado_1un + preco_creme_leite_1un + (45 / 1000) * preco("chocolate_po")
    custo_coco = preco_leite_condensado_1un + preco_creme_leite_1un + preco("coco_ralado")
    custo_ninho = preco_leite_condensado_1un + preco_creme_leite_1un + (30 / 200) * preco("leite_em_po")

    total_3_recheios = custo_brigadeiro + custo_coco + custo_ninho
    custo_recheio_unitario = total_3_recheios / 11

    # --- Calda, embalagem e margem de segurança ---
    custo_calda_unitario = preco("calda_refrigerante") / 50
    custo_embalagem_unitario = preco("kit_embalagem")

    custo_direto = custo_massa_unitario + custo_recheio_unitario + custo_calda_unitario + custo_embalagem_unitario
    margem_invisiveis = custo_direto * 0.10
    custo_total_unitario = custo_direto + margem_invisiveis

    return {
        "custo_massa_unitario": custo_massa_unitario,
        "custo_recheio_unitario": custo_recheio_unitario,
        "custo_calda_unitario": custo_calda_unitario,
        "custo_embalagem_unitario": custo_embalagem_unitario,
        "margem_invisiveis": margem_invisiveis,
        "custo_total_unitario": custo_total_unitario,
    }


def imprimir_relatorio(faturamento_mes=228.00, bolos_vendidos=18, nome_mes="Julho"):
    """Imprime o relatório no terminal. Pra fechar outro mês, chame com
    imprimir_relatorio(faturamento_mes=..., bolos_vendidos=..., nome_mes=...)."""
    c = calcular_custos()

    print("--- FICHA TÉCNICA (CUSTO POR POTINHO) ---")
    print(f"Massa do bolo: R$ {c['custo_massa_unitario']:.2f}")
    print(f"Recheio (média): R$ {c['custo_recheio_unitario']:.2f}")
    print(f"Calda + Embalagens: R$ {c['custo_calda_unitario'] + c['custo_embalagem_unitario']:.2f}")
    print(f"Margem Gás/Luz (10%): R$ {c['margem_invisiveis']:.2f}")
    print(f"👉 CUSTO TOTAL POR BOLO: R$ {c['custo_total_unitario']:.2f}\n")

    print("--- SIMULAÇÃO DE VENDAS E LUCRO ---")
    custo = c["custo_total_unitario"]
    print(f"Venda a R$ 12,00 -> Lucro Limpo: R$ {12.00 - custo:.2f} (Margem: {(12 - custo) / 12:.1%})")
    print(f"Venda a R$ 13,00 -> Lucro Limpo: R$ {13.00 - custo:.2f} (Margem: {(13 - custo) / 13:.1%})\n")

    custo_mes = bolos_vendidos * custo
    lucro_mes = faturamento_mes - custo_mes
    print(f"🍰 FECHAMENTO DE {nome_mes.upper()} ({bolos_vendidos} bolos vendidos):")
    print(f"Faturamento: R$ {faturamento_mes:.2f} | Custo Consumido: R$ {custo_mes:.2f} | LUCRO REAL: R$ {lucro_mes:.2f}")


if __name__ == "__main__":
    imprimir_relatorio()