#1
'''def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)
for x in range(174457, 174506):
    d = div(x)
    if len(d) == 2: 
        print(d[0], d[1])'''

#2
'''def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)
for x in range(81234, 134690):
    d = div(x)
    if len(d) == 3: 
        print(d[0], d[1], d[2])'''

#3
'''def div(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)
for x in range(154026, 154044):
    d = div(x)
    if len(d) == 4: 
        print(d[-2], d[-1])'''

#4
'''s = 0
def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)
for x in range(150001, 150150):
    d = div(x)
    if len(d) > 0 and sum(d) % 13 == 10: 
        print(x, sum(d))'''

#5
'''def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)
for x in range(250201, 250301):
    d = div(x)
    if (max(d) + min(d)) % 123 == 17: 
        print(x, min(d) + max(d))'''

#6
'''f = 0
def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)
for x in range(550001, 550101):
    d = div(x)
    if d > 0 and (sum(d) / len(d)) % 31 == 13: 
        print(x, (sum(d) / len(d)))'''

#7
'''p = 0
def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)
for x in range(400000001, 400000100):
    d = div(x)
    if d >= 5 and d[0] * d[1] * d[2] * d[3] * d[4] % 100 == 17 and d[0] * d[1] * d[2] * d[3] * d[4]<= x: 
        print(d[0] * d[1] * d[2] * d[3] * d[4], d[4])'''