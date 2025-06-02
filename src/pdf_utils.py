from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY
import os


class PDFUtils:
    @staticmethod
    def gerar_pdf(caminho_pdf, caminho_excel, texto, dataframe=None):
        doc = SimpleDocTemplate(caminho_pdf, pagesize=A4)
        elementos = []
        styles = getSampleStyleSheet()

        nome_excel = os.path.basename(caminho_excel)
        nome_sem_ext = os.path.splitext(nome_excel)[0]
        nome_formatado = nome_sem_ext.replace("_", " ").title()

        elementos.append(Paragraph(nome_formatado, styles["Title"]))
        elementos.append(Spacer(1, 12))

        estilo_justificado = ParagraphStyle(
            "Justify", parent=styles["Normal"], alignment=TA_JUSTIFY
        )

        if texto:
            elementos.append(Paragraph(texto, estilo_justificado))
            elementos.append(Spacer(1, 12))

        if dataframe is not None:
            data = [list(dataframe.columns)] + dataframe.values.tolist()
            tabela = Table(data)
            estilo = TableStyle(
                [
                    ("GRID", (0, 0), (-1, -1), 1, colors.black),  # Bordas da tabela
                    (
                        "FONTNAME",
                        (0, 0),
                        (-1, 0),
                        "Helvetica-Bold",
                    ),  # Cabeçalho em Negrito
                ]
            )
            tabela.setStyle(estilo)
            elementos.append(tabela)

        doc.build(elementos)
