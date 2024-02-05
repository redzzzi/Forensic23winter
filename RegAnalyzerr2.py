# HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings
# proxy settings
#  AutoConfigURL
#   url
#  ProxyServer
#   여러개 있을때
#    http=0.0.9.91:80;https=0.0.9.92:80;ftp=0.0.9.93:80
#   하나있을때
#    0.0.9.91:80

import winreg as reg  
import os     

key = reg.HKEY_CURRENT_USER 
key_value = "Software\Microsoft\Windows\CurrentVersion\Internet Settings"

open = reg.OpenKey(key,key_value,0,reg.KEY_ALL_ACCESS)

value, type = reg.QueryValueEx(open,"User Agent")
print(value,"Type:",type)

try:
 value, type = reg.QueryValueEx(open,"AutoConfigURL")
 print("AutoConfigURL",value,"Type:",type)
except FileNotFoundError:
 print("AutoConfigURL not found")

try:
 value, type = reg.QueryValueEx(open,"ProxyServer")
 print("ProxyServer",value,"Type:",type)
except FileNotFoundError:
 print("ProxyServer not found")

# now close the opened key 
reg.CloseKey(open) 