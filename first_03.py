from array import *

print("-------------------- LIST ---------------------")

print("")

l = [12,23,-10,3.5,'PYTHON','CO']
print("PRINTING ORIGINAL LIST: ", l)
print("PRINTING FIRST THREE ELEMENTS OF A LIST: ",l[0:3])
print("PRINTING LAST ELEMENTS OF A LIST: ",l[-1])
print("PRINTING FIRST THREE ELEMENTS OF A LIST TWICE: ",l[0:3]*2)

print("")

print("-------------------- LIST FUNCTION -------------------- ")

print("")

l1 = list(range(1,8))
print("LIST OF RANGE 1 TO 7: ", l1)
l1.append(9)
print("APPEND 9: ",l1)
l1.sort(reverse = True)
print("DESCENDING SORT: ",l1)
l1.sort()
print("ASCENDING SORT: ",l1)
l1.reverse()
print("REVERSE: ",l1)
l1.sort()
l1.remove(9)
print("REMOVE 9: ",l1)
print("COUNT: ",l1.count(5))
print("MAX: ",max(l1))
print("MIN: ",min(l1))
print("INDEX OF 6: ",l1.index(6))

print("")

print("-------------------- MATRICES USING LISTS -------------------- ")

print("")

m1 = [[1,2,3],[4,5,6],[7,8,9]]
for r in m1:
    print(r)

print("")

print("-------------------- TUPLE DATA-TYPE -------------------- ")

print("")

tpl1 = (-3.5,10,20,'PYTHON','B-3')
print("CREATED TUPLE IS: ",tpl1)
print("TUPLE ELEMENTS 0 TO 2 IS: ",tpl1[0:2])

print("")

print("-------------------- TUPLE FUNCTION -------------------- ")

print("")

tpl2 = (3,5,6,9,4,8,5,9,5,9,1,2)
print("LENGTH: ",len(tpl2))
print("MIN: ",min(tpl2))
print("MAX: ",max(tpl2))
print("COUNT NOS. OF 5: ",tpl2.count(9))
print("REVERSE SORT: ",sorted(tpl2,reverse=True))

print("")

print("-------------------- DICTIONARIES i.e. KEY:VALUE PAIR -------------------- ")

print("")

d1 = {'NAME':"TAUSEEF",'GENDER':"MALE",'AGE':19,'COLLEGE':"AIKTC"}
print("PRINT DICTIONARY: ",d1)

print("")

print("--> KEYS: ",d1.keys())
print("--> values: ",d1.values())
print("--> KEYS & VALUES: ",d1.items())
d1.update({'COUNTRY':"INDIA"})
print("--> UPDATED DICTIONARY: ", d1)

print("")

print("-------------------- ARRAYS -------------------- ")

print("")

arr = array('i',[10,20,30,40,50])
print("THE ARRAY ELEMENTS ARE: ")
for i in arr:
    print(i)
print("LENGTH OF ARRAY IS: ",len(arr))

arrr = array('u',['a','b','c','d','e','f'])
for ch in arrr:
    print(ch)