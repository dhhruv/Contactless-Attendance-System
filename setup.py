import sys 
import subprocess 
import os
# importing urllib.requests for internet cheking funtions 
import urllib.request 
  
# To check if the system is connected to the internet
def connect(host='https://google.com/'):
    try: 
        urllib.request.urlopen(host) 
        return True
    # trying to catch exception when internet is not ON. 
    except: 
        return False

def setup_a(module_name): 
  
    # updating pip to latest version 
    subprocess.run('python -m pip install --upgrade pip') 
  
    # commanding terminal to pip install required modules
    p = subprocess.run('python3 -m pip3 install '+module_name) 
    
    # Not connected to the internet
    if(p.returncode == 1 and connect() == False): 
        print("Error!! occured check\nInternet Conection.") 
  
    # Every thing worked fine 
    elif(p.returncode == 0): 
        print(module_name, " is installed successfully.") 
  
    # Name of module is wrong 
    elif(p.returncode == 1 and connect() == True): 
        print("Error!! occured check\nModule Name.") 

print('Installing')
print('Please wait....')
print('Do not close this program')
with open('requirements.txt') as file:
    data = file.readlines()
    for line in data:
        setup_a(line)
print('Installation finished')
subprocess.run('python3 main.py')#to run the main file