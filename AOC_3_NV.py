Map = open("Input_Day3.txt","r")
Trees = 0
place = 0
tick = 0
rows = -1
for row in Map:
  row = row.rstrip()
  rows = rows + 1
  if(rows % 2 == 0):
   if(tick == 0):
    tick = tick + 1

   else:
     place = place + 1
     if(place > 30):
         place = 0
         Row_1 = list(row)
         for i in range(0,31):
              if( i == place and  Row_1[place] == "#"):
                     Trees = Trees + 1
     else:
      Row_1 = list(row)
      for i in range(0,31):
           if( i == place and Row_1[place] == "#"):
                 Trees = Trees + 1

print("Number of Trees",Trees)