import socket

from .operator import get_operator_from_ip
from .internet_connection import check_internet_connection


def collect_basic_data():
    hostname = socket.gethostname()
    print("Nom d'hote:", hostname)

    ip_address = socket.gethostbyname(hostname)
    print("Adresse IP:", ip_address)

    operator = get_operator_from_ip()
    print("Operateur:", operator)

    internet_connection = check_internet_connection()
    print("Statut:", internet_connection)
