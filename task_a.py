day = input("What day is it? ").lower()

days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

if day in days:
    print(f"{day.capitalize()} is day {days.index(day) + 1}")
else:
    print("Please enter a valid day")



