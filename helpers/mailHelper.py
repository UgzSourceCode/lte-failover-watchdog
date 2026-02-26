import smtplib
import ssl
from email.message import EmailMessage

# =====================
# EMAIL
# =====================
def send_email(subject, body, config):
    msg = EmailMessage()
    msg["From"] = config["email_from"]
    msg["To"] = config["email_to"]
    msg["Subject"] = subject
    msg.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP(config["smtp_host"], config["smtp_port"]) as server:
        server.starttls(context=context)
        server.login(config["smtp_user"], config["smtp_pass"])
        server.send_message(msg)