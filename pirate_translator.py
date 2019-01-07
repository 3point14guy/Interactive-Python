translator = {"sir": "matey", "madam": "proud beauty", "boy": "matey", "man": "matey", "hotel": "fleabag inn", "student": "swabbie", "professor": "foul blaggart", "lawyer": "foul blaggart", "restaurant": "galley", "are": "be", "the": "th'", "bathroom": "head", "my": "me", "hello": "avast", "is": "be", "man": "matey"}

sentence = input("enter a sentence to translate: ")

translated = []
for word in sentence.split():
    print(word)
    if word in translator:
        translated.append(translator[word])
    else:
        translated.append(word)

print(" ".join(translated))
