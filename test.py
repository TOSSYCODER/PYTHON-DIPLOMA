def maink(*p):
    sort = sorted(p)
    print(sort)

    def add():
        a = sum(sort)
        print(a)
    add()
    
maink(1,3,7,8,6)