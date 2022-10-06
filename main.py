grade = int(input("Enter the grade: "))

if grade > 90:
    print(f"Congratulations your grade of {grade} earns you an A in this course")


o = int(input("Enter the hourly wage: "))
p = int(input("Enter the percentage increase or decrease: "))
n = int(input("Enter the number of years: "))

w = o * ((1 + p) ** n)

print(w)

days = 1
value = 0
total = 0
largest = 0

while days <= 7:
    value = int(input(f"Enter value for day {days}: "))
    days += 1
    total += value

    if value > largest:
        largest = value

average = total / days

print(f"The total of the values is {total},\n"
      f"the average of the values is {average},\n"
      f"the smallest value is {smallest},\n"
      f"the largest value is {largest}.")


q1 = input("What is your problem? ")
q2 = input("Have you had this problem before (yes or no)?").strip()

if q2 == "yes":
    print("Well, you have it again.")
else:
    print("Well, you have it now.")


age = int(input("Please enter your age in years: "))
max_heart_rate = 220 - age

print("Your target heart rate is: ")
target_heart_rate1 =  max_heart_rate * (50/100)
target_heart_rate2 = max_heart_rate * (85/100)

print(f"{target_heart_rate1} - {target_heart_rate2}")


angle1 = int(input("Enter a number as an angle: "))
angle2 = int(input("Enter a number as an angle: "))
angle3 = int(input("Enter a number as an angle: "))

if angle1 == angle2 and angle2 == angle3:
    print("It is an equilateral triangle")
else:
    print("It is not an equilateral triangle")

12.
for a in range(1, 11):
    print(a, end=' ')
print('\n')

for b in range(2, 21, 2):
    print(b, end=' ')
print('\n')

for c in range(3, 31, 3):
    print(c, end=' ')
print('\n')

for d in range(4, 41, 4):
    print(d, end=' ')
print('\n')

for e in range(5, 51, 5):
    print(e, end=' ')
print('\n')

for f in range(6, 61, 6):
    print(f, end=' ')
print('\n')

for g in range(7, 71, 7):
    print(g, end=' ')
print('\n')

for h in range(8, 81, 8):
    print(h, end=' ')
print('\n')

for i in range(9, 91, 9):
    print(i, end=' ')
print('\n')

for j in range(10, 101, 10):
    print(j, end=' ')
print('\n')