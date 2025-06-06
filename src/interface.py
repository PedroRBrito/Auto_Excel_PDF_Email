# flake8: noqa
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(592, 648)
        MainWindow.setStyleSheet(
            "/* === Global === */\n"
            "QMainWindow {\n"
            "    background-color: #FFFFFF;\n"
            "}\n"
            "\n"
            "QWidget {\n"
            '    font-family: "Segoe UI", Arial, sans-serif;\n'
            "    font-size: 13px;\n"
            "    color: #333333;\n"
            "}\n"
            "\n"
            "/* === Labels === */\n"
            "QLabel {\n"
            "    font-weight: normal;\n"
            "    color: #454545;\n"
            "    margin-bottom: 4px; \n"
            "}\n"
            "\n"
            "QLabel#label_SectionTitle { /* Para t\u00edtulos de se\u00e7\u00e3o, se voc\u00ea adicionar */\n"
            "    font-size: 15px;\n"
            "    font-weight: bold;\n"
            "    color: #007BFF;\n"
            "    margin-top: 10px;\n"
            "    margin-bottom: 6px;\n"
            "}\n"
            "\n"
            "/* === Campos de Entrada === */\n"
            "QLineEdit, QTextEdit {\n"
            "    background-color: #FFFFFF;\n"
            "    border: 1px solid #CED4DA;\n"
            "    border-radius: 5px;\n"
            "    padding: 10px;\n"
            "    font-size: 13px;\n"
            "    color: #495057;\n"
            "    selection-background-color: #007BFF;\n"
            "    selection-color: white;\n"
            "}\n"
            "\n"
            "QLineEdit:focus, QTextEdit:focus {\n"
            "    border: 1px solid #007BFF;\n"
            "}\n"
            "\n"
            "/* === Bot\u00f5es: Estilo Base"
            " === */\n"
            "QPushButton {\n"
            "    border-radius: 5px;\n"
            "    padding: 10px 20px; \n"
            "    font-size: 13px;\n"
            "    font-weight: 500; /* Um pouco menos que bold, mais moderno (normal, 500, bold) */\n"
            "    border: 1px solid transparent;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    opacity: 0.9;\n"
            "}\n"
            "\n"
            "QMessageBox QPushButton {\n"
            "    background-color: #007BFF;\n"
            "    color: white;\n"
            "    border-radius: 5px;\n"
            "    padding: 8px 16px;\n"
            "    font-weight: bold;\n"
            "}\n"
            "QMessageBox QPushButton:hover {\n"
            "    background-color: #0056B3;\n"
            "}\n"
            "\n"
            "/* === Bot\u00f5es Prim\u00e1rios (ex: Carregar, Enviar) === */\n"
            "QPushButton#pushButton_carregar_arquivo,\n"
            "QPushButton#pushButton_enviar_email {\n"
            "    background-color: #007BFF;\n"
            "    color: white;\n"
            "    border-color: #007BFF;\n"
            "}\n"
            "QPushButton#pushButton_carregar_arquivo:hover,\n"
            "QPushButton#pushButton_enviar_email:hover {\n"
            "    background-color: #0069D9;\n"
            "    border-color: #0062CC;\n"
            "}\n"
            "QPushButton#pushButton_carregar_arquivo:pressed,\n"
            "QPushButton#pushButton_enviar_email:pressed {\n"
            "    background-color: #0056B3;\n"
            "    border-color: #0056B3;\n"
            "}\n"
            "\n"
            "/* --- Botao Desabilitado (GENERICO) --- */\n"
            "QPushButton:disabled {\n"
            "    background-color: #d3d3d3;\n"
            "    color: #808080;\n"
            "    border: 1px solid #a9a9a9;\n"
            "    border-radius: 5px;\n"
            "    padding: 10px 20px;\n"
            "    font-size: 13px;\n"
            "    font-weight: 500;\n"
            "    font-style: italic;\n"
            "}\n"
            "\n"
            "/* --- Botao Desabilitado (ESPECIFICO para botoes primarios) --- */\n"
            "QPushButton#pushButton_carregar_arquivo:disabled,\n"
            "QPushButton#pushButton_enviar_email:disabled {\n"
            "    background-color: #b3d7ff; /* Um azul bem claro e desbotado */\n"
            "    color: #ffffff;\n"
            "    border-color: #a9cce3;\n"
            "    font-style: normal;\n"
            "}\n"
            "\n"
            "/* === Bot\u00e3o de Reset/Alerta (ex: Resetar) === */\n"
            "QPushButton#pushButton_resetar {\n"
            "    background-color"
            ": #F8F9FA;\n"
            "    color: #DC3545;\n"
            "    border: 1px solid #DC3545;\n"
            "}\n"
            "QPushButton#pushButton_resetar:hover {\n"
            "    background-color: #DC3545;\n"
            "    color: white;\n"
            "}\n"
            "QPushButton#pushButton_resetar:pressed {\n"
            "    background-color: #C82333;\n"
            "    color: white;\n"
            "    border-color: #C82333;\n"
            "}\n"
            "\n"
            "/* === Bot\u00f5es Secund\u00e1rios/Neutros (ex: Hist\u00f3rico, Fechar) === */\n"
            "QPushButton#pushButton_historico,\n"
            "QPushButton#pushButton_fechar {\n"
            "    background-color: #6C757D;\n"
            "    color: white;\n"
            "    border-color: #6C757D;\n"
            "}\n"
            "QPushButton#pushButton_historico:hover,\n"
            "QPushButton#pushButton_fechar:hover {\n"
            "    background-color: #5A6268;\n"
            "    border-color: #545B62;\n"
            "}\n"
            "QPushButton#pushButton_historico:pressed,\n"
            "QPushButton#pushButton_fechar:pressed {\n"
            "    background-color: #545B62;\n"
            "    border-color: #4E555B;\n"
            "}\n"
            "\n"
            "/* === Barra de Progresso === */\n"
            "QProgressBar {\n"
            "    border: 1px solid #CED4DA;\n"
            "    border-radius: 5px;\n"
            ""
            "    background-color: #E9ECEF;\n"
            "    text-align: center;\n"
            "    color: #495057;\n"
            "    height: 26px;\n"
            "    font-weight: 500;\n"
            "}\n"
            "\n"
            "QProgressBar::chunk {\n"
            "    background-color: #28A745;\n"
            "    border-radius: 4px; \n"
            "    margin: 2px;\n"
            "}"
        )
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_FileActions = QHBoxLayout()
        self.horizontalLayout_FileActions.setSpacing(10)
        self.horizontalLayout_FileActions.setObjectName("horizontalLayout_FileActions")
        self.label_nome_arquivo = QLabel(self.centralwidget)
        self.label_nome_arquivo.setObjectName("label_nome_arquivo")
        font = QFont()
        font.setFamily("Segoe UI")
        font.setBold(False)
        font.setWeight(50)
        self.label_nome_arquivo.setFont(font)

        self.horizontalLayout_FileActions.addWidget(self.label_nome_arquivo)

        self.pushButton_carregar_arquivo = QPushButton(self.centralwidget)
        self.pushButton_carregar_arquivo.setObjectName("pushButton_carregar_arquivo")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_carregar_arquivo.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_carregar_arquivo.setSizePolicy(sizePolicy)

        self.horizontalLayout_FileActions.addWidget(self.pushButton_carregar_arquivo)

        self.pushButton_resetar = QPushButton(self.centralwidget)
        self.pushButton_resetar.setObjectName("pushButton_resetar")
        sizePolicy.setHeightForWidth(
            self.pushButton_resetar.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_resetar.setSizePolicy(sizePolicy)

        self.horizontalLayout_FileActions.addWidget(self.pushButton_resetar)

        self.verticalLayout.addLayout(self.horizontalLayout_FileActions)

        self.label_relatorio = QLabel(self.centralwidget)
        self.label_relatorio.setObjectName("label_relatorio")
        self.label_relatorio.setFont(font)

        self.verticalLayout.addWidget(self.label_relatorio)

        self.textEdit_relatorio = QTextEdit(self.centralwidget)
        self.textEdit_relatorio.setObjectName("textEdit_relatorio")
        self.textEdit_relatorio.setMinimumSize(QSize(0, 120))

        self.verticalLayout.addWidget(self.textEdit_relatorio)

        self.label_detales_email = QLabel(self.centralwidget)
        self.label_detales_email.setObjectName("label_detales_email")
        self.label_detales_email.setFont(font)

        self.verticalLayout.addWidget(self.label_detales_email)

        self.formLayout_Email = QFormLayout()
        self.formLayout_Email.setObjectName("formLayout_Email")
        self.formLayout_Email.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.formLayout_Email.setHorizontalSpacing(10)
        self.formLayout_Email.setVerticalSpacing(10)
        self.label_destinatario_email = QLabel(self.centralwidget)
        self.label_destinatario_email.setObjectName("label_destinatario_email")

        self.formLayout_Email.setWidget(
            0, QFormLayout.LabelRole, self.label_destinatario_email
        )

        self.lineEdit_destinatario_email = QLineEdit(self.centralwidget)
        self.lineEdit_destinatario_email.setObjectName("lineEdit_destinatario_email")

        self.formLayout_Email.setWidget(
            0, QFormLayout.FieldRole, self.lineEdit_destinatario_email
        )

        self.label_titulo_email = QLabel(self.centralwidget)
        self.label_titulo_email.setObjectName("label_titulo_email")

        self.formLayout_Email.setWidget(
            1, QFormLayout.LabelRole, self.label_titulo_email
        )

        self.lineEdit_titulo_email = QLineEdit(self.centralwidget)
        self.lineEdit_titulo_email.setObjectName("lineEdit_titulo_email")

        self.formLayout_Email.setWidget(
            1, QFormLayout.FieldRole, self.lineEdit_titulo_email
        )

        self.label_corpo_email = QLabel(self.centralwidget)
        self.label_corpo_email.setObjectName("label_corpo_email")

        self.formLayout_Email.setWidget(
            2, QFormLayout.LabelRole, self.label_corpo_email
        )

        self.textEdit_corpo_email = QTextEdit(self.centralwidget)
        self.textEdit_corpo_email.setObjectName("textEdit_corpo_email")
        self.textEdit_corpo_email.setMinimumSize(QSize(0, 100))

        self.formLayout_Email.setWidget(
            2, QFormLayout.FieldRole, self.textEdit_corpo_email
        )

        self.verticalLayout.addLayout(self.formLayout_Email)

        self.horizontalLayout_BottomActions = QHBoxLayout()
        self.horizontalLayout_BottomActions.setSpacing(10)
        self.horizontalLayout_BottomActions.setObjectName(
            "horizontalLayout_BottomActions"
        )
        self.pushButton_historico = QPushButton(self.centralwidget)
        self.pushButton_historico.setObjectName("pushButton_historico")

        self.horizontalLayout_BottomActions.addWidget(self.pushButton_historico)

        self.pushButton_fechar = QPushButton(self.centralwidget)
        self.pushButton_fechar.setObjectName("pushButton_fechar")

        self.horizontalLayout_BottomActions.addWidget(self.pushButton_fechar)

        self.horizontalSpacer_BottomActions = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_BottomActions.addItem(self.horizontalSpacer_BottomActions)

        self.pushButton_enviar_email = QPushButton(self.centralwidget)
        self.pushButton_enviar_email.setObjectName("pushButton_enviar_email")
        self.pushButton_enviar_email.setAutoFillBackground(False)

        self.horizontalLayout_BottomActions.addWidget(self.pushButton_enviar_email)

        self.verticalLayout.addLayout(self.horizontalLayout_BottomActions)

        self.label_nome_etapa = QLabel(self.centralwidget)
        self.label_nome_etapa.setObjectName("label_nome_etapa")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.label_nome_etapa.sizePolicy().hasHeightForWidth()
        )
        self.label_nome_etapa.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.label_nome_etapa)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName("progressBar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(3)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy2)
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.progressBar)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate(
                "MainWindow", "Gerador de Relat\u00f3rios PDF", None
            )
        )
        self.label_nome_arquivo.setText(
            QCoreApplication.translate(
                "MainWindow", "1. Selecione o arquivo Excel para processar:", None
            )
        )
        self.pushButton_carregar_arquivo.setText(
            QCoreApplication.translate("MainWindow", "Carregar Arquivo", None)
        )
        self.pushButton_resetar.setText(
            QCoreApplication.translate("MainWindow", "Resetar", None)
        )
        self.label_relatorio.setText(
            QCoreApplication.translate(
                "MainWindow",
                "2. Escreva o texto principal do seu relat\u00f3rio (ser\u00e1 inclu\u00eddo no PDF):",
                None,
            )
        )
        self.label_detales_email.setText(
            QCoreApplication.translate(
                "MainWindow", "3. Detalhes para envio do e-mail:", None
            )
        )
        self.label_destinatario_email.setText(
            QCoreApplication.translate(
                "MainWindow", "E-mail do Destinat\u00e1rio:", None
            )
        )
        self.label_titulo_email.setText(
            QCoreApplication.translate("MainWindow", "T\u00edtulo do E-mail:", None)
        )
        self.label_corpo_email.setText(
            QCoreApplication.translate("MainWindow", "Corpo do E-mail:", None)
        )
        self.pushButton_historico.setText(
            QCoreApplication.translate("MainWindow", "Hist\u00f3rico", None)
        )
        self.pushButton_fechar.setText(
            QCoreApplication.translate("MainWindow", "Fechar", None)
        )
        self.pushButton_enviar_email.setText(
            QCoreApplication.translate("MainWindow", "Enviar E-mail com PDF", None)
        )
        self.label_nome_etapa.setText("")
        self.progressBar.setFormat(
            QCoreApplication.translate("MainWindow", "%p%", None)
        )

    # retranslateUi
