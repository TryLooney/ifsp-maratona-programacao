from sys import stdin
data = [int(i) for i in stdin.read().split()]

menor = data[0] > data[1] and data[1] or data[0]
maior = data[0] > data[1] and data[0] or data[1]
ranging = data[0] - data[1]
values = []
if (ranging == 0):
    print(0)
    exit();
for i in range(menor, maior):
    if (i%2 != 0):
        values.append(i)

print(values[len(values)-1])