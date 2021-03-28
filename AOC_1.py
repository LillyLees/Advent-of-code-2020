Map = open("Input_Day1.txt", "r")

Nums = []

for row in Map:
    row = row.rstrip()
    Nums.append(row)

Map.close()

print(Nums)
length = len(Nums)
for i in range(length):
    x = int(Nums[i])
    for y in range(length):
        z = int(Nums[y])
        for d in range(length):
            p = int(Nums[d])
            if (z + x + p == 2020):
                print(z, "+", x, "+", p, "= 2020")
                print("Sum = ", z * x * p)

