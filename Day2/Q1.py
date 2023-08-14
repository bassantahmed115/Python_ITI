def character_locator(sentence, char):
    locations = []
    for index, c in enumerate(sentence):
        if c == char:
            locations.append(index)
    
    return locations

def character_locator():
    sentence = input("Enter a sentence: ")
    char = input("Enter the character you want to locate: ")

    if len(char) != 1:
        return "Please enter only one character."

    locations = []
    for index, c in enumerate(sentence):
        if c == char:
            locations.append(index)
    
    if locations:
        return f"The character '{char}' is found at positions: {locations}"
    else:
        return f"The character '{char}' was not found in the sentence."

result = character_locator()
print(result)
