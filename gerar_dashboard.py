import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.chart import BarChart, Reference


wb = openpyxl.Workbook()


header_fill = PatternFill(start_color="4A2E2B", end_color="4A2E2B", fill_type="solid")  
sub_fill = PatternFill(start_color="D9C3B0", end_color="D9C3B0", fill_type="solid")   
zebra_fill = PatternFill(start_color="F9F6F0", end_color="F9F6F0", fill_type="solid")  
green_fill = PatternFill(start_color="E8F0E6", end_color="E8F0E6", fill_type="solid")   

font_title = Font(name="Arial", size=15, bold=True, color="4A2E2B")
font_header = Font(name="Arial", size=11, bold=True, color="FFFFFF")
font_bold = Font(name="Arial", size=11, bold=True, color="000000")
font_profit = Font(name="Arial", size=11, bold=True, color="2E5A27")

border_thin = Side(border_style="thin", color="CCCCCC")
box_border = Border(left=border_thin, right=border_thin, top=border_thin, bottom=border_thin)


# ABA 1: FICHA TÉCNICA

ws1 = wb.active
ws1.title = "1. Ficha Técnica e Custos"
ws1.views.sheetView[0].showGridLines = True
ws1["A1"] = "🍰 FICHA TÉCNICA E CUSTO AUTOMÁTICO (250g)"
ws1["A1"].font = font_title

headers1 = ["Ingrediente / Etapa", "Embalagem", "Preço Pago (R$)", "Uso na Receita", "Custo (R$)"]
for col_idx, h in enumerate(headers1, start=1):
    c = ws1.cell(row=4, column=col_idx, value=h)
    c.font, c.fill, c.alignment = font_header, header_fill, Alignment(horizontal="center")

dados1 = [
    ("Farinha de Trigo", "1000g", 5.75, "360g", "=C5*(360/1000)"),
    ("Açúcar", "1000g", 4.00, "240g", "=C6*(240/1000)"),
    ("Margarina", "250g", 2.99, "100g", "=C7*(100/250)"),
    ("Leite Líquido", "1000ml", 7.00, "300ml", "=C8*(300/1000)"),
    ("Fermento em Pó", "100g", 3.75, "10g", "=C9*(10/100)"),
    ("Ovos", "1 un", 0.60, "3 un", "=C10*3"),
    ("👉 CUSTO DA MASSA (POR BOLO)", "", "", "1 un (1/21 da massa)", "=SUM(E5:E10)/21"),
    ("Leite Condensado (3 caixas)", "395g", 18.75, "3 caixas", "=C12"),
    ("Creme de Leite (3 caixas)", "200g", 9.75, "3 caixas", "=C13"),
    ("Chocolate em Pó 50%", "1000g", 55.00, "45g", "=C14*(45/1000)"),
    ("Coco Ralado", "50g", 3.99, "50g", "=C15"),
    ("Leite em Pó", "200g", 7.75, "30g", "=C16*(30/200)"),
    ("👉 CUSTO DO RECHEIO (POR BOLO)", "", "", "1 un (1/11 dos recheios)", "=SUM(E12:E16)/11"),
    ("Calda de Refrigerante", "Garrafa", 12.50, "Porção (~1/50)", "=C18/50"),
    ("Kit Embalagem + Delivery", "Kit", 0.90, "1 kit", "=C19"),
]

for r_idx, linha in enumerate(dados1, start=5):
    is_destaque = "👉" in linha[0]
    for c_idx, val in enumerate(linha, start=1):
        cell = ws1.cell(row=r_idx, column=c_idx, value=val)
        cell.border = box_border
        if is_destaque: cell.font, cell.fill = font_bold, sub_fill
        elif r_idx % 2 == 0: cell.fill = zebra_fill
        if c_idx in [3, 5] and val != "": cell.number_format = "R$ #,##0.00"
        if c_idx in [2, 4]: cell.alignment = Alignment(horizontal="center")

ws1["G4"] = "💡 RESUMO FINAL POR POTINHO"
ws1["G4"].font = Font(name="Arial", size=11, bold=True, color="4A2E2B")
resumo = [
    ("Soma Custo Direto:", "=E11+E17+E18+E19"),
    ("+ Gás/Luz/Invisíveis (10%):", "=I5*0.1"),
    ("🔥 CUSTO TOTAL:", "=I5+I6"),
    ("Lucro Venda R$ 12,00:", "=12-I7"),
    ("Lucro Venda R$ 13,00:", "=13-I7")
]
for idx, (label, form) in enumerate(resumo, start=5):
    ws1.cell(row=idx, column=7, value=label).font = font_bold if "TOTAL" in label or "Lucro" in label else Font(name="Arial", size=11)
    c_val = ws1.cell(row=idx, column=9, value=form)
    c_val.number_format = "R$ #,##0.00"
    c_val.font = font_profit if "Lucro" in label else font_bold
    if "Lucro" in label: ws1.cell(row=idx, column=7).fill, c_val.fill = green_fill, green_fill
    elif "TOTAL" in label: ws1.cell(row=idx, column=7).fill, c_val.fill = sub_fill, sub_fill


# ABA 2: CONTROLE DE VENDAS

ws2 = wb.create_sheet(title="2. Controle de Vendas")
ws2.views.sheetView[0].showGridLines = True
ws2["A1"] = "📊 DIÁRIO DE VENDAS E REGISTRO DE PIX"
ws2["A1"].font = font_title

headers2 = ["Data", "Cliente", "Local", "Qtd", "Preço (R$)", "Total (R$)", "Custo (R$)", "LUCRO LIMPO (R$)"]
for col_idx, h in enumerate(headers2, start=1):
    c = ws2.cell(row=4, column=col_idx, value=h)
    c.font, c.fill, c.alignment = font_header, header_fill, Alignment(horizontal="center")

vendas_ex = [
    ("14/07/2026", "Andrea Rodrigues", "Casa", 1, 12.00),
    ("14/07/2026", "Maria Eduarda", "Casa", 1, 12.00),
    ("15/07/2026", "Marcus Wilker (Irmão)", "Trabalho", 3, 13.00),
    ("16/07/2026", "Kamilly Vitória", "Casa", 1, 12.00),
    ("17/07/2026", "Franklimilton", "Casa", 1, 12.00),
    ("19/07/2026", "Franklimilton", "Casa", 2, 12.00),
    ("20/07/2026", "Marcus Wilker (Irmão)", "Trabalho", 4, 13.00),
    ("20/07/2026", "Marcus Wilker (Irmão)", "Trabalho", 5, 13.00),
]

for idx, (dt, cli, loc, qtd, prc) in enumerate(vendas_ex, start=5):
    ws2.cell(row=idx, column=1, value=dt).alignment = Alignment(horizontal="center")
    ws2.cell(row=idx, column=2, value=cli)
    ws2.cell(row=idx, column=3, value=loc).alignment = Alignment(horizontal="center")
    ws2.cell(row=idx, column=4, value=qtd).alignment = Alignment(horizontal="center")
    ws2.cell(row=idx, column=5, value=prc).number_format = "R$ #,##0.00"
    
    ws2.cell(row=idx, column=6, value=f"=D{idx}*E{idx}").number_format = "R$ #,##0.00"
    ws2.cell(row=idx, column=7, value=f"=D{idx}*'1. Ficha Técnica e Custos'!$I$7").number_format = "R$ #,##0.00"
    
    c_prof = ws2.cell(row=idx, column=8, value=f"=F{idx}-G{idx}")
    c_prof.number_format = "R$ #,##0.00"
    c_prof.font, c_prof.fill = font_profit, green_fill
    
    for c in range(1, 9): ws2.cell(row=idx, column=c).border = box_border

# Linha de Totais do Mês
ws2.cell(row=13, column=3, value="TOTAL DO MÊS:").font = font_bold
ws2.cell(row=13, column=4, value="=SUM(D5:D12)").font = font_bold
ws2.cell(row=13, column=6, value="=SUM(F5:F12)").font = font_bold
ws2.cell(row=13, column=6).number_format = "R$ #,##0.00"
ws2.cell(row=13, column=7, value="=SUM(G5:G12)").font = font_bold
ws2.cell(row=13, column=7).number_format = "R$ #,##0.00"
ws2.cell(row=13, column=8, value="=SUM(H5:H12)").font = font_profit
ws2.cell(row=13, column=8).number_format = "R$ #,##0.00"
ws2.cell(row=13, column=8).fill = green_fill


# ABA 3: DASHBOARD VISUAL COM GRÁFICO

ws3 = wb.create_sheet(title="3. Dashboard Visual")
ws3.views.sheetView[0].showGridLines = True
ws3["A1"] = "📈 DASHBOARD DE DESEMPENHO E GRÁFICOS"
ws3["A1"].font = font_title

headers3 = ["Indicador", "Valor (R$)", "Descrição"]
for col_idx, h in enumerate(headers3, start=1):
    c = ws3.cell(row=4, column=col_idx, value=h)
    c.font, c.fill, c.alignment = font_header, header_fill, Alignment(horizontal="center")

dash_items = [
    ("Faturamento Total de Vendas", "='2. Controle de Vendas'!F13", "Soma de todas as vendas do mês"),
    ("Custo Total de Produção Usado", "='2. Controle de Vendas'!G13", "Custo das matérias-primas e potes consumidos"),
    ("LUCRO LIMPO REAL", "='2. Controle de Vendas'!H13", "Dinheiro limpo no seu bolso!")
]

for idx, (ind, form, desc) in enumerate(dash_items, start=5):
    ws3.cell(row=idx, column=1, value=ind).font = font_bold
    c_v = ws3.cell(row=idx, column=2, value=form)
    c_v.number_format = "R$ #,##0.00"
    c_v.font = font_profit if "LUCRO" in ind else font_bold
    ws3.cell(row=idx, column=3, value=desc)
    for c in range(1, 4):
        ws3.cell(row=idx, column=c).border = box_border
        if "LUCRO" in ind: ws3.cell(row=idx, column=c).fill = green_fill


chart = BarChart()
chart.type = "col"
chart.style = 10
chart.title = "Faturamento vs Custo vs Lucro Real (Julho)"
chart.y_axis.title = "Valor (R$)"
chart.x_axis.title = "Indicadores Financeiros"

data_ref = Reference(ws3, min_col=2, min_row=4, max_row=7)
cats_ref = Reference(ws3, min_col=1, min_row=5, max_row=7)
chart.add_data(data_ref, titles_from_data=True)
chart.set_categories(cats_ref)
chart.width = 16
chart.height = 10

# Adiciona o gráfico exatamente a partir da célula E4 da Aba 3!
ws3.add_chart(chart, "E4")


for ws in [ws1, ws2, ws3]:
    for col in ws.columns:
        max_len = max(len(str(cell.value or '')) for cell in col)
        col_letter = get_column_letter(col[0].column)
        ws.column_dimensions[col_letter].width = max(max_len + 4, 12)


wb.save("Minha_Planilha_Completa.xlsx")
print("✅ SUCESSO! Arquivo 'Minha_Planilha_Completa.xlsx' gerado com Dashboard e Gráficos de Barras!")