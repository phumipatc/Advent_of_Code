"""
    Task	: 02_1
    Author	: Phumipat C. [MAGCARI]
    Language: Python
    Created	: 04 December 2021 [12:46]
    Algo	: 
    Status	: 
"""
x, y = 0, 0
with open('02.in', 'r') as f:
    data = f.read().splitlines()
    for i in data:
        cmd, num = i.split()
        if cmd == 'forward':
            x += int(num)
        elif cmd == 'down':
            y += int(num)
        elif cmd == 'up':
            y -= int(num)
            y = max(y, 0)

print(x*y)
