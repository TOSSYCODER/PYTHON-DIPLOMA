class one():
    pass

class two():
    pass

class three():
    pass

class a (one,two):
    pass

class b (two, three):
    pass

class m (a,b,three):
    pass

# print(m())
# print(a())
# print(b())
# print(one())
# print(two())
# print(three())

#METHOD RESOLUTION ORDER

print(m.mro())      
print(a.mro())
print(b.mro())
print(one.mro())
print(two.mro())
print(three.mro())

key = (9,8,7,6)
k = str(list(key))
value = (1,2,3,4)
v = str(list(value))

dict = {'key': k, 'value': v}

print(dict)
