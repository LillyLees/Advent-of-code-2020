from nltk import flatten

Ans_Data = open("Input_Day6.txt", "r")
Ans = 0
N = list(Ans_Data)
Nested = []
nest = []

for i in range(len(N)):
    if (N[i] == "\n"):
        Nested.append(nest)
        nest = []
    elif (i == (len(N) - 1)):
        nest.append(N[i])
        Nested.append(nest)
        nest = []
    else:
        nest.append(N[i])

for x in Nested:
    smol = []
    for y in x:
        y = y.strip()
        z = list(y)
        smol.append(z)

    if (len(smol) == 1):
        Ans = Ans + len(smol[0])
    else:
        count = len(smol)
        temp = flatten(smol)
        PP = list(dict.fromkeys(temp))
        for k in PP:
            VV = temp.count(k)
            if (VV == count):
                Ans = Ans + 1
print(Ans)
