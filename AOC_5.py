Pass_list = open("Input_Day5.txt", "r")
Highest_ID = 0
IDs = []
LH = []
true = []
for row in Pass_list:
    Nums = 127
    Lowest = 0

    CS = 7
    CL = 0

    Row = 0
    Col = 0

    row = row.rstrip()
    Data_list = list(row)
    B = Data_list[:7]
    C = Data_list[7:]

    for i in range(3):
        Col_Bin = C[i]
        if (Col_Bin == "L"):
            if (i == 2):
                Col = CL
            else:
                CS = ((((CS - CL) + 1) / 2) - 1) + CL
        elif (Col_Bin == "R"):
            if (i == 2):
                Col = CS
            else:
                CL = (((CS - CL) + 1) / 2) + CL

    for X in range(7):
        Bin = B[X]
        if (Bin == "F"):
            if (X == 6):
                Row = Lowest
            else:
                Nums = ((((Nums - Lowest) + 1) / 2) - 1) + Lowest

        elif (Bin == "B"):
            if (X == 6):
                Row = Nums
            else:
                Lowest = (((Nums - Lowest) + 1) / 2) + Lowest

    ID = (Row * 8) + Col

    IDs.append(ID)
    if (ID > Highest_ID):
        Highest_ID = ID

for x in IDs:
    for y in range(len(IDs)):
        if (x + 2 == IDs[y]):

            LH.append(IDs[y] - 1)
        elif (x - 2 == IDs[y]):

            LH.append(x - 1)

for y in LH:

    if (y not in IDs):
        true.append(y)

print(true)
# print(Highest_ID)
# print(LH)