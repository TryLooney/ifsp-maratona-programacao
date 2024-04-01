"""
8 3 169 169 1
0 3 5
"""

import sys
data = [int(i) for i in sys.stdin.read().split()]

bits_lenght = data[0]
initial_value = data[2]
value = data[2]
torneiras = data[5:len(data)]
binary = [int(i) for i in bin(value)[2::]]

numbers = []

while (not initial_value in numbers):
    print('a')
    while len(binary) < bits_lenght:
        binary.insert(0, 0)
    result = binary[7]
    for i in range(1, len(torneiras)):
        result = result ^ binary[7-torneiras[i]]

    binary_str = "".join([str(i) for i in binary])
    new_binary = str(result) + binary_str[0:7]
    binary = [int(j) for j in new_binary]
    value = int(new_binary, 2)
    numbers.append(value)

print(min(numbers))