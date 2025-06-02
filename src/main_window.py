from typing import Optional
from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from interface import Ui_MainWindow
from excel_utils import ExcelUtils
from pdf_utils import PDFUtils
from email_utils import EmailUtils
from dotenv import load_dotenv
import os

load_dotenv()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.excel_file: Optional[str] = None

        # Conectar botões a funções
        self.ui.pushButton_historico.clicked.connect(self.historico)
        self.ui.pushButton_fechar.clicked.connect(self.fechar)
        self.ui.pushButton_enviar_email.clicked.connect(self.enviar_email)
        self.ui.pushButton_carregar_arquivo.clicked.connect(self.carregar_arquivo_excel)
        self.ui.pushButton_resetar.clicked.connect(self.resetar_opcoes)
        print("Janela iniciada")

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
            # self.nome_arquivo_completo = os.path(file_name)
            self.nome_arquivo_abv = os.path.basename(file_name)
            self.ui.label_nome_arquivo.setText(self.nome_arquivo_abv)
            self.excel_file = file_name
            print("arquivo carregado")

    def resetar_opcoes(self):
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

    def historico(self):
        pass

    def enviar_email(self):
        if not self.excel_file:
            print("Nenhum arquivo excel selecionado")

        # ler o dataframe
        df = ExcelUtils.ler_excel(self.excel_file)
        print(type(df))
        print("excel lido")
        self.ui.progressBar.setValue(10)

        # pegar o texto do usuário
        texto_usuario = self.ui.textEdit_relatorio.toPlainText()
        print("texto relatorio lido")
        self.ui.progressBar.setValue(20)

        # gerar pdf
        nome_pdf = os.path.splitext(self.nome_arquivo_abv)[0] + ".pdf"
        caminho_pdf = os.path.join("../pdf", nome_pdf)
        os.makedirs(os.path.dirname(caminho_pdf), exist_ok=True)
        self.ui.progressBar.setValue(30)

        PDFUtils.gerar_pdf(caminho_pdf, self.excel_file, texto_usuario, df)
        print("pdf gerado")
        self.ui.progressBar.setValue(40)

        # pegar dados do email
        destinatario = self.ui.lineEdit_destinatario_email.text()
        titulo_email = self.ui.lineEdit_titulo_email.text()
        corpo = self.ui.textEdit_corpo_email.toPlainText()
        self.ui.progressBar.setValue(60)

        # parametros do remetente
        remetente = os.getenv("EMAIL_REMETENTE")
        senha = os.getenv("SENHA_REMETENTE")
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        self.ui.progressBar.setValue(80)

        # enviar email com pdf em anexo
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
        print("email enviado!")
        self.ui.progressBar.setValue(100)

    def fechar(self):
        self.close()
