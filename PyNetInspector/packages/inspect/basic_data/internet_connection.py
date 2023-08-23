import requests


def check_internet_connection():
    url = "http://www.google.com"
    timeout = 5  # Temps d'attente en secondes pour la réponse

    try:
        response = requests.get(url, timeout=timeout)
        if response.status_code == 200:
            result = "Connecté"
            return result
    except requests.ConnectionError:
        pass
    return False
