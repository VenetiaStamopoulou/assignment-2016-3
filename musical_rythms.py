import argparse
import json
import sys

parser = argparse.ArgumentParser()

parser.add_argument("-s", type=int, help="SLOTS")
parser.add_argument("-p", type=int, help="PULSES")
parser.add_argument("-r", help="RECOGNISE")
parser.add_argument("-l", help="LIST_RYTHMS")

args = parser.parse_args()



g = []
p1 = args.p
s1 = args.s
r1 = args.r
l1 = args.l

m = s1 - p1

for i in range (0, p1):
    g.append([1])

for i in range (0, m):
    g.append([0])

y = len(g)

y1 = s1 % p1

for k in range (1, 10):
    if k == 1:
        while len(g[i]) == 1:
            for i in range (0, p1):
                if p1 < y:
                    g[i].append(0)
                    g.pop()
                    y = y - 1
                else:
                    break
            i = i + 1
    elif k > 1:
        for i in range (0, y1):
            if len(g[i]) == k:
                if y1 < y:
                    g[i].extend([1,0])
                    g.pop()
                    y = y - 1
                else:
                    break
u = []
for i in range (0, y1):
    u.extend(g[i])

x = 1
h = []
i = 0
while i <= len(u):
    for j in range (i, len(u)):
        if u[j] == 0:
            x = x + 1
            i = i + 1
        else:
            break
    i = i + 1
    h.append(x)
    x = 1
h.remove(1)

f = open('musical_rythms.json', 'r')
j = json.load(f)

results = 0
for k,value in j.items():
    if k == 'E('+str(p1)+','+str(s1)+')':
        results=value

f.close()

print ("E(",p1,",",s1,")=" ,[int("".join(str(x1) for x1 in u))],"=",[int("".join(str(x1) for x1 in h))], results)

if int(r1) == int("".join(str(x1) for x1 in u)):
    print ("E(",p1,",",s1,")=" ,[int("".join(str(x1) for x1 in u))],"=",[int("".join(str(x1) for x1 in h))], results)
else:
    print("Not a Euclidean rythm.")
