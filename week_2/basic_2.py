# Data type

i1 = 10
i2 = 99999999999999999999999
i3 = -10

f1 = 1.234
f2 = -5.678
f3 = .5
f4 = 10.

d = {
    'name': 'lgh',
    'age': 20
}


# Operator
print(1 + 2)
print(3 - 4)
print(5 * 6)
print(7 / 8)
print(9 % 10)
print(5 ** 2) # 5^2
a, b = divmod(100, 8)

x = 10
x += 1 # x++
x -= 1 # x--


# Type cast
print(1.5 + 2) # Float + Int => Float
print(bool(1)) # 0: False, Other: True
print(int(True))


# c:\programs\test\net.exe
print('c:\programs\test\net.exe')
print('c:\programs\\test\\net.exe') # Solved 1
print(r'c:\programs\test\net.exe') # Solved 2


# List slicing
idnum = '000509-1234567'
print(idnum[:6])
print(idnum[7])
print(idnum[::-1])


numbers = [i for i in range(1, 101)]
print(numbers)


# 1 ~ 100 Sum
sum_1 = 0
i = 1
while i <= 100:
    sum_1 += i
    i += 1

sum_2 = 0
for i in range(1, 101):
    sum_2 += i

print(sum_1, sum_2, sum(range(1, 101)))


# 대문자 <-> 소문자
name = 'JohN'
for c in name:
    if c.isupper():
        print(c.lower(), end='')
    else:
        print(c.upper(), end='')
