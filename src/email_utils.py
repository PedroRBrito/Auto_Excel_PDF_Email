import smtplib
from email.message import EmailMessage
import os


class EmailUtils:
    @staticmethod
    def enviar_email(
        destinatario,
        titulo,
        corpo,
        caminho_pdf,
        remetente,
        senha,
        smtp_server,
        smtp_port=587,
    ):
        msg = EmailMessage()
        msg["From"] = remetente
        msg["To"] = destinatario
        msg["Subject"] = titulo
        msg.set_content(corpo)

        if caminho_pdf and os.path.exists(caminho_pdf):
            with open(caminho_pdf, "rb") as f:
                pdf_data = f.read()
            msg.add_attachment(
                pdf_data,
                maintype="application",
                subtype="pdf",
                filename=os.path.basename(caminho_pdf),
            )

        with smtplib.SMTP(smtp_server, smtp_port) as smtp:
            smtp.starttls()
            smtp.login(remetente, senha)
            smtp.send_message(msg)
