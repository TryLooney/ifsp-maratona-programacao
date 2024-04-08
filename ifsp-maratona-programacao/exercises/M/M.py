from sys import stdin
data = [int(i) for i in stdin.read().split()]
print((data[0]%data[1] == 0 or data[1]%data[0] == 0) and "Sao Multiplos" or "Nao sao Multiplos")