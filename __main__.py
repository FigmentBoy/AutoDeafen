import pypresence
import requests
import gd
import os

try:
    deaf_percent = float(input("Enter the percent you want to deafen at:\n"))
except ValueError:
    print("Please enter a number!")
    os.exit(1)


def exchange_code(code: int) -> str:
    data = {
        'code': code
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    # Proxy server to not leak client secret
    r = requests.post("https://zbot.figmentcoding.me/get_token",
                      data=data,
                      headers=headers)
    r.raise_for_status()

    if (r.status_code != 200 or r.text == "-1"):
        return -1

    return r.text


try:
    memory = gd.memory.get_memory()
except RuntimeError:
    print("Geometry Dash is closed")
    os.exit(1)

client = pypresence.Client(836272609834434561)
client.start()

auth = client.authorize(836272609834434561, ["rpc"])
code = exchange_code(auth['data']['code'])

if (code == -1):
    print("Internal Server Error")
    os.exit(1)

client.authenticate(code)

deafened = False


def deafen(deaf=True):  # shorthand for client.set_voice_settings
    deafened = deaf
    client.set_voice_settings(deaf=deaf)


deafen(False)
os.system("cls")

while True:
    try:
        memory = gd.memory.get_memory()
    except RuntimeError:
        print("Geometry Dash was closed")
        os.exit(1)

    percent = memory.get_percent()
    dead = memory.is_dead()

    if (percent >= 100 or percent < pdeaf_percent or dead) and deafened:
            deafen(False)
    elif (percent >= deaf_percent and percent < 100) and not deafened:
        deafen(True)
