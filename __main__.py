import pypresence, requests, gd, os
try:
    percent = float(input("Enter the percent you want to deafen at:\n"))
except ValueError:
    print("Please enter a number!")
    exit(1)

def exchange_code(code):
    data = {
        'code': code
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    r = requests.post('https://zbot.figmentcoding.me/get_token', data=data, headers=headers) # Proxy server to not leak client secret
    r.raise_for_status()

    if (r.status_code != 200 or r.text == "-1"):
        return -1

    return r.text


try:
    memory = gd.memory.get_memory()
except RuntimeError:
    print("Geometry Dash is closed")
    exit(1)

c = pypresence.Client(836272609834434561)
c.start()

auth = c.authorize(836272609834434561, ["rpc"])
code = exchange_code(auth['data']['code'])

if (code == -1):
    print("Internal Server Error")
    exit(1)

c.authenticate(code)

def deafen():
    c.set_voice_settings(deaf=True)

def undeafen():
    c.set_voice_settings(deaf=False)


undeafen()
deafened = False;
os.system('cls');

while True:
    try:
        memory = gd.memory.get_memory()
    except RuntimeError:
        print("Geometry Dash was closed")
        exit(1)
    
    
    if (memory.get_percent() >= 100 or memory.get_percent() < percent or memory.is_dead()) and deafened:
        undeafen()
        deafened = False
    elif (memory.get_percent() >= percent and memory.get_percent() < 100) and not deafened:
        deafen()
        deafened = True



