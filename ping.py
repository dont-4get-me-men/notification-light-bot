import os
import random
import time


def is_ping_available(ip_adress: str):
    response = os.system('ping -c 1 ' + ip_adress)
    if response == 0:
        return True
    else:
        return False


class AccessibilityCheck:
    def __init__(self, bot, id, wait_time=120):
        self._wait_time = wait_time
        self.__bot = bot
        self.__id = id

    async def checking(self, ip):
        res = is_ping_available(ip)

        while True:
            new_res = is_ping_available(ip)
            print(new_res)
            if new_res != res:
                if new_res:
                    await self.__bot.send_message(self.__id, "there is electricity")
                else:
                    await self.__bot.send_message(self.__id, "there is no electricity")
                res = new_res
            time.sleep(self._wait_time)
