from typing import Optional
from historico import HistoricoDB
from PySide2.QtWidgets import (
    QVBoxLayout,
    QMainWindow,
    QFileDialog,
    QMessageBox,
    QDialog,
    QTreeWidget,
    QTreeWidgetItem,
)
from PySide2.QtGui import QFont
from interface import Ui_MainWindow
from excel_utils import ExcelUtils
from pdf_utils import PDFUtils
from email_utils import EmailUtils
from dotenv import load_dotenv
import textwrap
import os

load_dotenv()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        HistoricoDB.inicializar()
        print(os.path.abspath(HistoricoDB.DB_PATH))
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.excel_file: Optional[str] = None

        # Botão de enviar e-mail desabilitado
        self.ui.pushButton_enviar_email.setEnabled(False)

        # Verificação de campos preenchidos
        self.ui.pushButton_enviar_email.clicked.connect(self.enviar_email)
        self.ui.lineEdit_destinatario_email.textChanged.connect(
            self.verificar_campos_obrigatorios
        )
        self.ui.lineEdit_titulo_email.textChanged.connect(
            self.verificar_campos_obrigatorios
        )

        # Conectar botões a funções
        self.ui.pushButton_carregar_arquivo.clicked.connect(self.carregar_arquivo_excel)
        self.ui.pushButton_historico.clicked.connect(self.historico)
        self.ui.pushButton_fechar.clicked.connect(self.fechar)
        self.ui.pushButton_resetar.clicked.connect(self.resetar_opcoes)
        print("Janela iniciada")

    def verificar_campos_obrigatorios(self):
        campos_preenchidos = (
            self.excel_file is not None
            and self.ui.lineEdit_destinatario_email.text().strip() != ""
            and self.ui.lineEdit_titulo_email.text().strip() != ""
        )
        self.ui.pushButton_enviar_email.setEnabled(bool(campos_preenchidos))

    def carregar_arquivo_excel(self) -> None:
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Carregar arquivo Excel",
            "",
            "Excel Files (*.xlsx);;All Files (*)",
            options=options,
        )
        if file_name:
            self.nome_arquivo_abv = os.path.basename(file_name)
            self.ui.label_nome_arquivo.setText(self.nome_arquivo_abv)
            self.excel_file = file_name
            self.verificar_campos_obrigatorios()
            print("arquivo carregado")

    def resetar_opcoes(self) -> None:
        resposta = QMessageBox.question(
            self,
            "Confirmar limpeza",
            "Deseja realmente limpar todos os campos?",
            QMessageBox.Yes | QMessageBox.No,
        )
        if resposta == QMessageBox.Yes:
            self.ui.label_nome_arquivo.setText(
                "1. Selecione o arquivo Excel para processar:"
            )
            self.excel_file = None
            self.ui.lineEdit_destinatario_email.clear()
            self.ui.lineEdit_titulo_email.clear()
            self.ui.textEdit_corpo_email.clear()
            self.ui.textEdit_relatorio.clear()
            self.ui.progressBar.setValue(0)
            print("reset concluido")

    def quebra_linhas(self, texto, tamanho=80) -> None:
        return "\n".join(textwrap.wrap(texto, width=tamanho))

    def historico(self) -> None:
        registros = HistoricoDB.listar()

        dialog = QDialog(self)
        dialog.setWindowTitle("Histórico de envios")
        layout = QVBoxLayout()

        tree = QTreeWidget()
        tree.setColumnCount(1)
        tree.setHeaderLabels(["Histórico"])
        tree.setVerticalScrollMode(QTreeWidget.ScrollPerPixel)
        tree.verticalScrollBar().setSingleStep(5)
        tree.setHorizontalScrollMode(QTreeWidget.ScrollPerPixel)

        font_filho_bold = QFont()
        font_filho_bold.setBold(True)
        font_pai_bold = QFont()
        font_pai_bold.setBold(True)
        font_pai_bold.setPointSize(10)

        for registro in registros:
            # Item pai: linha principal
            pai_texto = f"{registro['data_hora']} | {registro['destinatario']} | {registro['nome_pdf']}"
            item_pai = QTreeWidgetItem([pai_texto])
            item_pai.setFont(0, font_pai_bold)

            # Relatório do pdf
            filho1_titulo = QTreeWidgetItem(["Relatório do pdf:"])
            filho1_titulo.setFont(0, font_filho_bold)
            filho1_conteudo = QTreeWidgetItem(
                [self.quebra_linhas(registro["relatorio"], 60)]
            )

            # Título do e-mail
            filho2_titulo = QTreeWidgetItem(["Título do e-mail:"])
            filho2_titulo.setFont(0, font_filho_bold)
            filho2_conteudo = QTreeWidgetItem([registro["titulo_email"]])

            # Corpo do e-mail
            filho3_titulo = QTreeWidgetItem(["Corpo do e-mail:"])
            filho3_titulo.setFont(0, font_filho_bold)
            filho3_conteudo = QTreeWidgetItem(
                [self.quebra_linhas(registro["corpo"], 60)]
            )

            # Adiciona filhos ao pai
            item_pai.addChild(filho1_titulo)
            item_pai.addChild(filho1_conteudo)
            item_pai.addChild(filho2_titulo)
            item_pai.addChild(filho2_conteudo)
            item_pai.addChild(filho3_titulo)
            item_pai.addChild(filho3_conteudo)

            tree.addTopLevelItem(item_pai)

        layout.addWidget(tree)
        dialog.setLayout(layout)
        dialog.resize(700, 400)
        dialog.exec_()

    def enviar_email(self) -> None:
        try:
            # Ler o dataframe
            etapa_atual = "Leitura do arquivo Excel"
            df = ExcelUtils.ler_excel(self.excel_file)
            print(type(df))
            print("excel lido")
            self.ui.progressBar.setValue(10)

            # Pegar o texto do usuário
            etapa_atual = "Leitura do relatório do PDF"
            texto_usuario = self.ui.textEdit_relatorio.toPlainText()
            print("texto relatorio lido")
            self.ui.progressBar.setValue(20)

            # Gerar pdf
            etapa_atual = "Criação do PDF"
            nome_pdf = os.path.splitext(self.nome_arquivo_abv)[0] + ".pdf"
            caminho_pdf = os.path.join("../pdf", nome_pdf)
            os.makedirs(os.path.dirname(caminho_pdf), exist_ok=True)
            self.ui.progressBar.setValue(30)

            PDFUtils.gerar_pdf(caminho_pdf, self.excel_file, texto_usuario, df)
            print("pdf gerado")
            self.ui.progressBar.setValue(40)

            # Pegar dados do email
            etapa_atual = "Leitura de dados do e-mail"
            destinatario = self.ui.lineEdit_destinatario_email.text()
            titulo_email = self.ui.lineEdit_titulo_email.text()
            corpo = self.ui.textEdit_corpo_email.toPlainText()
            self.ui.progressBar.setValue(60)

            # Parametros do remetente
            etapa_atual = "Leitura de dados do remetente"
            remetente = os.getenv("EMAIL_REMETENTE")
            senha = os.getenv("SENHA_REMETENTE")
            smtp_server = "smtp.gmail.com"
            smtp_port = 587
            self.ui.progressBar.setValue(80)
            if not remetente:
                QMessageBox.critical(
                    self,
                    "Erro ao ler e-mail do remetente",
                    "Configure corretamente o e-mail do remetente",
                )
                self.ui.progressBar.setValue(0)
                return
            if not senha:
                QMessageBox.critical(
                    self,
                    "Erro ao ler senha do remetente",
                    "Configure corretamente a senha do remetente",
                )
                self.ui.progressBar.setValue(0)
                return

            # Enviar email com pdf em anexo
            etapa_atual = "Envio de e-mail"
            EmailUtils.enviar_email(
                destinatario,
                titulo_email,
                corpo,
                caminho_pdf,
                remetente,
                senha,
                smtp_server,
                smtp_port,
            )
            # print("email enviado!")
            self.ui.progressBar.setValue(100)

            HistoricoDB.salvar(
                destinatario, nome_pdf, texto_usuario, corpo, titulo_email
            )

            QMessageBox.information(
                self, "Status", f"E-mail enviado com sucesso para {destinatario}"
            )
        except Exception as e:
            QMessageBox.critical(
                self,
                "Erro crítico",
                f"Erro durante a etapa de: {etapa_atual}\n\nDetale: {e}",
            )
            self.ui.progressBar.setValue(0)
            return

    def fechar(self) -> None:
        self.close()
