# # принимает число N  и выводит последовательность из N  членов

# # 5:
# import random
# n= int(input('Введите число: '))
# for i in range(n):
#     print(random.randrange(-100,100),end=", ")

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Для натуральног числа н создать индекс-значениеб состоявший из элементов 3н+1
n=int(input("Введите натуральное число"))
d={a:(3*a+1) for a in range(1,n+1)}

print(d)








#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Напишите программу, в которой пользовать вводит две строки, а программа определяет колличесво вхождений строки в другой

# line1=input()
# line2=input()

# temp1=line1.split()
# temp2= line2.split()

# count=0

# for i in range(len(temp1)):
#     if temp1[i] in temp2:
#         count+=1
        
# print(count)        