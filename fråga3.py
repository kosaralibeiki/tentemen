def grade(point):
    if 90 <= point <= 100:
        return "A"

    elif 80 <= point <= 89:
        return "B"

    elif 70 <= point <= 79:
        return "C"

    elif 60 <= point <= 69:
        return "D"

    elif 60 <= point <= 0:
        return "F"

    else:
        return f"Ogiltigt poängantal!"

# print(grade(100))
# print(grade(80))
# print(grade(81))
# print(grade(79))
# print(grade(70))
print(grade(-2))
print(grade(120))