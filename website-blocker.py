import time
from datetime import datetime as dt
#this is a mock file
host_temp = "hosts"
#this is the real file to make this program work
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "www.instagram.com", "instagram.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, ):
        try:
            with open(host_temp, 'r+') as file:
                content = file.read()
                for website in website_list:
                    if website in content:
                        pass
                    else:
                        file.write("\n" +redirect + "   " + website)
        except FileNotFoundError as ex:
            print(ex)
        
    else:
        try:
            with open(host_temp, 'r+') as file:
                content = file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in website_list):
                        file.write(line)
                file.truncate()
        except FileNotFoundError as ex:
            print(ex)
    time.sleep(3)
    