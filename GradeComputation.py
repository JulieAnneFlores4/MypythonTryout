print("Enter your grade in 7 Subjects: ")
gradeOne = int(input())
gradeTwo = int(input())
gradeThree = int(input())
gradeFour = int(input())
gradeFive = int(input())
gradeSix = int(input())
gradeSeven = int(input())

total = gradeOne + gradeTwo + gradeThree + gradeFour + gradeFive + gradeSix + gradeSeven
avg = total / 7

if 90 <= avg <= 100:
    print("Excellent! You Passed")
elif 80 <= avg < 90:
    print("You Passed! Congratulations!")
elif 61 <= avg < 80:
    print("You Failed!")
else:
    print("Invalid!")
