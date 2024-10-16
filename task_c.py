# Asks users to enter a password which should consist of letters and numbers only. Punctuation can
# be ignored – the tests will not check for punctuation handling.
# - Checks that the password is:
# - A minimum of 8 characters long
# - Contains more than 1 type of character (not just letters, not just numbers)
# - If the password is valid print:
# Your password is valid
# - If the password is not valid print:
# Your password must contain at least 8 characters, and a mix of letters and numbers
# Hint: You will need to use Boolean operators and some basic string manipulation functions

password = input("Enter password that consists of letterns and numbers: ")

if len(password) >= 8 and not(password.isnumeric() or password.isalpha()):
    print("Your password is Valid")
else:
    print("Your password needs to be at least 8 characters long or a mix of numbers and letters")

    