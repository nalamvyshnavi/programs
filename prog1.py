import os,ipaddress
os.system('cls')
while True:
    ip=input('enter ip address:')
    try:
        print(ipaddress.ip_address(ip))
        print('IP Valid')
    except:
        print('-'*50)
        print('IP is not vaild')
    finally:
        if ip=='mango':
            print('script finished')
            break