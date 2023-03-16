#Задача 16: Требуется вычислить, сколько раз встречается некоторое число X 
#в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N 
#– количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. 
#Последняя строка содержит число X
#*Пример:*
#5
#    1 2 3 4 5
#    3
#    -> 1
from random import randint
N = int(input("Input the number of elements in the array  "))
print (N)
list_1 = [randint(1, 10) for i in range(N)]
print (list_1)
X = int(input ("Input the number you want to find in the array  "))
print (X)
countNumberX = 0
for i in range (N):
    if list_1[i]==X:
        countNumberX+=1
print ("Number",N,"can be found",countNumberX,"times")
