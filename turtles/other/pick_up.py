# TODO - Create suitable data structures to store your pickup lines and their associated keywords
pick_up_lines = {"school": ["You look familiar. Did we take a class together? I could’ve sworn we had chemistry.",
                            "Is your name homework? Because I’m not doing you, but I should."
                            ],
                 "food": ["Are you a campfire? Because you’re hot and I want s’more."],
                 "rated g": ["Is your name Google? Because you’ve got everything I’m searching for.",
                             "There’s something wrong with my phone. It doesn’t have your number in it."
                             ],
                 "holiday": ["Can I take your picture to show Santa what I want for Christmas?"]
                 }
user_input = ""

while user_input.lower() != 'q':  # The program will end when the user enters 'q'
    user_input = input('Enter a keyword: ')
    print()
    print('Looking for pickup lines associated with "{}"...'.format(user_input))
    is_match = False
    for key, value in pick_up_lines.items():
        if user_input.lower() == key:
            for i, line in enumerate(value):
                print("{}. {}\n".format(i + 1, line))
                is_match = True
    if not is_match:
        print("I don't have any pickup lines for the keyword", user_input)


    """
    TODO - Display all pick-up lines that are associated with the entered keyword, or
    if there are none, inform the user that there are no pickup lines for that keyword.
    """

print('Good bye!')
