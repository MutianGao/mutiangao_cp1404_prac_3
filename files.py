# Q1
out_file = open("name.txt", "w")
name = input("What is your name?: ")
print(name, file=out_file)
out_file.close()

# Q2
in_file = open("name.txt", "r")
name = in_file.read().strip()
print("Your name is", name)
in_file.close()

# Q3
in_file = open("numbers.txt", "r")
num1 = int(in_file.readline())
num2 = int(in_file.readline())
in_file.close()
print(num1 + num2)

# Q4
in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total = total + number
print(total)
in_file.close()
