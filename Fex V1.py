# Modules importation
import os
import base64
try:
    from colorama import Fore, init
except:
    os.system("py -m pip install colorama")
    from colorama import Fore, init
init()

banner = (Fore.MAGENTA + """
 
███████╗███████╗██╗░░██╗  ██╗░░░██╗░░███╗░░
██╔════╝██╔════╝╚██╗██╔╝  ██║░░░██║░████║░░
█████╗░░█████╗░░░╚███╔╝░  ╚██╗░██╔╝██╔██║░░
██╔══╝░░██╔══╝░░░██╔██╗░  ░╚████╔╝░╚═╝██║░░
██║░░░░░███████╗██╔╝╚██╗  ░░╚██╔╝░░███████╗
╚═╝░░░░░╚══════╝╚═╝░░╚═╝  ░░░╚═╝░░░╚══════╝
""" + Fore.LIGHTCYAN_EX)
print(banner)
userid = input(" [INPUT] USERS ID : ")
encodedBytes = base64.b64encode(userid.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")
print(f'\n [LOGGED] TOKEN CAPTURE : {encodedStr}')
os.system('pause >nul')  # Pause command in Batch (Press Any Key To Exit)
