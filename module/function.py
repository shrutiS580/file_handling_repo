# num=[1,2,3,4,5,6]
# def sqr(n):
#     return n*n
# result=map(sqr,num)
# print(list(result))
# from functools import reduce
# num=[1,2,3,4,5]
# result=reduce(lambda a,b:a+b,num)
# print(result)
# result = list(map(lambda x:x*2,num))
# print(list(result))
# def even(n):
#     return n%2==0
# result=filter(even,num)
# print(list(result))
# Q1. Use map() to multiply every element of a list by 5.
from functools import reduce
num=[10,20,30,40,50,60,70,80,90,100,3]
# def mul(n):
#     return n*5
# result=map(mul,num)
# print(list(result))
# Q2. Use filter() to extract all numbers greater than 50 from a list of 10 numbers.
# def grat(n):
#     return n>50
# result=filter(grat,num)
# print(list(result))

# Q3. Given a list of numbers:
# - Use filter() to extract odd numbers.
# - Use map() to calculate their cubes.
# - Use reduce() to calculate the sum of cubes.
def odd(n):
    return n%2!=0
def cube(n):
    return n ** 3
    
result=filter(odd,num)
print(list(result))
result=map(cube,num)
print(list(result))
result=reduce(lambda a,b:a+b,num)
print(result)




