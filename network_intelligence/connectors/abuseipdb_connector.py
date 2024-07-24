import requests
from .base_connector import BaseConnector


class AbuseIPDBConnector(BaseConnector):
    def __init__(self, api_key):
        self.api_key = api_key

    def check_ip(self, ip):
        url = 'https://api.abuseipdb.com/api/v2/check'
        querystring = {'ipAddress': ip}
        headers = {
            'Accept': 'application/json',
            'Key': self.api_key
        }
        try:
            response = requests.get(url, headers=headers, params=querystring)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error checking IP {ip}: {e}")
            return None
