import requests


def get_operator_from_ip():
    try:
        response = requests.get("http://ipinfo.io/json")
        if response.status_code == 200:
            data = response.json()
            operator = data.get("org", "Opérateur inconnu")
            return operator
        else:
            return "Opérateur inconnu"
    except requests.ConnectionError:
        return "Impossible de récupérer l'opérateur"
