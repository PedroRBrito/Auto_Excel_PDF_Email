from PySide2.QtWidgets import QMainWindow, QFileDialog
from interface import Ui_MainWindow
import excel_utils, pdf_utils, email_utils

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
        # Conectar botões a funções
        self.ui.pushButton_historico.clicked.connect(self.historico)
        self.ui.pushButton_fechar.clicked.connect(self.fechar)
        self.ui.pushButton_enviar_email.clicked.connect(self.enviar_email)
        self.ui.pushButton_carregar_arquivo.clicked.connect(self.carregar_arquivo_excel)
        self.ui.pushButton_resetar.clicked.connect(self.resetar_opcoes)


    def carregar_arquivo_excel(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Carregar arquivo Excel", "", "Excel Files (*.xlsx);;All Files (*)", options=options)
        if file_name:
            self.ui.label_nome_arquivo.setText(file_name)
            self.excel_file = file_name
            self.process_excel_file(file_name)

    def resetar_opcoes(self):
        pass

    def historico(self):
        pass

    def fechar(self):
        pass

    def enviar_email(self):
        pass