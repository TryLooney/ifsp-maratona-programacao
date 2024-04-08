from sys import stdin
data = [float(i) for i in stdin.read().split()]
if (data[0] >= (data[1] + data[2]) or data[1] >= (data[0] + data[2]) or data[2] >= (data[0] + data[1])):
    print(f"Area = {((data[0] + data[1])*data[2]/2):.1f}")
    exit()

print(f"Perimetro = {(data[0] + data[1] + data[2]):.1f}")