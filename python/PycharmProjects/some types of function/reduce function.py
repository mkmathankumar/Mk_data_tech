from functools import reduce

nums=[1,2,3,4]
total=reduce(lambda a,b: a+b,nums)
print(total)

number=[10,22,4,26]
maxi=reduce(lambda a,b:a if a>b else b,number)
print(maxi)