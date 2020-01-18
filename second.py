#IMPORTS
#
import functools
#
#DEFAULT FUNCTION
#
# def add(n1,n2=5):
    # s=n1+n2
    # return s 
# 
# print(add(7))
#
#TASK
# def purchasegreet(name, product):
    # print("HEY!" + name + ", THANKS FOR PURCHASING " + product)
# 
# name = input("ENTER NAME: ")
# product = input("ENTER PRODUCT YOU HAVE PURCHASED: ")
# 
# purchasegreet(name,product)
#
#CONDITIONAL STATEMENTS
#
# a = 5
# if(a == 5):
    # print("equal")
# else:
    # print("not equal")
#
# a = 5
# if(a < 10):
    # if(a > 5):
        # print("not greater than 5")
    # print("equal")
# else:
    # print("not equal")
#
#TASK
# def vote(name,age):
    # if(age < '18'):
        # print(name + " YOU ARE NOT ELIGIBLE TO VOTE!")
    # else:
        # print(name + " YOU ARE ELIGABLE TO VOTE!!")
# 
# name = input("ENTER YOUR NAME: ")
# age  = input("ENTER YOUR AGE: ")
# 
# vote(name,age)
#
#DEFAULT AND CONDITIONAL OPERATORS
#
# def div(num1, num2):
    # ans = num1/num2
    # return ans
# 
# print(div(num2 = 5, num1 = 10))
#
#ERROE!
# def div(num1, num2):
    # if(num1 < num2):
        # ans = num1/num2
    # else:
        # ans = num2/num1
    # return ans
# 
# n1 = input("ENTER FIRST NO.: ")
# n2 = input("ENTER SECOND NO: ")
# 
# print(div(n1,n2))
#
# m = input("ENTER MARKS: ")
# 
# def result (m):
    # if (m <= '29'):
        # print("FAIL!")
    # else:
        # print("PASS!")
# 
        # if(m >='90'):
            # print("YOU HAVE GOT A+ GRADE!")
        # elif(m <='80'):
            # print("YOU HAVE GOT B+ GRADE!")
        # elif(m <='70'):
            # print("YOU HAVE GOT C+ GRADE!")
        # elif(m <='60'):
            # print("YOU HAVE GOT D+ GRADE!")
        # else:
            # print("JUST PASSED!")
# 
# result(m)
#
# *args(any variable) FUNCTION //FORMS TUPLE
#
#def add(*n):
#    ans = sum(n)
#    print(ans)
#    print(n)
#
#add(1,2,3,4,5,6,7,8,9)
#
#ERROE!
#
# no = input("HOW MANY NOS. DO YOU WANTER TO ADD!? :")
# for i in range(0,no,1): 
    # n = input("ENTER NO.: ")
# 
# def add(*n):
    # ans = sum(n)
    # print(ans)
    # print(n)
# 
# add(n)
#
# **kwargs(any variable) FUNCTION //FORMS DICTIONARY
#
# n = input("ENTER YOUR NAME: ")
# a = input("ENTER AGE: ")
# b = input("ENTER D.O.B: ")
# def person(b,**kwn):
#    print("WELCOME " + kwn['name'] + "!")
#    print("DATE OF BIRTH IS: " + b)
#    print("YOU ARE " + kwn['age'] + " YEARS OLD")
#    print("LIST CONTENTS ARE: ")
#    for i in kwn['l']:
    #    print (i)
# 
# person(b, name = n, age = a, l = ['l1','l2'])
#
# in keyword
#
#TASK
#
# vowels = 'aeiou'
# def vow(**name):
    # for i in name['names']:
        # if (i[0] in vowels):
            # print(i)
# 
# vow(names = ['tauseef', 'adshcrt', 'endfy6yn'])
#
#TASK
# 
# vowels = 'aeiou'
# def vow(k):
    # if (k[0] in vowels):
        # print(k)
# 
# n = ['tauseef', 'adshcrt', 'endfy6yn']
# 
# list(map(vow,n))
# 
#FILTER
#
# def isEven(n):
    # if(n%2 == 0):
        # return True
    # else:
        # return False
# 
# a = [1,2,3,4,5,6,7,8,9]
# 
# print(list(filter(isEven,a)))
#
#LAMBDA FUNCTION
#
# def square(num):
    # ans = num*num
    # return ans
# 
# a = [1,2,3,4,5,6]
# print(list(map(square,a)))
#
# a = [1,2,3,4,5,6,7,8,9]
# print("LIST IS: ")
# print(a)
# print("SQUARE FOR GIVEN LIST IS: ")
# print(list(map(lambda s:s*s,a)))
# print("EVEN ELEMENTS IN LIST: ")
# print(list(filter(lambda s: True if(s%2 == 0) else False,a)))
#
#REDUCE
#
# lis = [ 1 , 3, 5, 6, 2, ] 
# print ("The sum of the list elements is : ",end="") 
# print (functools.reduce(lambda a,b : a+b,lis)) 
# 
# print ("The maximum element of the list is : ",end="") 
# print (functools.reduce(lambda a,b : a if a > b else b,lis)) 
#
