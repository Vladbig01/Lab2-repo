# 1 Четные числа
a = int(input('Enter a: '))
b = int(input('Enter b: ')) + 1
[print(num, end=' ') for num in range(a, b) if a < b and num % 2 == 0]


# 2 Минимальный делитель
x = int(input())
y = 2
while y * y <= x:
    if x % y == 0:
        print(y)
        break
    y += 1
if y * y > x:
    print(x)


# 3 Делители числа
x = int(input('x = '))
for y in range(1, x + 1):
    if x % y == 0:
      print(y, end=' ')


# 4 Сумма чисел
n = int(input())
result = sum(int(input()) for i in range(n))
print(result)


# 5 Перевод числа
a = [[int(i) for i in input()], []]
for i in range(len(a[0]) - 1, -1, -1):
    a[1].append(2 ** i)
for i in range(len(a) + 1):
    if a[0][i] == 0:
        a[1][i] = 0
    else:
        a[1][i] = a[1][i] * 1
print(sum(a[1]))


# 6 Степень
def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)
a = int(input())
n = int(input())
print(power(a, n))







