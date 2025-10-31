# Udda och jämna!


numbers =[]
while True:
    user_input = input("Write a whole number or 'q' to quit: ").strip()

    if user_input == 'q':
        break

    try:
        user_input = int(user_input)

        if user_input >= 0:
            numbers.append(user_input)

        else:
            print("Please enter a whole number or 'q' to quit")
    except ValueError:
        print("Please enter a whole number or 'q' to quit")
        continue

if not numbers:
    print("No numbers entered")

unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

unique_numbers.sort()

# print(numbers)
for number in unique_numbers:
    counts = numbers.count(number)
    if number % 2 == 0:
        with open("jämna.txt", "a", encoding="UTF-8") as file:
            file.write(f"{number} : {counts}\n")
    else:
        with open("udda.txt", "a", encoding="UTF-8") as file:
            file.write(f"{number} : {counts}\n")
