print("Введите числа через пробел: ")
a = [int(i) for i in input().split()]
print("Последовательность неповторяющихся элементов: ")
for i in range(len(a)):
   flag = 1
   for j in range(len(a)):
      if a[i] == a[j] and i != j:
         flag = 0
         break
   if flag:
      print(a[i], end = " ")