from datetime import datetime as dt
import time
temp_hosts = "hosts"

h = '127.0.0.1'
w = []
website_list = ["www.facebook.com", "facebook.com"]
for website in website_list:
    a = h + ' ' + website + '\n'
    w.append(a)
# print(w)
h1 = dt(dt.now().year,dt.now().month,dt.now().day,8)
h2 = dt(dt.now().year,dt.now().month,dt.now().day,11,47)

while True:
    today = dt.now()
    if (h1 < today < h2):
        print('WORKING-TIME', dt.now())
        with open(temp_hosts, 'r+') as file:
            content = file.read()
            for website in website_list:
                if(website in content):
                    pass
                else:
                    file.write('\n' + h + ' ' + website + '\n')

    else:
        with open(temp_hosts, 'r+') as file:
            content = file.readlines()
            # print(content)
            # for j in range (0,(len(content))):
                # print(content[j])
            for i in range (0,(len(content))):
                # print(content[i])
                # for j in w:
                if content[i] == w[0]:
                    content[i] = content[i].replace(w[0] , ' ')
                elif content[i] == w[1]:
                    content[i] = content[i].replace(w[1], ' ')
                else:
                    pass
                print(content[i])
                # file.write()
                # print(i)
                # file.write()
        print('NON-WORKING', dt.now())
        # print(content)
        break
    time.sleep(1)
    