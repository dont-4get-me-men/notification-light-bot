import os 

def try_ping(ip_adress: str):
    response = os.system('ping -c 1 '+ ip)

    if response == 0:
        return True
    else:
        return False
