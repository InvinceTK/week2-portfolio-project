# A = 80 - 100
# B = 60 – 79
# C = 50 -59
# D = 40 – 49
# F = 0 – 39

# If the user enters a non-numerical value, your program should instead print:
# Error: Please enter a number
# And exit
# If the user enters a number outside of the permitted value, your program should print:
# Error: Grades must be between 0 and 100
# And exit

grade = input("What grade did you get? ")


if not grade.isnumeric():
    print("Error: Please enter a valid number.")
else:
    grade = int(grade)
    if grade < 0 or grade > 100:
        print("Error: Grades must be between 0 and 100")
    else:
        if grade >= 80:
            print(f"Your grade is A")
        elif grade >= 60:
            print(f"Your grade is B")
        elif grade >= 50:
            print(f"Your grade is C")
        elif grade >= 40:
            print(f"Your grade is D")
        else:
            print(f"Your grade is F")
