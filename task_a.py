day = input("What day is it? ").lower()

days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

while day not in days:
    day = input("What day is it?").lower()

print(f"{day} is day {days.index(day) + 1}")

