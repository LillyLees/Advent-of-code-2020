Data = open("numbers.txt","r")
List_Data = list(Data)
num = 0
tick = 24
for i in range(len(List_Data)):
  sub_List = []
  z = i+25
  if(i == (len(List_Data)-24)):
    break
  else:
    for x in range(i, z):
       sub_List.append(List_Data[x])
  Testing_Dig = int(List_Data[i+25])
  passes = 0
  for x in sub_List:
    x = int(x.strip())
    for y in sub_List:
      y = int(y.strip())
      if(x + y == Testing_Dig and x != y):
        passes = passes + 1
  if(passes == 0):
    num = Testing_Dig
    break

for x in range(len(List_Data)):
    Range_of = []
    S_Num = int(List_Data[x])
    sum_of_n = S_Num
    Range_of.append(S_Num)
    for z in range(x+1,len(List_Data)):
      z = int(List_Data[z].strip())
      Range_of.append(z)
      S_Num = S_Num + z
      if(S_Num == Testing_Dig):
        print(Range_of[0] + Range_of[len(Range_of)-1])
        break
