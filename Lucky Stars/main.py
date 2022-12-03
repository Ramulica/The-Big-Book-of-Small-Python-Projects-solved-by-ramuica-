import random


def get_answer() -> bool:
    """
    functions gets an answer which decides if
    some actions will be done
    :return:
    """
    x = input(str("press y for yes or n for no:"))
    while x != "y" and x != "n":
        print("you have entered a wrong answer")
        x = input(str("press y for yes or n for no:"))
    return x == "y"


def print_dice_faces(faces: list, dices: list):
    """
    Prints the faces that you rolled
    :param faces
    :return:
    """
    print("")
    star_f = ["+-----------+",
              "|     .     |",
              "|    ,O,    |",
              "| 'ooOOOoo' |",
              "|   `OOO`   |",
              "|   O' 'O   |",
              "+-----------+"]
    skull_f = ['+-----------+',
               '|    ___    |',
               '|   /   \\   |',
               '|  |() ()|  |',
               '|   \\ ^ /   |',
               '|    VVV    |',
               '+-----------+']
    question_f = ['+-----------+',
                  '|           |',
                  '|           |',
                  '|     ?     |',
                  '|           |',
                  '|           |',
                  '+-----------+']
    printable_faces = []
    for item in faces:
        if item == "star":
            printable_faces.append(star_f)
        elif item == "skull":
            printable_faces.append(skull_f)
        elif item == "question":
            printable_faces.append(question_f)
    for i in range(7):
        print(f'{printable_faces[0][i]}    {printable_faces[1][i]}    {printable_faces[2][i]}')
    print(f'    {dices[0]}           {dices[1]}           {dices[2]}\n')


def random_dice_face(dice_type) -> str:
    """
    function gets random face from dice depending on his type
    gold: 3 stars, 2 questions, 1 skull
    silver: 2 stars, 2 questions, 2 skulls
    bronze: 1 star, 2 questions, 3 skulls
    :return:
    """
    faces = []
    if dice_type == "bronze":
        faces = ["star", "question", "question", "skull", "skull", "skull"]
    elif dice_type == "silver":
        faces = ["star", "star", "question", "question", "skull", "skull"]
    elif dice_type == "gold":
        faces = ["star", "star", "star", "question", "question", "skull"]

    return random.choice(faces)


def get_random_dice(dict_dice_in_cup: dict) -> str:
    """
    Gets a random dice from the cup
    :return:dice type
    """
    l_dice = [[k] * v for k, v in dict_dice_in_cup.items()]
    dices = [item_1 for item in l_dice for item_1 in item]

    return random.choice(dices)


def remove_used_dice_from_cup(dict_dice_in_cup: dict, removed_dice: str):
    """
    remove the used dice from dict dice cup
    :param dict_dice_in_cup:
    :param removed_dice:
    :return:
    """
    for k, v in dict_dice_in_cup.items():
        if removed_dice == k:
            dict_dice_in_cup[k] = v - 1
    return dict_dice_in_cup


def how_many_players() -> dict:
    """
    Makes a dictionary with players and their score
    :return:
    """
    player_score = {}
    while True:
        try:
            player_number = int(input("How many players are playing:"))
        except ValueError:
            print(f'Player number must be written with digits')
        else:
            break
    for _ in range(player_number):
        player_score[input("What is the name of the player")] = 0
    return player_score


def winner(payers_score: dict) -> str:
    """
    When a player gets 13 points, everyone else gets one more turn before the game ends.
    Whoever has the most points wins.
    :return:
    """
    for k, v in payers_score.items():
        if v >= 13:
            print(f"{k} has earned {v} stars, everyone else gets one more turn before the game ends.")
            return k
    else:
        return "none"


def game_round() -> int:
    """
    On your turn, you pull three random dice from the dice cup and roll them.
    You can roll Stars, Skulls, and Question Marks. If you end your turn, you
    get one point per Star. If you choose to roll again, you keep the Question
    Marks and pull new dice to replace the Stars and Skulls. If you collect
    three Skulls, you lose all your Stars and end your turn.
    :return:
    """
    dice_in_cup = {"gold": 6, "silver": 4, "bronze": 3}
    star_count = 0
    skull_count = 0
    question_faces = []
    while True:
        rolled_dices = question_faces
        rolled_faces = [random_dice_face(item) for item in rolled_dices]
        question_faces = []
        for i in range(len(rolled_faces)):
            if rolled_faces[i] == "star":
                star_count += 1
            if rolled_faces[i] == "skull":
                skull_count += 1
            if rolled_faces[i] == "question":
                question_faces.append(rolled_dices[i])
        while len(rolled_faces) != 3:
            random_dice = (get_random_dice(dice_in_cup))
            random_face = random_dice_face(random_dice)
            dice_in_cup = remove_used_dice_from_cup(dice_in_cup, random_dice)
            rolled_dices.append(random_dice)
            rolled_faces.append(random_face)
            if random_face == "star":
                star_count += 1
            if random_face == "skull":
                skull_count += 1
            if random_face == "question":
                question_faces.append(random_dice)

        print_dice_faces(rolled_faces, rolled_dices)
        if skull_count >= 3:
            print(f"You have {skull_count} skulls, you lost your round")
            star_count = 0
            break

        print(f"you have {star_count} star(s) and {skull_count} skull(s)")
        print(f"Those are the dices ledt in the cup: {dice_in_cup}")

        if sum(dice_in_cup.values()) < 3 - len(question_faces):
            print("you used all your dices")
            break

        print("do you want to continue?")
        if not get_answer():
            break
    return star_count


players = how_many_players()
x = True
while x:

    for k, v in players.items():
        game_winner = winner(players)
        if game_winner != "none":
            x = False
            break
        print(f"\nIt's {k}'s turn to play")
        players[k] = v + game_round()
        print(f"\n\nThe score is {players}\n")

for k, v in players.items():
    if k != game_winner:
        players[k] = v + game_round()

print(f"\n\nThe final score is {players}\n")