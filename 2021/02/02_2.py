"""
    Task	: 02_2
    Author	: Phumipat C. [MAGCARI]
    Language: Python
    Created	: 04 December 2021 [12:48]
    Algo	: 
    Status	: 
"""
x, y, aim = 0, 0, 0
with open('02.in', 'r') as f:
    data = f.read().splitlines()
    for i in data:
        cmd, num = i.split()
        if cmd == 'forward':
            x += int(num)
            y += int(num) * aim
        elif cmd == 'down':
            aim += int(num)
        elif cmd == 'up':
            aim -= int(num)

print(x*y)
