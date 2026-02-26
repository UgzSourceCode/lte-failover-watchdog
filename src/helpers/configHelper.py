import os
from dotenv import load_dotenv, find_dotenv

# =====================
# CONFIG
# =====================
def get_config():
    dotenv_path = find_dotenv()
    load_dotenv(dotenv_path)

    ROUTER_IP = os.getenv("ROUTER_IP")
    ROUTER_USER = os.getenv("ROUTER_USER")
    ROUTER_PASS = os.getenv("ROUTER_PASS")

    MAX_FAILURES = int(os.getenv("MAX_FAILURES", 3))
    STATE_FILE = os.getenv("STATE_FILE", "./state.json")

    SMTP_HOST = os.getenv("SMTP_HOST")
    SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
    SMTP_USER = os.getenv("SMTP_USER")
    SMTP_PASS = os.getenv("SMTP_PASS")
    EMAIL_FROM = os.getenv("EMAIL_FROM")
    EMAIL_TO = os.getenv("EMAIL_TO")

    return {
        "router_ip": ROUTER_IP,
        "router_user": ROUTER_USER,
        "router_pass": ROUTER_PASS,
        "max_failures": MAX_FAILURES,
        "state_file": STATE_FILE,
        "smtp_host": SMTP_HOST,
        "smtp_port": SMTP_PORT,
        "smtp_user": SMTP_USER,
        "smtp_pass": SMTP_PASS,
        "email_from": EMAIL_FROM,
        "email_to": EMAIL_TO,
    }