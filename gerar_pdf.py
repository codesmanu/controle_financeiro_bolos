from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def gerar_relatorio_pdf():
    pdf_filename = "Relatorio_Confeitaria_Julho.pdf"
    doc = SimpleDocTemplate(pdf_filename, pagesize=A4, rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36)
    
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle('DocTitle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=18, textColor=colors.HexColor('#4A2E2B'), alignment=1, spaceAfter=15)
    subtitle_style = ParagraphStyle('DocSubtitle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=13, textColor=colors.HexColor('#4A2E2B'), spaceBefore=12, spaceAfter=8)
    normal_style = ParagraphStyle('DocNormal', parent=styles['Normal'], fontName='Helvetica', fontSize=10, textColor=colors.HexColor('#333333'), spaceAfter=6)
    bold_style = ParagraphStyle('DocBold', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=10, textColor=colors.HexColor('#000000'))
    profit_style = ParagraphStyle('DocProfit', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=11, textColor=colors.HexColor('#2E5A27'))

    story = []
    
    
    story.append(Paragraph("🍰 RELATÓRIO DE CUSTOS E DESEMPENHO FINANCEIRO", title_style))
    story.append(Paragraph("<b>Período:</b> Fechamento de Julho | <b>Produto:</b> Bolo de Pote (250g)", ParagraphStyle('center', parent=normal_style, alignment=1)))
    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#4A2E2B'), spaceAfter=15))
    
    # Seção 1: Ficha Técnica
    story.append(Paragraph("1. Ficha Técnica e Composição de Custos por Unidade", subtitle_style))
    data_custos = [
        [Paragraph("<b>Componente / Etapa</b>", bold_style), Paragraph("<b>Detalhe da Receita</b>", bold_style), Paragraph("<b>Custo Unitário (R$)</b>", bold_style)],
        ["Massa (Rendimento: 21 un)", "Trigo, Açúcar, Margarina, Leite, Ovos, Fermento", "R$ 0,40"],
        ["Recheios (Média 3 sabores)", "Brigadeiro, Coco e Leite Ninho (Rend: 11 un)", "R$ 3,28"],
        ["Calda + Embalagem", "Refrigerante (~1/50) + Pote, Tampa, Colher e Delivery", "R$ 1,15"],
        ["Margem de Segurança (10%)", "Gás, Energia Elétrica, Água e Limpeza", "R$ 0,48"],
        [Paragraph("<b>👉 CUSTO TOTAL POR BOLO</b>", bold_style), Paragraph("<b>Soma de todos os custos diretos + invisíveis</b>", bold_style), Paragraph("<b>R$ 5,32</b>", bold_style)]
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
        ["Venda a R$ 12,00", "R$ 5,32", Paragraph("<b>R$ 6,68</b>", profit_style), "55,6%"],
        ["Venda a R$ 13,00", "R$ 5,32", Paragraph("<b>R$ 7,68</b>", profit_style), "59,1%"]
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
    
    # Seção 3: Balanço de Julho
    story.append(Paragraph("3. Balanço Real de Julho (18 Bolos Vendidos)", subtitle_style))
    story.append(Paragraph("Resumo financeiro das transações efetuadas no mês de julho:", normal_style))
    story.append(Spacer(1, 5))
    data_balanco = [
        [Paragraph("<b>Indicador Financeiro</b>", bold_style), Paragraph("<b>Fórmula / Detalhe</b>", bold_style), Paragraph("<b>Valor Total (R$)</b>", bold_style)],
        ["Faturamento Total", "Soma das 18 unidades vendidas (a R$ 12 e R$ 13)", "R$ 228,00"],
        ["Custo Total Consumido", "18 unidades × R$ 5,32 (custo unitário com margem)", "R$ 95,81"],
        [Paragraph("<b>🔥 LUCRO LIMPO REAL</b>", profit_style), Paragraph("<b>Dinheiro livre gerado pelas vendas no mês</b>", bold_style), Paragraph("<b>R$ 132,19</b>", profit_style)]
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
    print("PDF 'Relatorio_Confeitaria_Julho.pdf' gerado com sucesso!")

if __name__ == "__main__":
    gerar_relatorio_pdf()