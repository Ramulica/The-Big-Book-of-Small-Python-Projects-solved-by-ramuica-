import random
import os


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


def get_color_biome(biome):
    """

    :param biome:
    :return:
    """
    color = ""
    obstacles = ""
    if biome == "grass":
        color = "\033[2;32;42m"
        obstacles = ["🌳", "🌲", "🌾"]
    elif biome == "snow":
        color = "\033[2;32;47m"
        obstacles = ["🎄", "🎁", "⛄"]
    elif biome == "dessert":
        color = "\033[2;32;43m"
        obstacles = ["🏜", "🌴", "🏵"]
    elif biome == "hell":
        color = "\033[2;32;41m"
        obstacles = ["🌋", "🔥", "📍"]
    elif biome == "unicorn":
        color = "\033[2;32;45m"
        obstacles = ["🌈", "🍧", "🌺", "🦄"]

    return color, obstacles


def get_correct_int_input(message) -> int:
    """

    :return:
    """
    while True:
        try:
            age = int(input(message))
        except ValueError:
            print(f'error input must be written with digits')
        else:
            break
    return age


def generate_room_length_height():
    """

    :return:
    """
    length = random.choice(range(8, 12))
    height = random.choice(range(6, 9))
    return length, height


def generate_rooms(biome: str, length: int, height: int) -> list:
    """
    "🧙‍" +🌳🌲🌾⛄🎁🎄
    :return:
    """
    output = []
    color, obstacles = get_color_biome(biome)
    output.append(("  " * (length + 2)))
    for i in range(height):
        obstacle_column = [random.choice(range(length)) for _ in range(random.choice(range(1, 3)))]
        obstacle_column.sort()
        obstacle_column.append(" ")
        # print(obstacle_column)
        # print(obstacle_column[0])
        obstacle_count = 0
        row = ""
        for i_1 in range(length):
            if i_1 == obstacle_column[obstacle_count]:
                row += f"{random.choice(obstacles)}"
                obstacle_count += 1
            else:
                row += f"  "
        output.append(row)
    output.append(("  " * (length + 2)))

    return output


def print_room(room: str, biome: str):
    """

    :param room:
    :param biome:
    :return:
    """
    print(f"\033[2;32;40m{room[0]}\033[0;0m")
    color, obstacles = get_color_biome(biome)
    margins = '\033[2;32;40m  '
    for item in room[1:-1]:
        print(f"{margins}{color}{item}{margins}\033[0;0m")
    print(f"\033[2;32;40m{room[-1]}\033[0;0m")


def get_random_biome() -> str:
    """

    :return:
    """
    return random.choice(["grass", "snow", "dessert", "hell", "unicorn"])


def add_object_on_map(room: list, hero: str, column: int, row: int):
    """

    :param hero:
    :param room:
    :param column:
    :param row:
    :return:
    """
    column = column - 1
    output = []
    count_row_positions = 0
    count_row_positions_actions = 0

    for i, item in enumerate(room):
        if i == row:
            if column == 0:
                if item[0] == " ":
                    output.append(f"{hero}{item[2::]}")
                else:
                    output.append(f"{hero}{item[1::]}")
            else:
                for ch in item:

                    if ch == " ":
                        count_row_positions += 1
                        count_row_positions_actions += 1
                    elif ch != " ":
                        count_row_positions += 1
                        count_row_positions_actions += 2

                    if count_row_positions_actions >= column * 2:
                        break

                output.append(f"{item[0:count_row_positions]}{hero}{item[count_row_positions + 2::]}")
        else:
            output.append(item)
    return output


def choose_door(biome: str):
    """

    :param biome:
    :return:
    """
    dor = ""
    if biome == "grass":
        dor = "⛩"
    elif biome == "snow":
        dor = "🏛"
    elif biome == "dessert":
        dor = "🛕"
    elif biome == "hell":
        dor = "⛩"
    elif biome == "unicorn":
        dor = "🏛"
    return dor


def choose_enemy():
    """

    :return:
    """
    return random.choice(['👨🏿', '💀', '👺', '👹', '🕷', '🦂', '👻', '👽', '😈', '🌬', '🎃', '👾', '🐲', "🎭"])


def get_hero_name() -> str:
    """
    If the username doesn't have unknown characters it returns the name
    :return:
    """
    main_path = os.getcwd()
    os.chdir("Your_characters")
    while True:
        username = input(str("Enter your username:"))

        if len(username) >= 4 and f"{username}.txt" not in os.listdir():
            x = 0
            for ch in username:
                if ch in '!"#$%&\'*()+,/:;<=>?@[\\]^`{|}~':
                    x = 1
            if x == 0:
                break
            else:
                print("Error: username cannot contain any of these characters !\"#$%&\'*+,/:;<=>?@[\\]^`{|}~")
        else:
            if len(username) < 4:
                print("Error: username must have at least 4 characters")
            else:
                print("username already used")
    os.chdir(main_path)
    return username


def write_hero_data(hero_name: str, hero_class: str, level: str,
                    gold: str, materials: dict, gear: dict, inventory: list):
    """

    :return:
    """

    main_path = os.getcwd()
    new_data = [hero_class, level, gold]
    for k, v in materials.items():
        new_data.append(f"{v}")
    for k_1, v_1 in gear.items():
        new_data.append(f"{v_1}")
    for item in inventory:
        new_data.append(item)
    os.chdir("Your_characters")

    with open(f"{hero_name}.txt", "w") as fw:
        for item in new_data:
            fw.write(item + "\n")

    os.chdir(main_path)


def read_abilities(selected_hero: str):
    """

    :param selected_hero:
    :return:
    """
    main_path = os.getcwd()
    os.chdir("heroes")
    for item in os.listdir():
        if item[0:4] == selected_hero[0:4]:
            with open(item, "r") as fr:
                content = fr.readlines()
    os.chdir(main_path)
    output = [item.strip() for item in content]
    for item in output:
        print(item)


def create_hero():
    """

    :return:
    """
    name = ""
    main_while_break = 0
    print("")
    print(
        "Choose a class for your hero:\nWizard(🧙)\nShadow(👤‍)\nVampire(🧛‍)\nfairy.txt(🧚‍)\nTriton(🧜)\nSpirit(🧞‍)")
    hero_class = str.lower(input("Choose one option by writing the class name:"))
    classes = ["wizard", "shadow", "vampire", "fairy", "triton", "spirit"]
    while True:

        while hero_class not in classes:
            print("incorrect class, try again")
            hero_class = str.lower(input("Choose one option by writing the class name:"))
        with open("hero_class_description", "r") as fr:
            content = fr.readlines()
        for item in content:
            if str.lower(item[0:4]) == str.lower(hero_class[0:4]):
                print(f"\n{item}\n")
        print("Choose one option:\ngo back(b)\nchoose class(c)\nread abilities(a)")
        option = str.lower(input("Your option:"))
        while option:
            if option not in ["c", "b", "a"]:
                print("option is incorrect")
            elif option == "a":
                read_abilities(hero_class)
            elif option == "c":
                items_0 = {"helm": "empty_", "chest": "empty_", "boots": "empty_", "weapon": "empty_",
                           "sec_weapon": "empty_", "jewel": "empty_"}
                materials_0 = {"wood": '0', "iron": '0', "diamond": '0', "angelic dust": '0'}
                name = get_hero_name()
                write_hero_data(name, hero_class, "0", "500", materials_0, items_0, ["empty_"] * 18)
                main_while_break = 1
                break
            else:
                break
            print("\nChoose one option:\ngo back(b)\nchoose class(c)\nread abilities(a)")
            option = str.lower(input("Your option:"))

        if main_while_break == 1:
            break
        else:
            print("")
            print("Choose a class for your hero:\nWizard(🧙)\nShadow(👤‍)\nVampire(🧛‍)"
                  "\nfairy.txt(🧚‍)\nTriton(🧜)\nSpirit(🧞‍)")
            hero_class = str.lower(input("Choose one option by writing the class name:"))
            classes = ["wizard", "shadow", "vampire", "fairy", "triton", "spirit"]
    return f"{name}.txt"


def get_hero_symbol(hero_name):
    """

    :param hero_name:
    :return:
    """
    output = ""
    changed_directory = 0
    main_path = os.getcwd()
    if main_path != "C:\\Users\\andre\\PycharmProjects\\" \
                    "The-Big-Book-of-Small-Python-Projects-solved-by-ramuica-\\Angelic Powers\\Your_characters":
        os.chdir("Your_characters")
        changed_directory = 1
    for item in os.listdir():
        if item == f"{hero_name}.txt":
            with open(item, "r") as fr:
                content = fr.readlines()
    hero_and_class = {"wizard": "🧙", "shadow": "👤", "vampire": "🧛", "fairy": "🧚", "triton": "🧜", "spirit": "🧞"}
    for k, v in hero_and_class.items():
        if k == content[0].strip():
            output = v
    if changed_directory == 1:
        os.chdir(main_path)
    return output


def get_item_symbol(item):
    """

    :param item:
    :return:
    """

    output = ""
    dict_items = {"crown": "👑", "wand": "🎆",
                  "the_eye": "🧿", "robe": "👘",
                  "talisman": "🎐", "boots": "👢"}

    for k, v in dict_items.items():
        if item == k:
            output = v
            break
    return output


def play_existing_hero():
    """

    :return:
    """
    main_path = os.getcwd()
    os.chdir("Your_characters")
    while True:
        print("\nChoose what hero do you want to play:")
        for i, item in enumerate(os.listdir()):
            symbol = get_hero_symbol(item[0:-4])
            print(f"{item[0:-4]}{symbol}({i + 1})")
        option = get_correct_int_input("\nChoose a hero by writing his corresponding number: ")
        if 0 < option <= len(os.listdir()):
            output = os.listdir()[option - 1]
            break
        else:
            print("the option you choose doesn't correspond to any hero")
    os.chdir(main_path)
    return output


def decide_what_hero_to_play():
    """

    :return:
    """
    while True:
        print("Do you want to create a new hero or to play an existing one?\nCreate(c)\nChoose existing hero(e)")
        option = input("\nChoose an option by writing his corresponding letter: ")
        if option == "e":
            print(play_existing_hero())
            break
        elif option == "c":
            print(create_hero())
            break
        else:
            print("\nthe letter you choose doesn't correspond to any option. Try again\n")


def read_inventory(file):
    """

    :param file:
    :return:
    """
    main_path = os.getcwd()
    os.chdir("Your_characters")
    with open(file, "r") as fr:
        content = fr.readlines()
    os.chdir(main_path)
    inventory = [item.strip() for item in content]
    return inventory


def get_random_rarity(difficulty):
    """

    :param difficulty:
    :return:
    """
    red_item = 10 * difficulty
    grren_item = 50 * difficulty
    yellow_item = 500 * difficulty
    blue_item = 1300 * difficulty
    black_chance = 10000 - blue_item - yellow_item - grren_item - red_item
    list_chances = ["common"] * (black_chance) + ["normal"] * (blue_item) + ["rare"] * \
                   (yellow_item) + ["legendary"] * (grren_item) + ["angelic"] * (red_item)
    return random.choice(list_chances)


def get_rarity_color(rarity):
    if rarity == "common":
        return "\033[40m", "\033[30m"
    elif rarity == "normal":
        return "\033[44m", "\033[34m"
    elif rarity == "rare":
        return "\033[43m", "\033[33m"
    elif rarity == "legendary":
        return "\033[42m", "\033[32m"
    elif rarity == "angelic":
        return "\033[41m", "\033[31m"


def print_inventory(file):
    """

    :param file:
    :return:
    """

    symbol = get_hero_symbol(file[0:-4])
    inventory = read_inventory(file)
    print(f"\033[4m{' ' * 30}\033[0;0m ")
    print(f"|\033[95m{file[0:-4]}  lv: {inventory[1]}\033[0;0m "
          f"{' ' * (21 - len(file[0:-4]) - len(str(inventory[1])))}|")
    print(f"|  \033[1;30;45m|{symbol}|\033[2;37;0m{' ' * 10}\033[1;30;47m{item_colored_symbol(inventory[12])}\033[0;0m "
          f"\033[1;30;47m{item_colored_symbol(inventory[7])}\033[2;37;0m{' ' * 7}|")
    print(f"|\033[32mwood: {inventory[3]}\033[0;0m{' ' * (22 - len(str(inventory[3])))}|")
    print(f"|\033[38msilver: {inventory[4]}\033[0;0m"
          f"{' ' * (8 - len(str(inventory[4])))}\033[1;30;47m{item_colored_symbol(inventory[10])}\033[0;0m "
          f"\033[1;30;47m{item_colored_symbol(inventory[8])}\033[0;0m \033[1;30;47m{item_colored_symbol(inventory[11])}\033[0;0m"
          f"{' ' * 3}|")
    print(f"|\033[34mdiamond: {inventory[5]}\033[0;0m{' ' * (19- len(str(inventory[5])))}|")
    print(f"|\033[31mangelic dust: {inventory[6]}\033[0;0m{' ' * (5- len(str(inventory[6])))}\033[1;30;47m"
          f"{item_colored_symbol(inventory[9])}\033[0;0m"
          f"{' ' * 7}|")
    print(f"|\033[33mgold: {inventory[2]}\033[0;0m{' ' * (22- len(str(inventory[2])))}|")
    row_1 = ""
    row_2 = ""
    row_3 = ""
    row_counter = 1
    for item in inventory[13::]:
        if row_counter <= 6:
            row_1 += f"{item_colored_symbol(item)}  "
        elif row_counter <= 12:
            row_2 += f"{item_colored_symbol(item)}  "
        elif row_counter <= 18:
            row_3 += f"{item_colored_symbol(item)}  "
        row_counter += 1
    if row_counter < 7:
        row_1 += "\033[1;30;47m  \033[0;0m  " * (7 - row_counter)
        row_2 += "\033[1;30;47m  \033[0;0m  " * 6
        row_3 += "\033[1;30;47m  \033[0;0m  " * 6
    elif row_counter < 13:
        row_2 += "\033[1;30;47m  \033[0;0m  " * (13 - row_counter)
        row_3 += "\033[1;30;47m  \033[0;0m  " * 6
    elif row_counter < 19:
        row_3 += "\033[1;30;47m  \033[0;0m  " * (19 - row_counter)
    print(f"|{' ' * 28}|")
    print(f"|  {row_1} |")
    print(f"|{' ' * 28}|")
    print(f"|  {row_2} |")
    print(f"|{' ' * 28}|")
    print(f"|  {row_3} |")
    print(f"|\033[4m{' ' * 28}\033[0;0m|")


def random_primary_stat(rarity,):
    """

    :return:
    """

    if rarity == "common":
        return f"primary: {random.choice(range(2, 5))}"
    elif rarity == "normal":
        return f"primary: {random.choice(range(4, 12))}"
    elif rarity == "rare":
        return f"primary: {random.choice(range(10, 25))}"
    elif rarity == "legendary":
        return f"primary: {random.choice(range(50, 100))}"
    elif rarity == "angelic":
        return f"primary: 200"


def random_secondary_stat(rarity):
    """

    :param rarity:
    :return:
    """
    stat_factor = {"armor": 1, "hp": 10, "crit": 0.2, "crit_dmg": 1, "speed": 1, "mr": 1,
                   "dodge": 0.4, "cc_immun": 0.2, "mana": 0.2}

    stat_name = random.choice(list(stat_factor.keys()))

    if rarity == "common":
        return f"{stat_name}: {round(random.choice(range(2, 5)) * stat_factor[stat_name], 1)}"
    elif rarity == "normal":
        return f"{stat_name}: {round(random.choice(range(4, 12)) * stat_factor[stat_name], 1)}"
    elif rarity == "rare":
        return f"{stat_name}: {round(random.choice(range(10, 25)) * stat_factor[stat_name], 1)}"
    elif rarity == "legendary":
        return f"{stat_name}: {round(random.choice(range(50, 100)) * stat_factor[stat_name], 1)}"
    elif rarity == "angelic":
        return f"{stat_name}: {round(200 * stat_factor[stat_name], 1)}"


def create_item(item_name, difficulty):
    """

    :param item_name:
    :param difficulty:
    :return:
    """
    rarity = get_random_rarity(difficulty)
    return f"{item_name} {rarity} {random_primary_stat(rarity)}" \
           f" {random_secondary_stat(rarity)} {random_secondary_stat(rarity)} {random_secondary_stat(rarity)}"\


def print_item(item):
    """

    :param item:
    :return:
    """
    item_l = item.split()

    item_color, text_color = get_rarity_color(item_l[1])
    print(f" {text_color}{'_' * 16}\033[0;0m ")
    print(f"{text_color}|\033[0;0m{item_l[0]}{' ' * (15 - len(item_l[0]) - len(item_l[1]))}{text_color}{item_l[1]} |")
    print(f"{text_color}|\033[0;0m {item_color}{get_item_symbol(item_l[0]) }\033[0;0m{' ' * 13}{text_color}|\033[0;0m")
    print(f"{text_color}|{' ' * 16}|\033[0;0m")
    print(f"{text_color}|\033[0;0m {item_l[2]} {item_l[3]}\033[0;0m{' ' * (14 - len(item_l[2]) - len(item_l[3]))}{text_color}|\033[0;0m")
    print(f"{text_color}|\033[0;0m {item_l[4]} {item_l[5]}\033[0;0m{' ' * (14 - len(item_l[4]) - len(item_l[5]))}{text_color}|\033[0;0m")
    print(f"{text_color}|\033[0;0m {item_l[6]} {item_l[7]}\033[0;0m{' ' * (14 - len(item_l[6]) - len(item_l[7]))}{text_color}|\033[0;0m")
    print(f"{text_color}|\033[0;0m {item_l[8]} {item_l[9]}\033[0;0m{' ' * (14 - len(item_l[8]) - len(item_l[9]))}{text_color}|\033[0;0m")
    print(f"{text_color}|{'_' * 16}|\033[0;0m")


def item_colored_symbol(item):
    """

    :param item:
    :return:
    """
    if item == "empty":
        return "\033[1;30;47m⬛\033[0;0m"
    else:
        item_l = item.split()
        item_color, text_color = get_rarity_color(item_l[1])
        return f"{item_color}{get_item_symbol(item_l[0])}\033[0;0m"


def navigate_inventory(file):
    """

    :return:
    """
    full_inventory = read_inventory(file)
    inventory = full_inventory[7::]

    print("inventory option:\n-see stats of a weapon(s)\n-equip a weapon(e)\ngo back(b)")
    option = input("choose one option by writing its corresponding value:")
    while True:
        if option == "s":
            print("Choose item:\nhead(0)\nchest(1)\nfeet(2)\nmain hand(3)\n2nd hand(4)\n"
                  "jewel(5)\ninventory(coresponding number)")
            option_s = get_correct_int_input("choose one option by writing its corresponding value:")
            if option_s <= 21:
                print_item(inventory[option_s])
            else:
                print("Wrong value entered")
        elif option == "b":
            break
        else:
            print("wrong value entered")
        print("inventory option:\n-see stats of a weapon(s)\n-equip a weapon(e)\ngo back(b)")
        option = input("choose one option by writing its corresponding value:")


def hero_movement(file, column: int, row: int, max_column: int, max_row: int):
    """

    :param column:
    :param row:
    :param max_column:
    :param max_row:
    :return:
    """
    print("You can move by entering a sequence of movements:\n-go up(w)\n-go left(a)\n-go down(s)\n-go right(d)\n\n"
          "Other options:\nsee inventory(i)\nexit(e)")
    movement = str.lower(input("enter a sequence of movements:"))
    if movement == "i":
        print_inventory(file)
        navigate_inventory(file)
    if movement == "e":
        return 0, 0
    else:
        while True:
            row_func = row
            column_func = column
            while True:
                for ch in movement:
                    if ch not in "wasd":
                        print("incorrect sequence")
                        movement = str.lower(input("enter a sequence of movements:"))
                        break
                else:
                    break
            for ch in movement:
                if ch == "w":
                    row_func -= 1
                if ch == "s":
                    row_func += 1
                if ch == "a":
                    column_func -= 1
                if ch == "d":
                    column_func += 1
            if 0 < column_func <= max_column and 0 < row_func <= max_row:
                break
            else:
                print("incorrect movement")
                movement = str.lower(input("enter a sequence of movements:"))
        return column_func, row_func


biome = get_random_biome()
length, height = generate_room_length_height()
room_1 = generate_rooms(biome, length, height)
room_1 = add_object_on_map(room_1, choose_enemy(), 5, 6)
room_1 = add_object_on_map(room_1, choose_enemy(), 1, 6)
room_1 = add_object_on_map(room_1, choose_enemy(), 5, 1)
column, row = 1, 1
room_1_h = add_object_on_map(room_1, "🧙", column, row)
print_room(room_1_h, biome)
while True:
    column, row = hero_movement("ramulica.txt", column, row, length, height)
    if column + row == 0:
        break
    else:
        room_1_h = add_object_on_map(room_1, "🧙", column, row)
        print_room(room_1_h, biome)




