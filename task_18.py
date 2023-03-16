#Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#*Пример:*
#5
#    1 2 3 4 5
#    6
#    -> 5
from random import randint
N = int(input("Input the number of elements in the array  "))
print (N)
list_1 = [randint(1, 10) for i in range(N)]
X = int(input ("Input the number you want to find the closest to in the array  "))
tempDifference = 0
minDifference = 0
result = 0
print (list_1)
for i in range (N):
    if list_1[i]>X:
        tempDifference = (list_1[i]-X)
        minDifference = list_1[i]
    else:
        tempDifference = (X-list_1[i])
        minDifference = list_1[i]
        if tempDifference<minDifference:
            minDifference = tempDifference
            result = list_1[i]
print (result)
