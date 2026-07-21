# 1. Tabela de preços pagos no mercado
precos = {
    'creme_de_leite_200g': 3.25,
    'leite_condensado_395g': 6.25,
    'margarina_250g': 2.99,
    'leite_em_po_200g': 7.75,
    'fermento_100g': 3.75,
    'trigo_1000g': 5.75,
    'leite_liquido_1000ml': 7.00,
    'coco_ralado_50g': 3.99,
    'chocolate_po_1000g': 55.00,  # média entre 50 e 60
    'acucar_1000g': 4.00,
    'ovo_1un': 0.60
}

# 2. Custo da Massa (Rendimento: 21 bolos)
custo_trigo = (360 / 1000) * precos['trigo_1000g']       # 3 xícaras (120g cada)
custo_acucar = (240 / 1000) * precos['acucar_1000g']     # 1,5 xícara (160g cada)
custo_margarina = (100 / 250) * precos['margarina_250g'] # 100g
custo_leite = (300 / 1000) * precos['leite_liquido_1000ml'] # 300ml
custo_fermento = (10 / 100) * precos['fermento_100g']    # 10g
custo_ovos = 3 * precos['ovo_1un']                       # 3 ovos

total_massa = custo_trigo + custo_acucar + custo_margarina + custo_leite + custo_fermento + custo_ovos
custo_massa_unitario = total_massa / 21


custo_brigadeiro = precos['leite_condensado_395g'] + precos['creme_de_leite_200g'] + (45 / 1000) * precos['chocolate_po_1000g']
custo_coco = precos['leite_condensado_395g'] + precos['creme_de_leite_200g'] + precos['coco_ralado_50g']
custo_ninho = precos['leite_condensado_395g'] + precos['creme_de_leite_200g'] + (30 / 200) * precos['leite_em_po_200g']

total_3_recheios = custo_brigadeiro + custo_coco + custo_ninho
custo_recheio_unitario = total_3_recheios / 11


custo_calda_unitario = 12.50 / 50  
custo_embalagem_unitario = 0.90    

custo_direto = custo_massa_unitario + custo_recheio_unitario + custo_calda_unitario + custo_embalagem_unitario
margem_invisiveis = custo_direto * 0.10  
custo_total_unitario = custo_direto + margem_invisiveis


print("--- FICHA TÉCNICA (CUSTO POR POTINHO) ---")
print(f"Massa do bolo: R$ {custo_massa_unitario:.2f}")
print(f"Recheio (média): R$ {custo_recheio_unitario:.2f}")
print(f"Calda + Embalagens: R$ {custo_calda_unitario + custo_embalagem_unitario:.2f}")
print(f"Margem Gás/Luz (10%): R$ {margem_invisiveis:.2f}")
print(f"👉 CUSTO TOTAL POR BOLO: R$ {custo_total_unitario:.2f}\n")

print("--- SIMULAÇÃO DE VENDAS E LUCRO ---")
print(f"Venda a R$ 12,00 -> Lucro Limpo: R$ {12.00 - custo_total_unitario:.2f} (Margem: {(12-custo_total_unitario)/12:.1%})")
print(f"Venda a R$ 13,00 -> Lucro Limpo: R$ {13.00 - custo_total_unitario:.2f} (Margem: {(13-custo_total_unitario)/13:.1%})\n")


faturamento_julho = 228.00
custo_julho = 18 * custo_total_unitario
lucro_julho = faturamento_julho - custo_julho
print(f"🍰 FECHAMENTO DE JULHO (18 bolos vendidos):")
print(f"Faturamento: R$ {faturamento_julho:.2f} | Custo Consumido: R$ {custo_julho:.2f} | LUCRO REAL: R$ {lucro_julho:.2f}")