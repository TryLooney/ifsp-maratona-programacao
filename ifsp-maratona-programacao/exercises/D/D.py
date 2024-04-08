from sys import stdin

# // número inteiro da divisão
# % resto da divisão

data = int(stdin.read())
print(f"{data//365} ano(s)\n{(data%365)//30} mes(es)\n{((data%365)%30)} dia(s)")