from sys import stdin
data = [int(i) for i in stdin.read().split()]
print(f"DIFERENCA = {data[0] * data[1] - data[2] * data[3]}")