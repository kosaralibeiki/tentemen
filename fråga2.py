
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

sorted_numbers = numbers.sort()

print(numbers)
for number in numbers:
    counts = numbers.count(number)
    if number % 2 == 0:
        with open("jämna.txt", "a", encoding="UTF-8") as file:
            file.write(f"{number} : {counts}\n")
    else:
        with open("udda.txt", "a", encoding="UTF-8") as file:
            file.write(f"{number} : {counts}\n")
