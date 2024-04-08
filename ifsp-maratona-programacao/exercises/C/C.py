from sys import stdin
from math import sqrt

data = [float(i) for i in stdin.read().split()]
print(f"{sqrt((data[2]-data[0])**2+(data[3]-data[1])**2):.4f}")