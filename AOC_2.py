myFile = open("My_Input.txt", "r")
num_good_pass = 0

for row in myFile:
    feild = row.split(" ")
    range_of_letter = list(map(int, feild[0].split("-")))
    letter_1st = list(feild[1])
    letter = letter_1st[0]

    password = list(feild[2])
    count = 0

    i1 = range_of_letter[0] - 1
    i2 = range_of_letter[1] - 1
    if (password[i1] == letter and password[i2] != letter or password[i1] != letter and password[i2] == letter):
        num_good_pass = num_good_pass + 1

print("Number of good passwords", num_good_pass)