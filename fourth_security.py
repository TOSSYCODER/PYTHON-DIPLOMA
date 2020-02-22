from datetime import datetime as dt
import time
# today = dt.now()
# print(today)

# if (today > dt(dt.now().year,dt.now().month,dt.now().day)):
#     print("hai")
#     print(today)
# else:
#     print("nahi hai")

# print(dt(dt.now().year,dt.now().month,dt.now().day,dt.now().hour,dt.now().minute,dt.now().second))

# today = dt.now().hour
# h1 = 8
# h2 = 16

# if (today > h1 or today < h2):
#     print('hai')
# else:
#     print('nahi hai')

# print(dt(dt.now().year,dt.now().month,dt.now().day,10))

# today = dt.now()
# h1 = dt(dt.now().year,dt.now().month,dt.now().day,8)
# h2 = dt(dt.now().year,dt.now().month,dt.now().day,16)

# if (h1 < today < h2):
#     print('WORKING')
# else:
#     print('NON-WORKING')

temp_hosts = "hosts"
# today = dt.now()

h = '127.0.0.1'
website_list = ["www.facebook.com", "facebook.com"]
h1 = dt(dt.now().year,dt.now().month,dt.now().day,8)
h2 = dt(dt.now().year,dt.now().month,dt.now().day,15,46)

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
print(content)
time.sleep(1)
    # else:
    #     print('NON-WORKING', dt.now())
    #     w = []
    #     with open(temp_hosts, 'r+') as file:
    #         content = file.readlines()
    #         # print(content)
    #         for website in website_list:
    #             a = h + ' ' + website
    #             w.append(a)
    #             # print(a)
    #             # if(website in content):
    #         for j in w:
    #             for i in content:
    #                 # print(i)
    #                 # if(a in i):
    #                     # i =''
    #                 i = i.replace( j , ' ')
    #                 print(i)
    #             # print((content[24]))
                    
                    
    #     break
        # print(content)
    # time.sleep(1)    

