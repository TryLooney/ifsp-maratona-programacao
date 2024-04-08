from sys import stdin
data = [int(i) for i in stdin.read().split()]
print(f"PROD = {data[0]*data[1]}")