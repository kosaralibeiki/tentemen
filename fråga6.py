
inputs = []
while True:
    user_input = input("Vänligen skriv in något eller q för att avsluta: ")

    if user_input == "q":
        break

    inputs.append(user_input)


unique_texts = []
for text in inputs:
    if text not in unique_texts:
        unique_texts.append(text)

text_count = []
for text in unique_texts:
    count = inputs.count(text)
    text_count.append(count)
    print(count, text)


