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
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(484, 528)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_arquivo_excel = QLabel(self.layoutWidget)
        self.label_arquivo_excel.setObjectName(u"label_arquivo_excel")

        self.verticalLayout.addWidget(self.label_arquivo_excel)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_carregar_arquivo = QPushButton(self.layoutWidget)
        self.pushButton_carregar_arquivo.setObjectName(u"pushButton_carregar_arquivo")

        self.horizontalLayout_2.addWidget(self.pushButton_carregar_arquivo)

        self.label_nome_arquivo = QLabel(self.layoutWidget)
        self.label_nome_arquivo.setObjectName(u"label_nome_arquivo")

        self.horizontalLayout_2.addWidget(self.label_nome_arquivo)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.splitter.addWidget(self.layoutWidget)
        self.pushButton_resetar = QPushButton(self.splitter)
        self.pushButton_resetar.setObjectName(u"pushButton_resetar")
        self.pushButton_resetar.setEnabled(True)
        self.pushButton_resetar.setCursor(QCursor(Qt.ArrowCursor))
        self.pushButton_resetar.setAcceptDrops(False)
        self.pushButton_resetar.setToolTipDuration(-1)
        self.pushButton_resetar.setAutoFillBackground(False)
        self.pushButton_resetar.setAutoDefault(False)
        self.pushButton_resetar.setFlat(False)
        self.splitter.addWidget(self.pushButton_resetar)

        self.verticalLayout_7.addWidget(self.splitter)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_relatorio = QLabel(self.centralwidget)
        self.label_relatorio.setObjectName(u"label_relatorio")

        self.verticalLayout_2.addWidget(self.label_relatorio)

        self.textEdit_relatorio = QTextEdit(self.centralwidget)
        self.textEdit_relatorio.setObjectName(u"textEdit_relatorio")

        self.verticalLayout_2.addWidget(self.textEdit_relatorio)


        self.verticalLayout_7.addLayout(self.verticalLayout_2)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_destinatario = QLabel(self.centralwidget)
        self.label_destinatario.setObjectName(u"label_destinatario")

        self.verticalLayout_3.addWidget(self.label_destinatario)

        self.lineEdit_destinatario = QLineEdit(self.centralwidget)
        self.lineEdit_destinatario.setObjectName(u"lineEdit_destinatario")

        self.verticalLayout_3.addWidget(self.lineEdit_destinatario)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_destinatario_2 = QLabel(self.centralwidget)
        self.label_destinatario_2.setObjectName(u"label_destinatario_2")

        self.verticalLayout_5.addWidget(self.label_destinatario_2)

        self.lineEdit_destinatario_2 = QLineEdit(self.centralwidget)
        self.lineEdit_destinatario_2.setObjectName(u"lineEdit_destinatario_2")

        self.verticalLayout_5.addWidget(self.lineEdit_destinatario_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_destinatario_3 = QLabel(self.centralwidget)
        self.label_destinatario_3.setObjectName(u"label_destinatario_3")

        self.verticalLayout_4.addWidget(self.label_destinatario_3)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_4.addWidget(self.textEdit)


        self.verticalLayout_7.addLayout(self.verticalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_historico = QPushButton(self.centralwidget)
        self.pushButton_historico.setObjectName(u"pushButton_historico")

        self.horizontalLayout.addWidget(self.pushButton_historico)

        self.pushButton_fechar = QPushButton(self.centralwidget)
        self.pushButton_fechar.setObjectName(u"pushButton_fechar")
        self.pushButton_fechar.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout.addWidget(self.pushButton_fechar)

        self.pushButton_enviar_email = QPushButton(self.centralwidget)
        self.pushButton_enviar_email.setObjectName(u"pushButton_enviar_email")

        self.horizontalLayout.addWidget(self.pushButton_enviar_email)


        self.verticalLayout_7.addLayout(self.horizontalLayout)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.progressBar_envio = QProgressBar(self.centralwidget)
        self.progressBar_envio.setObjectName(u"progressBar_envio")
        self.progressBar_envio.setValue(0)
        self.progressBar_envio.setOrientation(Qt.Horizontal)
        self.progressBar_envio.setInvertedAppearance(False)

        self.verticalLayout_6.addWidget(self.progressBar_envio)

        self.label_nome_etapa = QLabel(self.centralwidget)
        self.label_nome_etapa.setObjectName(u"label_nome_etapa")
        self.label_nome_etapa.setTextFormat(Qt.PlainText)
        self.label_nome_etapa.setScaledContents(False)
        self.label_nome_etapa.setWordWrap(False)
        self.label_nome_etapa.setIndent(0)

        self.verticalLayout_6.addWidget(self.label_nome_etapa)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setSizeGripEnabled(True)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.pushButton_resetar.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_arquivo_excel.setText(QCoreApplication.translate("MainWindow", u"Carregue o arquivo excel:", None))
        self.pushButton_carregar_arquivo.setText(QCoreApplication.translate("MainWindow", u"Carregar Arquivo", None))
        self.label_nome_arquivo.setText(QCoreApplication.translate("MainWindow", u"\"Nome do arquivo aqui\"", None))
#if QT_CONFIG(tooltip)
        self.pushButton_resetar.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton_resetar.setText(QCoreApplication.translate("MainWindow", u"Resetar", None))
        self.label_relatorio.setText(QCoreApplication.translate("MainWindow", u"Escreva o texto do seu relat\u00f3rio aqui:", None))
        self.label_destinatario.setText(QCoreApplication.translate("MainWindow", u"Escreva o e-mail do destinat\u00e1rio:", None))
        self.label_destinatario_2.setText(QCoreApplication.translate("MainWindow", u"Escreva o t\u00edtulo do e-mail:", None))
        self.label_destinatario_3.setText(QCoreApplication.translate("MainWindow", u"Escreva o corpo do e-mail:", None))
        self.pushButton_historico.setText(QCoreApplication.translate("MainWindow", u"Hist\u00f3rico", None))
        self.pushButton_fechar.setText(QCoreApplication.translate("MainWindow", u"Fechar", None))
        self.pushButton_enviar_email.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.label_nome_etapa.setText(QCoreApplication.translate("MainWindow", u"Nome da Etapa", None))
    # retranslateUi

