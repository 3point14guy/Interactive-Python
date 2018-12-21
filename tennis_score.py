import random

player_a_wins = False
player_b_wins = False

# for i in range(1): # temp until while condition can be completed
player_a = ["Federer", 0]
player_b = ["Agassi", 0]
score = ""
i = 0

# determine who gets to serve
serve = random.choice((1,2))
if serve ==1:
    print("{} serves this game.\n".format(player_a[0]))
else:
    print("{} serves this game.\n".format(player_b[0]))

def print_score(serve, player_a, player_b):
    if serve ==1:
        print_score = "{} : {}, {} : {}\n".format(player_a[0], player_a[1], player_b[0], player_b[1])
    else:
        print_score = "{} : {}, {} : {}\n".format(player_b[0], player_b[1], player_a[0], player_a[1])
    print(print_score)

def score_game_to_deuce(player_one, player_two, score, player_one_wins):
    if player_one[1] < 30:
        player_one[1] += 15

    elif player_one[1] == 30:
        if player_two[1] == 40:
            score = "deuce"
        else:
            player_one[1] += 10
    elif player_one[1] == 40 and player_two[1] != 40:
        score = "{} wins!".format(player_one[0])
        player_one_wins = True
    else:
        score = "deuce"
    return player_one, score, player_one_wins

def score_game_after_deuce(player_one, player_two, score, player_one_wins):
    if score == "deuce":
        score = "Advantage {}".format(player_one[0])
    elif score == "Advantage {}".format(player_one[0]):
        score = "{} wins!".format(player_one[0])
        player_one_wins = True
    elif score == "Advantage {}".format(player_two[0]):
        score = "deuce"
    return score, player_one_wins

while score != "deuce" and player_a_wins == False and player_b_wins == False:
    point = random.choice((1,2))
    if point == 1:
        print("Point awarded to {}".format(player_a[0]))
        player_a, score, player_a_wins = score_game_to_deuce(player_a, player_b, score, player_a_wins)
        # if player_a_wins == True:
        #     break
    else:
        print("Point awarded to {}".format(player_b[0]))
        player_b, score, player_b_wins = score_game_to_deuce(player_b, player_a, score, player_b_wins)
        # if player_a_wins == True:
        #     break
    if  score != "deuce" and player_a_wins == False and player_b_wins == False:
        print_score(serve, player_a, player_b)
    else:
        print(score)


while player_a_wins == False and player_b_wins == False:
    point = random.choice((1,2))
    if point == 1:
        print("Point awarded to {}".format(player_a[0]))
        score, player_a_wins = score_game_after_deuce(player_a, player_b, score, player_a_wins)
    else:
        print("Point awarded to {}".format(player_b[0]))
        score, player_b_wins = score_game_after_deuce(player_b, player_a, score, player_b_wins)

    print(score)

print("\n\n")
