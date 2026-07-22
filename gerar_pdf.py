from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

from calcular_lucro import calcular_custos

# --- Dados do fechamento do mês: só isso muda de mês pra mês ---
NOME_MES = "Julho"
BOLOS_VENDIDOS = 18
FATURAMENTO_TOTAL = 228.00


def brl(valor):
    """Formata um número como reais no padrão brasileiro (vírgula)."""
    return f"R$ {valor:.2f}".replace(".", ",")


def pct(valor):
    """Formata uma fração como porcentagem no padrão brasileiro (vírgula)."""
    return f"{valor:.1%}".replace(".", ",")


def gerar_relatorio_pdf():
    custos = calcular_custos()
    custo_total = custos["custo_total_unitario"]
    custo_calda_embalagem = custos["custo_calda_unitario"] + custos["custo_embalagem_unitario"]

    lucro_12 = 12.00 - custo_total
    lucro_13 = 13.00 - custo_total
    margem_12 = lucro_12 / 12.00
    margem_13 = lucro_13 / 13.00

    custo_consumido_mes = BOLOS_VENDIDOS * custo_total
    lucro_real_mes = FATURAMENTO_TOTAL - custo_consumido_mes

    pdf_filename = f"Relatorio_Confeitaria_{NOME_MES}.pdf"
    doc = SimpleDocTemplate(pdf_filename, pagesize=A4, rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36)

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle('DocTitle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=18, textColor=colors.HexColor('#4A2E2B'), alignment=1, spaceAfter=15)
    subtitle_style = ParagraphStyle('DocSubtitle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=13, textColor=colors.HexColor('#4A2E2B'), spaceBefore=12, spaceAfter=8)
    normal_style = ParagraphStyle('DocNormal', parent=styles['Normal'], fontName='Helvetica', fontSize=10, textColor=colors.HexColor('#333333'), spaceAfter=6)
    bold_style = ParagraphStyle('DocBold', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=10, textColor=colors.HexColor('#000000'))
    profit_style = ParagraphStyle('DocProfit', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=11, textColor=colors.HexColor('#2E5A27'))

    story = []

    story.append(Paragraph("🍰 RELATÓRIO DE CUSTOS E DESEMPENHO FINANCEIRO", title_style))
    story.append(Paragraph(f"<b>Período:</b> Fechamento de {NOME_MES} | <b>Produto:</b> Bolo de Pote (250g)", ParagraphStyle('center', parent=normal_style, alignment=1)))
    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#4A2E2B'), spaceAfter=15))

    # Seção 1: Ficha Técnica
    story.append(Paragraph("1. Ficha Técnica e Composição de Custos por Unidade", subtitle_style))
    data_custos = [
        [Paragraph("<b>Componente / Etapa</b>", bold_style), Paragraph("<b>Detalhe da Receita</b>", bold_style), Paragraph("<b>Custo Unitário (R$)</b>", bold_style)],
        ["Massa (Rendimento: 21 un)", "Trigo, Açúcar, Margarina, Leite, Ovos, Fermento", brl(custos['custo_massa_unitario'])],
        ["Recheios (Média 3 sabores)", "Brigadeiro, Coco e Leite Ninho (Rend: 11 un)", brl(custos['custo_recheio_unitario'])],
        ["Calda + Embalagem", "Refrigerante (~1/50) + Pote, Tampa, Colher e Delivery", brl(custo_calda_embalagem)],
        ["Margem de Segurança (10%)", "Gás, Energia Elétrica, Água e Limpeza", brl(custos['margem_invisiveis'])],
        [Paragraph("<b>👉 CUSTO TOTAL POR BOLO</b>", bold_style), Paragraph("<b>Soma de todos os custos diretos + invisíveis</b>", bold_style), Paragraph(f"<b>{brl(custo_total)}</b>", bold_style)]
    ]
    t_custos = Table(data_custos, colWidths=[160, 260, 100])
    t_custos.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4A2E2B')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (2, 0), (2, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CCCCCC')),
        ('BACKGROUND', (0, 1), (-1, 1), colors.HexColor('#F9F6F0')),
        ('BACKGROUND', (0, 3), (-1, 3), colors.HexColor('#F9F6F0')),
        ('BACKGROUND', (0, 5), (-1, 5), colors.HexColor('#D9C3B0')),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(t_custos)
    story.append(Spacer(1, 15))

    # Seção 2: Vendas e Lucratividade
    story.append(Paragraph("2. Simulação de Preço de Venda e Lucratividade", subtitle_style))
    data_vendas = [
        [Paragraph("<b>Cenário de Venda</b>", bold_style), Paragraph("<b>Custo Consumido</b>", bold_style), Paragraph("<b>Lucro Limpo / Bolo</b>", bold_style), Paragraph("<b>Margem (%)</b>", bold_style)],
        ["Venda a R$ 12,00", brl(custo_total), Paragraph(f"<b>{brl(lucro_12)}</b>", profit_style), pct(margem_12)],
        ["Venda a R$ 13,00", brl(custo_total), Paragraph(f"<b>{brl(lucro_13)}</b>", profit_style), pct(margem_13)]
    ]
    t_vendas = Table(data_vendas, colWidths=[140, 120, 140, 120])
    t_vendas.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4A2E2B')),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CCCCCC')),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#E8F0E6')),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
        ('TOPPADDING', (0, 0), (-1, -1), 7),
    ]))
    story.append(t_vendas)
    story.append(Spacer(1, 15))

    # Seção 3: Balanço do mês
    story.append(Paragraph(f"3. Balanço Real de {NOME_MES} ({BOLOS_VENDIDOS} Bolos Vendidos)", subtitle_style))
    story.append(Paragraph("Resumo financeiro das transações efetuadas no mês:", normal_style))
    story.append(Spacer(1, 5))
    data_balanco = [
        [Paragraph("<b>Indicador Financeiro</b>", bold_style), Paragraph("<b>Fórmula / Detalhe</b>", bold_style), Paragraph("<b>Valor Total (R$)</b>", bold_style)],
        ["Faturamento Total", f"Soma das {BOLOS_VENDIDOS} unidades vendidas no mês", brl(FATURAMENTO_TOTAL)],
        ["Custo Total Consumido", f"{BOLOS_VENDIDOS} unidades × {brl(custo_total)} (custo unitário com margem)", brl(custo_consumido_mes)],
        [Paragraph("<b>🔥 LUCRO LIMPO REAL</b>", profit_style), Paragraph("<b>Dinheiro livre gerado pelas vendas no mês</b>", bold_style), Paragraph(f"<b>{brl(lucro_real_mes)}</b>", profit_style)]
    ]
    t_balanco = Table(data_balanco, colWidths=[160, 240, 120])
    t_balanco.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4A2E2B')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (2, 0), (2, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CCCCCC')),
        ('BACKGROUND', (0, 1), (-1, 1), colors.HexColor('#F9F6F0')),
        ('BACKGROUND', (0, 2), (-1, 2), colors.HexColor('#F9F6F0')),
        ('BACKGROUND', (0, 3), (-1, 3), colors.HexColor('#E8F0E6')),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(t_balanco)
    story.append(Spacer(1, 20))

    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#CCCCCC'), spaceAfter=10))
    story.append(Paragraph("Gerado automaticamente via Python & ReportLab • Sistema de Gestão para Confeitaria", ParagraphStyle('footer', parent=normal_style, fontSize=8, textColor=colors.HexColor('#777777'), alignment=1)))

    doc.build(story)
    print(f"PDF '{pdf_filename}' gerado com sucesso!")


if __name__ == "__main__":
    gerar_relatorio_pdf()