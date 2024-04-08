from sys import stdin
data = [float(i) for i in stdin.read().split()]
print(f"MEDIA = {(((data[0]*3.5) + (data[1]*7.5))/11):.5f}")