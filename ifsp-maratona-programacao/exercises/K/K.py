from sys import stdin
data = [float(i) for i in stdin.read().split()]
print(f"MEDIA = {(((data[0]*2) + (data[1]*3) + (data[2]*5))/10):.1f}")