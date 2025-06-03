import sqlite3
import os
from typing import List, Tuple
from datetime import datetime


class HistoricoDB:
    DB_PATH = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "data", "historico.db")
    )

    @staticmethod
    def inicializar() -> None:
        os.makedirs(os.path.dirname(HistoricoDB.DB_PATH), exist_ok=True)
        conn = sqlite3.connect(HistoricoDB.DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS historico (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data_hora TEXT,
                nome_pdf TEXT,
                relatorio TEXT,
                destinatario TEXT,
                titulo_email TEXT,
                corpo TEXT
            )
        """
        )
        conn.commit()
        conn.close()

    @staticmethod
    def salvar(destinatario, nome_pdf, relatorio, corpo, titulo_email) -> None:
        conn = sqlite3.connect(HistoricoDB.DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO historico (data_hora, nome_pdf, relatorio, destinatario, titulo_email, corpo)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                nome_pdf,
                relatorio,
                destinatario,
                titulo_email,
                corpo,
            ),
        )
        conn.commit()
        conn.close()

    @staticmethod
    def listar() -> List[Tuple[str, str, str, str, str, str]]:
        conn = sqlite3.connect(HistoricoDB.DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(
            "SELECT data_hora, nome_pdf, relatorio, destinatario, titulo_email, corpo FROM historico ORDER BY id DESC"
        )
        registros = cursor.fetchall()
        conn.close()
        return registros

    # @staticmethod
    # def limpar() -> None:
    #     conn = sqlite3.connect(HistoricoDB.DB_PATH)
    #     cursor = conn.cursor()
    #     cursor.execute("DELETE FROM historico")
    #     conn.commit()
    #     conn.close()
