import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY
import os

def gerar_pdf(caminho_pdf, caminho_excel, texto, dataframe=None):
    doc = SimpleDocTemplate(caminho_pdf, pagesize=A4)
    elementos = []
    styles = getSampleStyleSheet()

    nome_excel = os.path.basename(caminho_excel)
    elementos.append(Paragraph(nome_excel, styles['Title']))
    elementos.append(Spacer(1,12))

    estilo_justificado = ParagraphStyle(
        'Justify',
        parent=styles['Normal'],
        alignment=TA_JUSTIFY
    )

    if texto:
        elementos.append(Paragraph(texto, estilo_justificado))
        elementos.append(Spacer(1, 12))

    if dataframe is not None:
        data = [list(dataframe.columns)] + dataframe.values.tolist()
        tabela = Table(data)
        estilo = TableStyle([
            ('GRID', (0,0), (-1,-1), 1, colors.black), #Bordas da tabela
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'), #Cabeçalho em Negrito
        ])
        tabela.setStyle(estilo)
        elementos.append(tabela)

    doc.build(elementos)

# DataFrame de teste
df = pd.DataFrame({
        "Nome": ["Xuxulinha", "Xuxulinho", "Porquinhos"],
        "Idade": [27, 27, 28],
        "Locomoção": ["Mini Cooper", "Mustang E-Tech", "Meia"]
    })
texto_usuario = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
caminho_excel = "Planilha Usuarios"
gerar_pdf("pdf/teste.pdf", caminho_excel, texto_usuario, df)