from typing import Optional
from PySide2.QtWidgets import QMainWindow, QFileDialog
from interface import Ui_MainWindow
from excel_utils import ExcelUtils
from pdf_utils import PDFUtils
import excel_utils, pdf_utils, email_utils
import os

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


    def carregar_arquivo_excel(self) -> None:
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Carregar arquivo Excel", "", "Excel Files (*.xlsx);;All Files (*)", options=options)
        if file_name:
            self.nome_arquivo_abv = os.path.basename(file_name)
            self.ui.label_nome_arquivo.setText(self.nome_arquivo_abv)
            self.excel_file = file_name


    def resetar_opcoes(self):
        self.ui.label_nome_arquivo.setText("1. Selecione o arquivo Excel para processar:")
        

    def historico(self):
        pass

    def enviar_email(self):
        if not self.excel_file:
            print("Nenhum arquivo excel selecionado")
        df = ExcelUtils.ler_excel(self.excel_file)
        
        pass

    def fechar(self):
        self.close()