import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter


wb = openpyxl.Workbook()
wb.active.title = "1. Ficha Técnica"
ws1 = wb["1. Ficha Técnica"]
ws1.views.sheetView[0].showGridLines = True


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


ws1["A1"] = "🍰 FICHA TÉCNICA E CUSTO AUTOMÁTICO POR BOLO (250g)"
ws1["A1"].font = font_title


headers = ["Ingrediente / Etapa", "Embalagem", "Preço Pago (R$)", "Uso na Receita", "Custo (R$)"]
for col_idx, h in enumerate(headers, start=1):
    cell = ws1.cell(row=4, column=col_idx, value=h)
    cell.font = font_header
    cell.fill = header_fill
    cell.alignment = Alignment(horizontal="center")


dados = [
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

for row_idx, linha in enumerate(dados, start=5):
    is_destaque = "👉" in linha[0]
    for col_idx, val in enumerate(linha, start=1):
        cell = ws1.cell(row=row_idx, column=col_idx, value=val)
        cell.border = box_border
        
        if is_destaque:
            cell.font = font_bold
            cell.fill = sub_fill
        elif row_idx % 2 == 0:
            cell.fill = zebra_fill
            
        if col_idx in [3, 5] and val != "":
            cell.number_format = "R$ #,##0.00"
        if col_idx in [2, 4]:
            cell.alignment = Alignment(horizontal="center")


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
    if "Lucro" in label:
        ws1.cell(row=idx, column=7).fill = green_fill
        c_val.fill = green_fill
    elif "TOTAL" in label:
        ws1.cell(row=idx, column=7).fill = sub_fill
        c_val.fill = sub_fill


for col in ws1.columns:
    max_len = max(len(str(cell.value or '')) for cell in col)
    col_letter = get_column_letter(col[0].column)
    ws1.column_dimensions[col_letter].width = max(max_len + 3, 12)

ws1.column_dimensions["A"].width = 32
ws1.column_dimensions["G"].width = 28


wb.save("Minha_Planilha_Gerada.xlsx")
print("Planilha Minha_Planilha_Gerada.xlsx criada com sucesso!")


#comando no terminal: python gerar_planilha.py - escrever e abrir a planilha gerada no Excel