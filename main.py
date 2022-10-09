# If a number is divisible by 3 write "Fizz" if it's divisible by 5 write "Buzz". If neither write "__"
number_set = [3, 4, 55, 36, 12, 1, 100, 27, 45, 2, 360, 22, 150]

for number in number_set:
    if number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print("__")
# Fizz buzz appears to be working correctly

# GitHub shared project
