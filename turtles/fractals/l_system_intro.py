def apply_rules(left_side_char):
    # each character is passed from process string to be acted on
    right_side_char = ""
    if left_side_char == 'A':
        right_side_char = 'B'   # Rule 1
    elif left_side_char == 'B':
        right_side_char = 'AB'  # Rule 2
    else:
        # some characters may not have rules, and we want to retain the character unmodified
        right_side_char = left_side_char    # no rules apply so keep the character
    return right_side_char


def process_string(old_str):
    new_string = ""
    # go over each character in our axiom
    for character in old_str:
        # accumulator
        # have our rules act on that character and concatonate the result into a new string
        new_string = new_string + apply_rules(character)

    return new_string


def create_L_system(num_of_iterations, axiom):
    #bc we will use the end result for the start in each successive iteration, we will declare and initialize start and end variables
    start_string = axiom
    end_string = ""
    # start iteration
    for i in range(num_of_iterations):
        #set the endstring to the result of applying the rule to the axiom (start_string)
        end_string = process_string(start_string)
        # assign this new axiom to start_string for processing in next iteration
        start_string = end_string
        # print result at end of each iteration
        print(end_string)
    # after all iterations, give the results of applying the rules to the axiom, n generations
    return end_string

# we'll start the system by telling how many iterations(generations) and the axiom to iterate on
print(create_L_system(4, "A"))
