from sys import stdin
from math import sqrt

data = [float(i) for i in stdin.read().split()]
delta = data[1]**2-4*data[0]*data[2]
if (delta <= 0 or data[0] <= 0 or data[1] <= 0 or data[2] <= 0):
    print("Impossivel calcular")
    exit();

print(f'R1 = {(-data[1]+sqrt(delta))/(2*data[0]):.5f}')
print(f'R2 = {(-data[1]-sqrt(delta))/(2*data[0]):.5f}')