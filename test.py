import requests;

URL = 'https://github.com/afsal-p-u/'
password_list = "rockyou.txt"
extention = ['','.php','.html','.js']

with open(password_list, 'rb') as file:
        for line in file:
            for word in line.split():
                for ext in extention:
                    print(word.decode())
                    data = requests.get(URL + word.decode()+ext)
                    if data.status_code == 200:
                        print("found ", data.status_code, " ", "/"+word.decode()+ext)