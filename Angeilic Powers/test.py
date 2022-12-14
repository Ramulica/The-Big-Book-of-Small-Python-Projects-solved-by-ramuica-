import random
import os
# import main
#
# def get_color_biome(biome):
#     """
#
#     :param biome:
#     :return:
#     """
#     if biome == "grass":
#         color = "\033[2;32;42m"
#         obstacles = ["🌳", "🌲", "🌾"]
#     elif biome == "snow":
#         color = "\033[2;32;47m"
#         obstacles = ["🎄", "🎁", "⛄"]
#     elif biome == "dessert":
#         color = "\033[2;32;43m"
#         obstacles = ["🏜", "🌴", "🏵"]
#     elif biome == "hell":
#         color = "\033[2;32;41m"
#         obstacles = ["🌋", "🔥", "📍"]
#     elif biome == "unicorn":
#         color = "\033[2;32;45m"
#         obstacles = ["🌈", "🍧", "🌺", "🦄"]
#
#     return color, obstacles
#
#
# def genereate_rooms(biome: str) -> list:
#     """
#     "🧙‍" +🌳🌲🌾⛄🎁🎄
#     :return:
#     """
#     lenght = random.choice(range(8, 12))
#     hight = random.choice(range(6, 9))
#     output = []
#     color, obstacles = get_color_biome(biome)
#     output.append(("  " * (lenght + 2)))
#     for i in range(hight):
#         obstacle_column = [random.choice(range(lenght)) for _ in range(random.choice(range(1, 3)))]
#         obstacle_column.sort()
#         obstacle_column.append(" ")
#         # print(obstacle_column)
#         # print(obstacle_column[0])
#         obstacle_count = 0
#         row = ""
#         for i_1 in range(lenght):
#             if i_1 == obstacle_column[obstacle_count]:
#                 row += f"{random.choice(obstacles)}"
#                 obstacle_count += 1
#             else:
#                 row += f"  "
#         output.append(row)
#     output.append(("  " * (lenght + 2)))
#
#     return output
#
#
# def print_room(room: str, biome):
#     """
#
#     :param room:
#     :return:
#     """
#     print(f"\033[2;32;40m{room[0]}\033[0;0m")
#     color, obstacles = get_color_biome(biome)
#     margins = '\033[2;32;40m  '
#     for item_f in room[1:-1]:
#         print(f"{margins}{color}{item_f}{margins}\033[0;0m")
#     print(f"\033[2;32;40m{room[-1]}\033[0;0m")
#
# def get_random_biome() -> str:
#     """
#
#     :return:
#     """
#     return random.choice(["grass", "snow", "dessert", "hell", "unicorn"])
#
#
# def add_hero_on_map(room: list, hero: str, column: int, row: int, biome: str):
#     """
#
#     :param hero:
#     :param room:
#     :param column:
#     :param row:
#     :param biome:
#     :return:
#     """
#     margins = '\033[2;32;40m  '
#     color, obstacles = get_color_biome(biome)
#     hero_1 = f"{color}{hero}"
#     count_range = 0
#     output = []
#     for i, item_f in enumerate(room):
#         if i == row:
#
#             output.append(len(item_f))
#
#         else:
#             output.append(item_f)
#     return output
#
#
# biome = get_random_biome()
# room_1 = genereate_rooms(biome)
# print_room(room_1, biome)
# print(" ")
# # room_1_with_hero = add_hero_on_map(room_1, "🧙", 4, 4, biome)
# # print_room(room_1_with_hero)
#
# def hero_movement(column: int, row: int, max_column: int, max_row: int):
#     """
#
#     :param column:
#     :param row:
#     :return:
#     """
#     print("You can move by entering a sequence of movements:\n-go up(w)\n-go left(a)\n-go down(s)\n-go right(d)")
#     movement = str.lower(input("enter a sequence of movements:"))
#     while True:
#         row_func = row
#         column_func = column
#         while True:
#             for ch in movement:
#                 if ch not in "wasd":
#                     print("incorrect sequence")
#                     movement = str.lower(input("enter a sequence of movements:"))
#                     break
#             else:
#                 break
#         for ch in movement:
#             if ch == "w":
#                 row_func += 1
#             if ch == "s":
#                 row_func -= 1
#             if ch == "a":
#                 column_func -= 1
#             if ch == "d":
#                 column_func += 1
#         if 0 < column_func <= max_column and 0 < row_func <= max_row:
#             break
#         else:
#             print("incorrect movement")
#             movement = str.lower(input("enter a sequence of movements:"))
#     return column_func, row_func
#
#
# print(hero_movement(1, 2, 5, 6))
# def get_hero_name() -> str:
#     """
#     If the username doesn't have unknown characters it returns the name
#     :return:
#     """
#     while True:
#         username = input(str("Enter your username:"))
#         x = 0
#         for ch in username:
#             if ch in '!"#$%&\'*()+,/:;<=>?@[\\]^`{|}~':
#                 x = 1
#         if x == 0:
#             break
#         else:
#             print("Error: username cannot contain any of these characters !\"#$%&\'*+,/:;<=>?@[\\]^`{|}~")
#     return username
#
#
# def write_hero_data(hero_name: str, hero_class: str, level: str, gold: str, materials: dict, gear: dict, inventory: list):
#     """
#
#     :return:
#     """
#
#     main_path = os.getcwd()
#     new_data = [hero_class, level, gold]
#     for k, v in materials.item_fs():
#         new_data.append(f"{v}")
#     for k_1, v_1 in gear.item_fs():
#         new_data.append(f"{v_1}")
#     for item_f in inventory:
#         new_data.append(item_f)
#     os.chdir("Your_characters")
#
#     with open(f"{hero_name}.txt", "w") as fw:
#         for item_f in new_data:
#             fw.write(item_f + "\n")
#
#     os.chdir(main_path)
#
#
# def read_abilities(selected_hero: str):
#     """
#
#     :param selected_hero:
#     :return:
#     """
#     main_path = os.getcwd()
#     os.chdir("heroes")
#     for item_f in os.listdir():
#         if item_f[0:4] == selected_hero[0:4]:
#             with open(item_f, "r") as fr:
#                 content = fr.readlines()
#     os.chdir(main_path)
#     output = [item_f.strip() for item_f in content]
#     for item_f in output:
#         print(item_f)
#
#
# def create_hero():
#     """
#
#     :return:
#     """
#     main_while_break = 0
#     print("")
#     print(
#         "Choose a class for your hero:\nWizard(🧙)\nShadow(👤‍)\nVampire(🧛‍)\nfairy.txt(🧚‍)\nTriton(🧜)\nSpirit(🧞‍)")
#     hero_class = str.lower(input("Choose one option by writing the class name:"))
#     hero_and_class = {"wizard": "🧙", "shadow": "👤", "vampire": "🧛", "fairy": "🧚", "triton": "🧜", "spirit": "🧞"}
#     classes = ["wizard", "shadow", "vampire", "fairy", "triton", "spirit"]
#     while True:
#
#         while hero_class not in classes:
#             print("incorrect class, try again")
#             hero_class = str.lower(input("Choose one option by writing the class name:"))
#         with open("hero_class_description", "r") as fr:
#             content = fr.readlines()
#         for item_f in content:
#             if str.lower(item_f[0:4]) == str.lower(hero_class[0:4]):
#                 print(f"\n{item_f}\n")
#         print("Choose one option:\ngo back(b)\nchoose class(c)\nread abilities(a)")
#         option = str.lower(input("Your option:"))
#         while option:
#             if option not in ["c", "b", "a"]:
#                 print("option is incorrect")
#             elif option == "a":
#                 read_abilities(hero_class)
#             elif option == "c":
#                 item_fs_0 = {"helm": "empty", "chest": "empty", "boots": "empty", "weapon": "empty", "sec_weapon": "empty",
#                            "jewel": "empty"}
#                 matirials_0 = {"wood": '0', "iron": '0', "diamond": '0', "angelic dust": '0'}
#                 name = get_hero_name()
#                 write_hero_data(name, hero_class, "0", "500",matirials_0, item_fs_0, [])
#                 main_while_break = 1
#                 break
#             else:
#                 break
#             print("\nChoose one option:\ngo back(b)\nchoose class(c)\nread abilities(a)")
#             option = str.lower(input("Your option:"))
#
#         if main_while_break == 1:
#             break
#         else:
#             print("")
#             print("Choose a class for your hero:\nWizard(🧙)\nShadow(👤‍)\nVampire(🧛‍)\nfairy.txt(🧚‍)\nTriton(🧜)\nSpirit(🧞‍)")
#             hero_class = str.lower(input("Choose one option by writing the class name:"))
#             hero_and_class = {"wizard": "🧙", "shadow": "👤", "vampire": "🧛", "fairy": "🧚", "triton": "🧜", "spirit": "🧞"}
#             classes = ["wizard", "shadow", "vampire", "fairy", "triton", "spirit"]
#
#
#
#
# create_hero()

# def get_hero_symbol(hero_name):
#     """
#
#     :param hero_class:
#     :return:
#     """
#     output = ""
#     main_path = os.getcwd()
#     os.chdir("Your_characters")
#     for item_f in os.listdir():
#         if item_f == f"{hero_name}.txt":
#             with open(item_f, "r") as fr:
#                 content = fr.readlines()
#     hero_and_class = {"wizard": "🧙", "shadow": "👤", "vampire": "🧛", "fairy": "🧚", "triton": "🧜", "spirit": "🧞"}
#     for k, v in hero_and_class.item_fs():
#         if k == content[0].strip():
#             output = v
#     os.chdir(main_path)
#     return output

#
# def get_hero_name() -> str:
#     """
#     If the username doesn't have unknown characters it returns the name
#     :return:
#     """
#     main_path = os.getcwd()
#     os.chdir("Your_characters")
#     while True:
#         username = input(str("Enter your username:"))
#
#         if len(username) >= 4 and f"{username}.txt" not in os.listdir():
#             x = 0
#             for ch in username:
#                 if ch in '!"#$%&\'*()+,/:;<=>?@[\\]^`{|}~':
#                     x = 1
#             if x == 0:
#                 break
#             else:
#                 print("Error: username cannot contain any of these characters !\"#$%&\'*+,/:;<=>?@[\\]^`{|}~")
#         else:
#             if len(username) < 4:
#                 print("Error: username must have at least 4 characters")
#             else:
#                 print("username already used")
#     os.chdir(main_path)
#     return username
#
# print(get_hero_name())
#
# def get_correct_int_input(message) -> int:
#     """
#
#     :return:
#     """
#     while True:
#         try:
#             age = int(input(message))
#         except ValueError:
#             print(f'error input must be written with digits')
#         else:
#             break
#     return age
# #
# # print(get_correct_age("Choose a hero by writing his coresponding number: "))
#
#
# def get_correct_int_input(message) -> int:
#     """
#
#     :return:
#     """
#     while True:
#         try:
#             age = int(input(message))
#         except ValueError:
#             print(f'error input must be written with digits')
#         else:
#             break
#     return age
#
#
# def get_hero_symbol(hero_name):
#     """
#
#     :param hero_class:
#     :return:
#     """
#     output = ""
#     changed_directory = 0
#     main_path = os.getcwd()
#     if main_path != "C:\\Users\\andre\\PycharmProjects\\" \
#                     "The-Big-Book-of-Small-Python-Projects-solved-by-ramuica-\\Angeilic Powers\\Your_characters":
#         os.chdir("Your_characters")
#         changed_directory = 1
#     for item_f in os.listdir():
#         if item_f == f"{hero_name}.txt":
#             with open(item_f, "r") as fr:
#                 content = fr.readlines()
#     hero_and_class = {"wizard": "🧙", "shadow": "👤", "vampire": "🧛", "fairy": "🧚", "triton": "🧜", "spirit": "🧞"}
#     for k, v in hero_and_class.item_fs():
#         if k == content[0].strip():
#             output = v
#     if changed_directory == 1:
#         os.chdir(main_path)
#     return output
#
#
# def play_existing_hero():
#     """
#
#     :return:
#     """
#     main_path = os.getcwd()
#     os.chdir("Your_characters")
#     while True:
#         print("\nChoose what hereo do you want to play:")
#         for i, item_f in enumerate(os.listdir()):
#             symbol = get_hero_symbol(item_f[0:-4])
#             print(f"{item_f[0:-4]}{symbol}({i + 1})")
#         option = get_correct_int_input("\nChoose a hero by writing his coresponding number: ")
#         if 0 < option <= len(os.listdir()):
#             output = os.listdir()[option - 1]
#             break
#         else:
#             print("the option you choose doesn't correspond to any hero")
#     os.chdir(main_path)
#     return output
#
#
# print(play_existing_hero())
# # print(get_hero_symbol("Ardeiul iute"))
#
# # for i in range(200):
# #     print(i)
# #     print(f"\033[{str(i)}m RAMULICA")
# def get_random_rarity(difficulty):
#     """
#
#     :param difficulty:
#     :return:
#     """
#     red_item_f = 15 * difficulty
#     grren_item_f = 50 * difficulty
#     yellow_item_f = 500 * difficulty
#     blue_item_f = 1300 * difficulty
#     black_chance = 10000 - blue_item_f - yellow_item_f - grren_item_f - red_item_f
#     list_chances = ["\033[1;30;40m"] * (black_chance) + ["\033[1;30;44m"] * (blue_item_f) + ["\033[1;30;43m"] * \
#                    (yellow_item_f) + ["\033[1;30;42m"] * (grren_item_f) + ["\033[1;30;41m"] * (red_item_f)
#     return random.choice(list_chances)
#
# for _ in range(1000):
#     print(f"{get_random_rarity(5)}item_f")


# def random_secondary_stat(rarity):
#     """
#
#     :param rarity:
#     :return:
#     """
#     stat_factor = {"armor": 1, "hp": 10, "crit": 0.2, "crit dmg": 1, "speed": 1, "mr": 1,
#                    "dodge": 0.4, "control immunity": 0.2, "mana": 0.2}
#
#     stat_name = random.choice(list(stat_factor.keys()))
#
#     if rarity == "\033[1;30;40m":
#         return f"{stat_name}: {round(random.choice(range(2, 5)) * stat_factor[stat_name], 1)}"
#     elif rarity == "\033[1;30;44m":
#         return f"{stat_name}: {round(random.choice(range(4, 12)) * stat_factor[stat_name], 1)}"
#     elif rarity == "\033[1;30;43m":
#         return f"{stat_name}: {round(random.choice(range(10, 25)) * stat_factor[stat_name], 1)}"
#     elif rarity == "\033[1;30;42m":
#         return f"{stat_name}: {round(random.choice(range(50, 100)) * stat_factor[stat_name], 1)}"
#     elif rarity == "\033[1;30;41m":
#         return f"{stat_name}: {round(200 * stat_factor[stat_name], 1)}"
#
# print(random_secondary_stat("\033[1;30;43m"))
#
# list_1 = ['empt',' empt', 'empt']
#
# print(list_1.index("empty"))

# def colors_16(color_):
#     return("\033[2;{num}m {num} \033[0;0m".format(num=str(color_)))
#
#
# def colors_256(color_):
#     num1 = str(color_)
#     num2 = str(color_).ljust(3, ' ')
#     if color_ % 16 == 0:
#         return(f"\033[38;5;{num1}m {num2} \033[0;0m\n")
#     else:
#         return(f"\033[38;5;{num1}m {num2} \033[0;0m")
#
# print("The 16 colors scheme is:")
# print(' '.join([colors_16(x) for x in range(30, 38)]))
# print("\nThe 256 colors scheme is:")
# print(' '.join([colors_256(x) for x in range(256)]))
#
#
# print("\033[48;5;208m236")
#
# def add_random_doors():
#     door_wall = ["up", "down"]
#     for _ in range(5):
#         if door_wall[-1] == "down":
# #             door_wall.extend(random.choice([['up', 'down'], ['right', 'left'], ['left', 'right']]))
# #         elif door_wall[-1] == "up":
# #             door_wall.extend(random.choice([['down', 'up'], ['right', 'left'], ['left', 'right']]))
# #         elif door_wall[-1] == "left":
# #             door_wall.extend(random.choice([['down', 'up'], ['right', 'left'], ['up', 'down']]))
# #         elif door_wall[-1] == "right":
# #             door_wall.extend(random.choice([['down', 'up'], ['up', 'down'], ['left', 'right']]))
# #     return door_wall
# #
# # print(add_random_doors())
# print(len("⛩"))
# import random
# import os
#
#
# def get_answer() -> bool:
#     """
#     functions gets an answer which decides if
#     some actions will be done
#     :return:
#     """
#     x = input(str("press y for yes or n for no:"))
#     while x != "y" and x != "n":
#         print("you have entered a wrong answer")
#         x = input(str("press y for yes or n for no:"))
#     return x == "y"
#
#
# def get_color_biome(biome):
#     """
#
#     :param biome:
#     :return:
#     """
#     color = ""
#     obstacles = ""
#     if biome == "grass":
#         color = "\033[2;32;42m"
#         obstacles = ["🌳", "🌲", "🌾"]
#     elif biome == "snow":
#         color = "\033[2;32;47m"
#         obstacles = ["🎄", "🎁", "⛄"]
#     elif biome == "dessert":
#         color = "\033[2;32;43m"
#         obstacles = ["🏜", "🌴", "🏵"]
#     elif biome == "hell":
#         color = "\033[2;32;41m"
#         obstacles = ["🌋", "🔥", "📍"]
#     elif biome == "unicorn":
#         color = "\033[2;32;45m"
#         obstacles = ["🌈", "🍧", "🌺", "🦄"]
#
#     return color, obstacles
#
#
# def get_correct_int_input(message) -> int:
#     """
#
#     :return:
#     """
#     while True:
#         try:
#             age = int(input(message))
#         except ValueError:
#             print(f'error input must be written with digits')
#         else:
#             break
#     return age
#
#
# def generate_room_length_height():
#     """
#
#     :return:
#     """
#     length = random.choice(range(8, 12))
#     height = random.choice(range(6, 9))
#     return length, height
#
#
# def generate_rooms(biome: str, length: int, height: int) -> list:
#     """
#     "🧙‍" +🌳🌲🌾⛄🎁🎄
#     :return:
#     """
#     output = []
#     color, obstacles = get_color_biome(biome)
#     output.append(("  " * (length + 2)))
#     for i in range(height):
#         obstacle_column = [random.choice(range(length)) for _ in range(random.choice(range(1, 3)))]
#         obstacle_column.sort()
#         obstacle_column.append(" ")
#         # print(obstacle_column)
#         # print(obstacle_column[0])
#         obstacle_count = 0
#         row = ""
#         for i_1 in range(length):
#             if i_1 == obstacle_column[obstacle_count]:
#                 row += f"{random.choice(obstacles)}"
#                 obstacle_count += 1
#             else:
#                 row += f"  "
#         output.append(row)
#     output.append(("  " * (length + 2)))
#
#     return output
#
#
# def print_room(room: str, biome: str):
#     """
#
#     :param room:
#     :param biome:
#     :return:
#     """
#     print(f"\033[2;32;40m{room[0]}\033[0;0m")
#     color, obstacles = get_color_biome(biome)
#     margins = '\033[2;32;40m  '
#     for item_f in room[1:-1]:
#         print(f"{margins}{color}{item_f}{margins}\033[0;0m")
#     print(f"\033[2;32;40m{room[-1]}\033[0;0m")
#
#
# def get_random_biome() -> str:
#     """
#
#     :return:
#     """
#     return random.choice(["grass", "snow", "dessert", "hell", "unicorn"])
#
#
# def add_object_on_map(room: list, hero: str, column: int, row: int):
#     """
#     :param hero:
#     :param room:
#     :param column:
#     :param row:
#     :return:
#     """
#     column = column - 1
#     output = []
#     count_row_positions = 0
#     count_row_positions_actions = 0
#
#     for i, item_f in enumerate(room):
#         if i == row:
#             if column == 0:
#                 if item_f[0] == " ":
#                     output.append(f"{hero}{item_f[2::]}")
#                 else:
#                     output.append(f"{hero}{item_f[1::]}")
#             else:
#                 for ch in item_f:
#
#                     if ch == " ":
#                         count_row_positions += 1
#                         count_row_positions_actions += 1
#                     elif ch != " ":
#                         count_row_positions += 1
#                         count_row_positions_actions += 2
#
#                     if count_row_positions_actions >= column * 2:
#                         break
#
#                 output.append(f"{item_f[0:count_row_positions]}{hero}{item_f[count_row_positions + 1::]}")
#         else:
#             output.append(item_f)
#     return output
#
#
# def choose_door(biome: str):
#     """
#
#     :param biome:
#     :return:
#     """
#     dor = ""
#     if biome == "grass":
#         dor = "⛩"
#     elif biome == "snow":
#         dor = "🏛"
#     elif biome == "dessert":
#         dor = "🛕"
#     elif biome == "hell":
#         dor = "⛩"
#     elif biome == "unicorn":
#         dor = "🏛"
#     return dor
#
#
# def choose_enemy():
#     """
#
#     :return:
#     """
#     return random.choice(['💀', '👺', '👹', '🕷', '🦂', '👻', '👽', '😈', '🌬', '🎃', '👾', '🐲', "🎭"])
#
#
# def get_hero_name() -> str:
#     """
#     If the username doesn't have unknown characters it returns the name
#     :return:
#     """
#     main_path = os.getcwd()
#     os.chdir("Your_characters")
#     while True:
#         username = input(str("Enter your username:"))
#
#         if len(username) >= 4 and f"{username}.txt" not in os.listdir():
#             x = 0
#             for ch in username:
#                 if ch in '!"#$%&\'*()+,/:;<=>?@[\\]^`{|}~':
#                     x = 1
#             if x == 0:
#                 break
#             else:
#                 print("Error: username cannot contain any of these characters !\"#$%&\'*+,/:;<=>?@[\\]^`{|}~")
#         else:
#             if len(username) < 4:
#                 print("Error: username must have at least 4 characters")
#             else:
#                 print("username already used")
#     os.chdir(main_path)
#     return username
#
#
# def write_hero_data(hero_name: str, hero_class: str, level: str,
#                     gold: str, materials: dict, gear: dict, inventory: list):
#     """
#
#     :return:
#     """
#
#     main_path = os.getcwd()
#     new_data = [hero_class, level, gold]
#     for k, v in materials.item_fs():
#         new_data.append(f"{v}")
#     for k_1, v_1 in gear.item_fs():
#         new_data.append(f"{v_1}")
#     for item_f in inventory:
#         new_data.append(item_f)
#     os.chdir("Your_characters")
#
#     with open(f"{hero_name}.txt", "w") as fw:
#         for item_f in new_data:
#             fw.write(item_f + "\n")
#
#     os.chdir(main_path)
#
#
# def read_abilities(selected_hero: str):
#     """
#
#     :param selected_hero:
#     :return:
#     """
#     main_path = os.getcwd()
#     os.chdir("heroes")
#     for item_f in os.listdir():
#         if item_f[0:4] == selected_hero[0:4]:
#             with open(item_f, "r") as fr:
#                 content = fr.readlines()
#     os.chdir(main_path)
#     output = [item_f.strip() for item_f in content]
#     for item_f in output:
#         print(item_f)
#
#
# def create_hero():
#     """
#
#     :return:
#     """
#     name = ""
#     main_while_break = 0
#     print("")
#     print(
#         "Choose a class for your hero:\nWizard(🧙)\nShadow(👤‍)\nVampire(🧛‍)\nfairy.txt(🧚‍)\nTriton(🧜)\nSpirit(🧞‍)")
#     hero_class = str.lower(input("Choose one option by writing the class name:"))
#     classes = ["wizard", "shadow", "vampire", "fairy", "triton", "spirit"]
#     while True:
#
#         while hero_class not in classes:
#             print("incorrect class, try again")
#             hero_class = str.lower(input("Choose one option by writing the class name:"))
#         with open("hero_class_description", "r") as fr:
#             content = fr.readlines()
#         for item_f in content:
#             if str.lower(item_f[0:4]) == str.lower(hero_class[0:4]):
#                 print(f"\n{item_f}\n")
#         print("Choose one option:\ngo back(b)\nchoose class(c)\nread abilities(a)")
#         option = str.lower(input("Your option:"))
#         while option:
#             if option not in ["c", "b", "a"]:
#                 print("option is incorrect")
#             elif option == "a":
#                 read_abilities(hero_class)
#             elif option == "c":
#                 item_fs_0 = {"helm": "empty_", "chest": "empty_", "boots": "empty_", "weapon": "empty_",
#                            "sec_weapon": "empty_", "jewel": "empty_"}
#                 materials_0 = {"wood": '0', "iron": '0', "diamond": '0', "angelic dust": '0'}
#                 name = get_hero_name()
#                 write_hero_data(name, hero_class, "0", "500", materials_0, item_fs_0, ["empty_"] * 18)
#                 main_while_break = 1
#                 break
#             else:
#                 break
#             print("\nChoose one option:\ngo back(b)\nchoose class(c)\nread abilities(a)")
#             option = str.lower(input("Your option:"))
#
#         if main_while_break == 1:
#             break
#         else:
#             print("")
#             print("Choose a class for your hero:\nWizard(🧙)\nShadow(👤‍)\nVampire(🧛‍)"
#                   "\nfairy.txt(🧚‍)\nTriton(🧜)\nSpirit(🧞‍)")
#             hero_class = str.lower(input("Choose one option by writing the class name:"))
#             classes = ["wizard", "shadow", "vampire", "fairy", "triton", "spirit"]
#     return f"{name}.txt"
#
#
# def get_hero_symbol(hero_name):
#     """
#
#     :param hero_name:
#     :return:
#     """
#     output = ""
#     changed_directory = 0
#     main_path = os.getcwd()
#     if main_path != "C:\\Users\\andre\\PycharmProjects\\" \
#                     "The-Big-Book-of-Small-Python-Projects-solved-by-ramuica-\\Angelic Powers\\Your_characters":
#         os.chdir("Your_characters")
#         changed_directory = 1
#     for item_f in os.listdir():
#         if item_f == f"{hero_name}.txt":
#             with open(item_f, "r") as fr:
#                 content = fr.readlines()
#     hero_and_class = {"wizard": "🧙", "shadow": "👤", "vampire": "🧛", "fairy": "🧚", "triton": "🧜", "spirit": "🧞"}
#     for k, v in hero_and_class.item_fs():
#         if k == content[0].strip():
#             output = v
#     if changed_directory == 1:
#         os.chdir(main_path)
#     return output
#
#
# def get_item_f_symbol(item_f):
#     """
#
#     :param item_f:
#     :return:
#     """
#
#     output = ""
#     dict_item_fs = {"crown": "👑", "wand": "🎆",
#                   "the_eye": "🧿", "robe": "👘",
#                   "talisman": "🎐", "boots": "👢"}
#
#     for k, v in dict_item_fs.item_fs():
#         if item_f == k:
#             output = v
#             break
#     return output
#
#
# def play_existing_hero():
#     """
#
#     :return:
#     """
#     main_path = os.getcwd()
#     os.chdir("Your_characters")
#     while True:
#         print("\nChoose what hero do you want to play:")
#         for i, item_f in enumerate(os.listdir()):
#             symbol = get_hero_symbol(item_f[0:-4])
#             print(f"{item_f[0:-4]}{symbol}({i + 1})")
#         option = get_correct_int_input("\nChoose a hero by writing his corresponding number: ")
#         if 0 < option <= len(os.listdir()):
#             output = os.listdir()[option - 1]
#             break
#         else:
#             print("the option you choose doesn't correspond to any hero")
#     os.chdir(main_path)
#     return output
#
#
# def decide_what_hero_to_play():
#     """
#
#     :return:
#     """
#     while True:
#         print("Do you want to create a new hero or to play an existing one?\nCreate(c)\nChoose existing hero(e)")
#         option = input("\nChoose an option by writing his corresponding letter: ")
#         if option == "e":
#             print(play_existing_hero())
#             break
#         elif option == "c":
#             print(create_hero())
#             break
#         else:
#             print("\nthe letter you choose doesn't correspond to any option. Try again\n")
#
#
# def read_inventory(file):
#     """
#
#     :param file:
#     :return:
#     """
#     main_path = os.getcwd()
#     os.chdir("Your_characters")
#     with open(file, "r") as fr:
#         content = fr.readlines()
#     os.chdir(main_path)
#     inventory = [item_f.strip() for item_f in content]
#     return inventory
#
#
# def get_random_rarity(difficulty):
#     """
#
#     :param difficulty:
#     :return:
#     """
#     red_item_f = 10 * difficulty
#     grren_item_f = 50 * difficulty
#     yellow_item_f = 500 * difficulty
#     blue_item_f = 1300 * difficulty
#     black_chance = 10000 - blue_item_f - yellow_item_f - grren_item_f - red_item_f
#     list_chances = ["common"] * (black_chance) + ["normal"] * (blue_item_f) + ["rare"] * \
#                    (yellow_item_f) + ["legendary"] * (grren_item_f) + ["angelic"] * (red_item_f)
#     return random.choice(list_chances)
#
#
# def get_rarity_color(rarity):
#     if rarity == "common":
#         return "\033[40m", "\033[30m"
#     elif rarity == "normal":
#         return "\033[44m", "\033[34m"
#     elif rarity == "rare":
#         return "\033[43m", "\033[33m"
#     elif rarity == "legendary":
#         return "\033[42m", "\033[32m"
#     elif rarity == "angelic":
#         return "\033[41m", "\033[31m"
#
#
# def print_inventory(file):
#     """
#
#     :param file:
#     :return:
#     """
#
#     symbol = get_hero_symbol(file[0:-4])
#     inventory = read_inventory(file)
#     print(f"\033[4m{' ' * 30}\033[0;0m ")
#     print(f"|\033[95m{file[0:-4]}  lv: {inventory[1]}\033[0;0m "
#           f"{' ' * (21 - len(file[0:-4]) - len(str(inventory[1])))}|")
#     print(f"|  \033[1;30;45m|{symbol}|\033[2;37;0m{' ' * 10}\033[1;30;47m{item_f_colored_symbol(inventory[12])}\033[0;0m "
#           f"\033[1;30;47m{item_f_colored_symbol(inventory[7])}\033[2;37;0m{' ' * 7}|")
#     print(f"|\033[32mwood: {inventory[3]}\033[0;0m{' ' * (22 - len(str(inventory[3])))}|")
#     print(f"|\033[38msilver: {inventory[4]}\033[0;0m"
#           f"{' ' * (8 - len(str(inventory[4])))}\033[1;30;47m{item_f_colored_symbol(inventory[10])}\033[0;0m "
#           f"\033[1;30;47m{item_f_colored_symbol(inventory[8])}\033[0;0m \033[1;30;47m{item_f_colored_symbol(inventory[11])}\033[0;0m"
#           f"{' ' * 3}|")
#     print(f"|\033[34mdiamond: {inventory[5]}\033[0;0m{' ' * (19 - len(str(inventory[5])))}|")
#     print(f"|\033[31mangelic dust: {inventory[6]}\033[0;0m{' ' * (5 - len(str(inventory[6])))}\033[1;30;47m"
#           f"{item_f_colored_symbol(inventory[9])}\033[0;0m"
#           f"{' ' * 7}|")
#     print(f"|\033[33mgold: {inventory[2]}\033[0;0m{' ' * (22 - len(str(inventory[2])))}|")
#     row_1 = ""
#     row_2 = ""
#     row_3 = ""
#     row_counter = 1
#     for item_f in inventory[13::]:
#         if row_counter <= 6:
#             row_1 += f"{item_f_colored_symbol(item_f)}  "
#         elif row_counter <= 12:
#             row_2 += f"{item_f_colored_symbol(item_f)}  "
#         elif row_counter <= 18:
#             row_3 += f"{item_f_colored_symbol(item_f)}  "
#         row_counter += 1
#     if row_counter < 7:
#         row_1 += "\033[1;30;47m  \033[0;0m  " * (7 - row_counter)
#         row_2 += "\033[1;30;47m  \033[0;0m  " * 6
#         row_3 += "\033[1;30;47m  \033[0;0m  " * 6
#     elif row_counter < 13:
#         row_2 += "\033[1;30;47m  \033[0;0m  " * (13 - row_counter)
#         row_3 += "\033[1;30;47m  \033[0;0m  " * 6
#     elif row_counter < 19:
#         row_3 += "\033[1;30;47m  \033[0;0m  " * (19 - row_counter)
#     print(f"|{' ' * 28}|")
#     print(f"|  {row_1} |")
#     print(f"|{' ' * 28}|")
#     print(f"|  {row_2} |")
#     print(f"|{' ' * 28}|")
#     print(f"|  {row_3} |")
#     print(f"|\033[4m{' ' * 28}\033[0;0m|")
#
#
# def random_primary_stat(rarity, ):
#     """
#
#     :return:
#     """
#
#     if rarity == "common":
#         return f"primary: {random.choice(range(2, 5))}"
#     elif rarity == "normal":
#         return f"primary: {random.choice(range(4, 12))}"
#     elif rarity == "rare":
#         return f"primary: {random.choice(range(10, 25))}"
#     elif rarity == "legendary":
#         return f"primary: {random.choice(range(50, 100))}"
#     elif rarity == "angelic":
#         return f"primary: 200"
#
#
# def random_secondary_stat(rarity):
#     """
#
#     :param rarity:
#     :return:
#     """
#     stat_factor = {"armor": 1, "hp": 10, "crit": 0.2, "crit_dmg": 1, "speed": 1, "mr": 1,
#                    "dodge": 0.4, "cc_immun": 0.2, "mana": 0.2}
#
#     stat_name = random.choice(list(stat_factor.keys()))
#
#     if rarity == "common":
#         return f"{stat_name}: {round(random.choice(range(2, 5)) * stat_factor[stat_name], 1)}"
#     elif rarity == "normal":
#         return f"{stat_name}: {round(random.choice(range(4, 12)) * stat_factor[stat_name], 1)}"
#     elif rarity == "rare":
#         return f"{stat_name}: {round(random.choice(range(10, 25)) * stat_factor[stat_name], 1)}"
#     elif rarity == "legendary":
#         return f"{stat_name}: {round(random.choice(range(50, 100)) * stat_factor[stat_name], 1)}"
#     elif rarity == "angelic":
#         return f"{stat_name}: {round(200 * stat_factor[stat_name], 1)}"
#
#
# def create_item_f(item_f_name, difficulty):
#     """
#
#     :param item_f_name:
#     :param difficulty:
#     :return:
#     """
#     rarity = get_random_rarity(difficulty)
#     return f"{item_f_name} {rarity} {random_primary_stat(rarity)}" \
#            f" {random_secondary_stat(rarity)} {random_secondary_stat(rarity)} {random_secondary_stat(rarity)}"
#
#
# def print_item_f(item_f):
#     """
#
#     :param item_f:
#     :return:
#     """
#     item_f_l = item_f.split()
#
#     item_f_color, text_color = get_rarity_color(item_f_l[1])
#     print(f" {text_color}{'_' * 16}\033[0;0m ")
#     print(
#         f"{text_color}|\033[0;0m{item_f_l[0]}{' ' * (15 - len(item_f_l[0]) - len(item_f_l[1]))}{text_color}{item_f_l[1]} |")
#     print(
#         f"{text_color}|\033[0;0m {item_f_color}{get_item_f_symbol(item_f_l[0])}\033[0;0m{' ' * 13}{text_color}|\033[0;0m")
#     print(f"{text_color}|{' ' * 16}|\033[0;0m")
#     print(
#         f"{text_color}|\033[0;0m {item_f_l[2]} {item_f_l[3]}\033[0;0m{' ' * (14 - len(item_f_l[2]) - len(item_f_l[3]))}{text_color}|\033[0;0m")
#     print(
#         f"{text_color}|\033[0;0m {item_f_l[4]} {item_f_l[5]}\033[0;0m{' ' * (14 - len(item_f_l[4]) - len(item_f_l[5]))}{text_color}|\033[0;0m")
#     print(
#         f"{text_color}|\033[0;0m {item_f_l[6]} {item_f_l[7]}\033[0;0m{' ' * (14 - len(item_f_l[6]) - len(item_f_l[7]))}{text_color}|\033[0;0m")
#     print(
#         f"{text_color}|\033[0;0m {item_f_l[8]} {item_f_l[9]}\033[0;0m{' ' * (14 - len(item_f_l[8]) - len(item_f_l[9]))}{text_color}|\033[0;0m")
#     print(f"{text_color}|{'_' * 16}|\033[0;0m")
#
#
# def item_f_colored_symbol(item_f):
#     """
#
#     :param item_f:
#     :return:
#     """
#     if item_f == "empty":
#         return "\033[1;30;47m⬛\033[0;0m"
#     else:
#         item_f_l = item_f.split()
#         item_f_color, text_color = get_rarity_color(item_f_l[1])
#         return f"{item_f_color}{get_item_f_symbol(item_f_l[0])}\033[0;0m"
#
#
# def navigate_inventory(file):
#     """
#
#     :return:
#     """
#     full_inventory = read_inventory(file)
#     inventory = full_inventory[7::]
#
#     print("inventory option:\n-see stats of a weapon(s)\n-equip a weapon(e)\ngo back(b)")
#     option = input("choose one option by writing its corresponding value:")
#     while True:
#         if option == "s":
#             print("Choose item_f:\nhead(0)\nchest(1)\nfeet(2)\nmain hand(3)\n2nd hand(4)\n"
#                   "jewel(5)\ninventory(coresponding number)")
#             option_s = get_correct_int_input("choose one option by writing its corresponding value:")
#             if option_s <= 21:
#                 if inventory[option_s] == "empty":
#                     print("You don't have an item_f in that slot")
#                 else:
#                     print_item_f(inventory[option_s])
#             else:
#                 print("Wrong value entered")
#         elif option == "b":
#             break
#         else:
#             print("wrong value entered")
#         print("inventory option:\n-see stats of a weapon(s)\n-equip a weapon(e)\ngo back(b)")
#         option = input("choose one option by writing its corresponding value:")
#
#
# def hero_movement(file, column: int, row: int, max_column: int, max_row: int):
#     """
#
#     :param column:
#     :param row:
#     :param max_column:
#     :param max_row:
#     :return:
#     """
#     print("You can move by entering a sequence of movements:\n-go up(w)\n-go left(a)\n-go down(s)\n-go right(d)\n\n"
#           "Other options:\nsee inventory(i)\nexit(e)")
#     movement = str.lower(input("enter a sequence of movements:"))
#     correct_movement = 0
#     while True:
#         if movement == "i":
#             print_inventory(file)
#             navigate_inventory(file)
#         elif movement == "e":
#             print("Are you sure you want to exit?")
#             if get_answer():
#                 return 0, 0
#         else:
#             row_func = row
#             column_func = column
#             while True:
#                 for ch in movement:
#                     if ch not in "wasd":
#                         print("incorrect sequence")
#                         break
#                 else:
#                     for ch in movement:
#                         if ch == "w":
#                             row_func -= 1
#                         if ch == "s":
#                             row_func += 1
#                         if ch == "a":
#                             column_func -= 1
#                         if ch == "d":
#                             column_func += 1
#                 if 0 < column_func <= max_column and 0 < row_func <= max_row:
#                     return column_func, row_func
#                 else:
#                     print("incorrect movement")
#                     break
#         movement = str.lower(input("enter a sequence of movements:"))
#
#
# def village():
#     """
#
#     :return:
#     """
#     return ["", f"{'  ' * 2}⚒{'  ' * 3}‼", f"{'  ' * 7}", f"{'  ' * 3}⛲{'  ' * 3}", f"{'  ' * 7}",
#             f"💍{'  ' * 2}💰{'  ' * 3}"]
#
#
# def print_village(village):
#     margin = f"\033[48;5;0m{' ' * 2}\033[0;0m"
#     print(f"\033[48;5;0m{' ' * 22}\033[0;0m")
#     print(f"\033[48;5;0m{'  ' * 2}\033[48;5;28m🏘🏠⛪\033[48;5;0m{'  ' * 2}\033[48;5;28m🏚🏤\033[48;5;0m   \033[0;0m")
#
#     print(f"{margin}{margin}\033[48;5;28m{village[1]}⛪{margin}")
#     print(f"{margin}{margin}\033[48;5;28m{village[2]}{margin}{margin}")
#     print(f"{margin}{margin}\033[48;5;28m{village[3]}{margin}{margin}")
#     print(f"{margin}\033[48;5;28m🏰{village[4]}{margin}{margin}")
#     print(f"{margin}\033[48;5;28m💒{village[5]}🏚{margin}")
#     print(f"\033[48;5;0m{'  ' * 1}\033[48;5;28m🏘🏠\033[48;5;0m{'  ' * 2}\033[48;5;28m🏚🏤\033[48;5;0m {'  ' * 3}\033[0;0m")
#     print(f"\033[48;5;0m{' ' * 22}\033[0;0m")
#
#
# def village_interface():
#     column_v, row_v = 1, 3
#     print(f"instructions")
#     village_with_hero = add_object_on_map(village(), "🧙‍", column_v, row_v)
#     print_village(village_with_hero)
#     while True:
#         column_v, row_v = hero_movement("ramulica.txt", column_v, row_v, 7, 5)
#         print(column_v, row_v)
#         if column_v == 0 and row_v == 0:
#             return False
#         else:
#             village_with_hero = add_object_on_map(village(), "🧙", column_v, row_v)
#             print_village(village_with_hero)
#             if column_v == 7 and row_v == 1:
#                 print("Do you want to go in a mission?")
#                 if get_answer():
#                     return True
#             elif column_v == 1 and row_v == 5:
#                 print("Do you want to buy something from jeweler?")
#                 if get_answer():
#                     print("make jeweler interface")
#             elif column_v == 4 and row_v == 5:
#                 print("Do you want to buy something from shop?")
#                 if get_answer():
#                     print("make shop interface")
#             elif column_v == 3 and row_v == 1:
#                 print("Do you want to craft something at the blacksmith?")
#                 if get_answer():
#                     print("make blacksmith interface")
#
#
# def margin_random_generator(column, row):
#     cl_rw = ["x", "y"]
#     random.shuffle(cl_rw)
#     if cl_rw[0] == "x":
#         return [random.choice([column, 1]), random.choice(range(1, row))]
#     else:
#         return [random.choice(range(1, column)), random.choice([row, 1])]
#
#
# def door_data(entrance, biome, column, row, next_room):
#     if entrance == "up":
# #         return random.choice(range(2, column - 1)), 1, next_room, choose_door(biome)
# #     elif entrance == "down":
# #         return random.choice(range(2, column - 1)), row, next_room, choose_door(biome)
# #     elif entrance == "right":
# #         return column, random.choice(range(2, row - 1)), next_room, choose_door(biome)
# #     elif entrance == "left":
# #         return 1, random.choice(range(2, row - 1)), next_room, choose_door(biome)
# #
# #
# # class Map:
# #     room_index = 0
# #
# #     def __init__(self, room, entrance, exit, length, height):
# #         self.entrance = entrance
# #         room_m = add_object_on_map(room, self.entrance[3], self.entrance[0], self.entrance[1])
# #         self.exit = exit
# #         room_m = add_object_on_map(room_m, self.exit[3], self.exit[0], self.exit[1])
# #
# #         self.enemy_1 = margin_random_generator(length, height), choose_enemy()
# #         room_m = add_object_on_map(room_m, self.enemy_1[1], self.enemy_1[0][0], self.enemy_1[0][1])
# #         self.enemy_2 = margin_random_generator(length, height), choose_enemy()
# #         room_m = add_object_on_map(room_m, self.enemy_2[1], self.enemy_2[0][0], self.enemy_2[0][1])
# #         self.enemy_3 = margin_random_generator(length, height), choose_enemy()
# #         room_m = add_object_on_map(room_m, self.enemy_3[1], self.enemy_3[0][0], self.enemy_3[0][1])
# #         if random.choice([True, False]):
# #             self.enemy_4 = [random.choice(range(1, length)), random.choice(range(1, height))], choose_enemy()
# #             room_m = add_object_on_map(room_m, self.enemy_4[1], self.enemy_4[0][0], self.enemy_4[0][1])
# #         if random.choice([True, False]):
# #             self.enemy_5 = [random.choice(range(1, length)), random.choice(range(1, height))], choose_enemy()
# #             room_m = add_object_on_map(room_m, self.enemy_5[1], self.enemy_5[0][0], self.enemy_5[0][1])
# #         if random.choice([True, False]):
# #             self.enemy_6 = [random.choice(range(1, length)), random.choice(range(1, height))], choose_enemy()
# #             room_m = add_object_on_map(room_m, self.enemy_6[1], self.enemy_6[0][0], self.enemy_6[0][1])
# #         self.room = room_m
# #         self.room_index = Map.room_index
# #         Map.room_index += 1
# #
# #     def move_to_room(self, room_index):
# #         if self.room_index == room_index:
# #             return self.room
# #
# #
# # def add_random_doors():
# #     door_wall = ["up", "down"]
# #     for _ in range(5):
# #         if door_wall[-1] == "down":
# #             door_wall.extend(random.choice([['up', 'down'], ['right', 'left'], ['left', 'right']]))
# #         elif door_wall[-1] == "up":
# #             door_wall.extend(random.choice([['down', 'up'], ['right', 'left'], ['left', 'right']]))
# #         elif door_wall[-1] == "left":
# #             door_wall.extend(random.choice([['down', 'up'], ['right', 'left'], ['up', 'down']]))
# #         elif door_wall[-1] == "right":
# #             door_wall.extend(random.choice([['down', 'up'], ['up', 'down'], ['left', 'right']]))
# #     return door_wall[1::]
#
#
# import random
# import os
#
#
# def get_answer() -> bool:
#     """
#     functions gets an answer which decides if
#     some actions will be done
#     :return:
#     """
#     x = input(str("press y for yes or n for no:"))
#     while x != "y" and x != "n":
#         print("you have entered a wrong answer")
#         x = input(str("press y for yes or n for no:"))
#     return x == "y"
#
#
# def get_color_biome(biome):
#     """
#
#     :param biome:
#     :return:
#     """
#     color = ""
#     obstacles = ""
#     if biome == "grass":
#         color = "\033[2;32;42m"
#         obstacles = ["🌳", "🌲", "🌾"]
#     elif biome == "snow":
#         color = "\033[2;32;47m"
#         obstacles = ["🎄", "🎁", "⛄"]
#     elif biome == "dessert":
#         color = "\033[2;32;43m"
#         obstacles = ["🏜", "🌴", "🏵"]
#     elif biome == "hell":
#         color = "\033[2;32;41m"
#         obstacles = ["🌋", "🔥", "📍"]
#     elif biome == "unicorn":
#         color = "\033[2;32;45m"
#         obstacles = ["🌈", "🍧", "🌺", "🦄"]
#
#     return color, obstacles
#
#
# def get_correct_int_input(message) -> int:
#     """
#
#     :return:
#     """
#     while True:
#         try:
#             age = int(input(message))
#         except ValueError:
#             print(f'error input must be written with digits')
#         else:
#             break
#     return age
#
#
# def generate_room_length_height():
#     """
#
#     :return:
#     """
#     length = random.choice(range(8, 12))
#     height = random.choice(range(6, 9))
#     return length, height
#
#
# def generate_rooms(biome: str, length: int, height: int) -> list:
#     """
#     "🧙‍" +🌳🌲🌾⛄🎁🎄
#     :return:
#     """
#     output = []
#     color, obstacles = get_color_biome(biome)
#     output.append(("  " * (length + 2)))
#     for i in range(height):
#         obstacle_column = [random.choice(range(length)) for _ in range(random.choice(range(1, 3)))]
#         obstacle_column.sort()
#         obstacle_column.append(" ")
#         # print(obstacle_column)
#         # print(obstacle_column[0])
#         obstacle_count = 0
#         row = ""
#         for i_1 in range(length):
#             if i_1 == obstacle_column[obstacle_count]:
#                 row += f"{random.choice(obstacles)}"
#                 obstacle_count += 1
#             else:
#                 row += f"  "
#         output.append(row)
#     output.append(("  " * (length + 2)))
#
#     return output
#
#
# def print_room(room: str, biome: str):
#     """
#
#     :param room:
#     :param biome:
#     :return:
#     """
#     print(f"\033[2;32;40m{room[0]}\033[0;0m")
#     color, obstacles = get_color_biome(biome)
#     margins = '\033[2;32;40m  '
#     for item_f in room[1:-1]:
#         print(f"{margins}{color}{item_f}{margins}\033[0;0m")
#     print(f"\033[2;32;40m{room[-1]}\033[0;0m")
#
#
# def get_random_biome() -> str:
#     """
#
#     :return:
#     """
#     return random.choice(["grass", "snow", "dessert", "hell", "unicorn"])
#
#
# def add_object_on_map(room: list, hero: str, column: int, row: int):
#     """
#     :param hero:
#     :param room:
#     :param column:
#     :param row:
#     :return:
#     """
#     column = column - 1
#     output = []
#     count_row_positions = 0
#     count_row_positions_actions = 0
#
#     for i, item_f in enumerate(room):
#         if i == row:
#             if column == 0:
#                 if item_f[0] == " ":
#                     output.append(f"{hero}{item_f[2::]}")
#                 else:
#                     output.append(f"{hero}{item_f[1::]}")
#             else:
#                 for ch in item_f:
#
#                     if ch == " ":
#                         count_row_positions += 1
#                         count_row_positions_actions += 1
#                     elif ch != " ":
#                         count_row_positions += 1
#                         count_row_positions_actions += 2
#
#                     if count_row_positions_actions >= column * 2:
#                         break
#
#                 output.append(f"{item_f[0:count_row_positions]}{hero}{item_f[count_row_positions + 1::]}")
#         else:
#             output.append(item_f)
#     return output
#
#
# def choose_door(biome: str):
#     """
#
#     :param biome:
#     :return:
#     """
#     dor = ""
#     if biome == "grass":
#         dor = "⛩"
#     elif biome == "snow":
#         dor = "🏛"
#     elif biome == "dessert":
#         dor = "🛕"
#     elif biome == "hell":
#         dor = "⛩"
#     elif biome == "unicorn":
#         dor = "🏛"
#     return dor
#
#
# def choose_enemy():
#     """
#
#     :return:
#     """
#     return random.choice(['💀', '👺', '👹', '🕷', '🦂', '👻', '👽', '😈', '🌬', '🎃', '👾', '🐲', "🎭"])
#
#
# def get_hero_name() -> str:
#     """
#     If the username doesn't have unknown characters it returns the name
#     :return:
#     """
#     main_path = os.getcwd()
#     os.chdir("Your_characters")
#     while True:
#         username = input(str("Enter your username:"))
#
#         if len(username) >= 4 and f"{username}.txt" not in os.listdir():
#             x = 0
#             for ch in username:
#                 if ch in '!"#$%&\'*()+,/:;<=>?@[\\]^`{|}~':
#                     x = 1
#             if x == 0:
#                 break
#             else:
#                 print("Error: username cannot contain any of these characters !\"#$%&\'*+,/:;<=>?@[\\]^`{|}~")
#         else:
#             if len(username) < 4:
#                 print("Error: username must have at least 4 characters")
#             else:
#                 print("username already used")
#     os.chdir(main_path)
#     return username
#
#
# def write_hero_data(hero_name: str, hero_class: str, level: str,
#                     gold: str, materials: dict, gear: dict, inventory: list):
#     """
#
#     :return:
#     """
#
#     main_path = os.getcwd()
#     new_data = [hero_class, level, gold]
#     for k, v in materials.item_fs():
#         new_data.append(f"{v}")
#     for k_1, v_1 in gear.item_fs():
#         new_data.append(f"{v_1}")
#     for item_f in inventory:
#         new_data.append(item_f)
#     os.chdir("Your_characters")
#
#     with open(f"{hero_name}.txt", "w") as fw:
#         for item_f in new_data:
#             fw.write(item_f + "\n")
#
#     os.chdir(main_path)
#
#
# def read_abilities(selected_hero: str):
#     """
#
#     :param selected_hero:
#     :return:
#     """
#     main_path = os.getcwd()
#     os.chdir("heroes")
#     for item_f in os.listdir():
#         if item_f[0:4] == selected_hero[0:4]:
#             with open(item_f, "r") as fr:
#                 content = fr.readlines()
#     os.chdir(main_path)
#     output = [item_f.strip() for item_f in content]
#     for item_f in output:
#         print(item_f)
#
#
# def create_hero():
#     """
#
#     :return:
#     """
#     name = ""
#     main_while_break = 0
#     print("")
#     print(
#         "Choose a class for your hero:\nWizard(🧙)\nShadow(👤‍)\nVampire(🧛‍)\nfairy.txt(🧚‍)\nTriton(🧜)\nSpirit(🧞‍)")
#     hero_class = str.lower(input("Choose one option by writing the class name:"))
#     classes = ["wizard", "shadow", "vampire", "fairy", "triton", "spirit"]
#     while True:
#
#         while hero_class not in classes:
#             print("incorrect class, try again")
#             hero_class = str.lower(input("Choose one option by writing the class name:"))
#         with open("hero_class_description", "r") as fr:
#             content = fr.readlines()
#         for item_f in content:
#             if str.lower(item_f[0:4]) == str.lower(hero_class[0:4]):
#                 print(f"\n{item_f}\n")
#         print("Choose one option:\ngo back(b)\nchoose class(c)\nread abilities(a)")
#         option = str.lower(input("Your option:"))
#         while option:
#             if option not in ["c", "b", "a"]:
#                 print("option is incorrect")
#             elif option == "a":
#                 read_abilities(hero_class)
#             elif option == "c":
#                 item_fs_0 = {"helm": "empty_", "chest": "empty_", "boots": "empty_", "weapon": "empty_",
#                            "sec_weapon": "empty_", "jewel": "empty_"}
#                 materials_0 = {"wood": '0', "iron": '0', "diamond": '0', "angelic dust": '0'}
#                 name = get_hero_name()
#                 write_hero_data(name, hero_class, "0", "500", materials_0, item_fs_0, ["empty_"] * 18)
#                 main_while_break = 1
#                 break
#             else:
#                 break
#             print("\nChoose one option:\ngo back(b)\nchoose class(c)\nread abilities(a)")
#             option = str.lower(input("Your option:"))
#
#         if main_while_break == 1:
#             break
#         else:
#             print("")
#             print("Choose a class for your hero:\nWizard(🧙)\nShadow(👤‍)\nVampire(🧛‍)"
#                   "\nfairy.txt(🧚‍)\nTriton(🧜)\nSpirit(🧞‍)")
#             hero_class = str.lower(input("Choose one option by writing the class name:"))
#             classes = ["wizard", "shadow", "vampire", "fairy", "triton", "spirit"]
#     return f"{name}.txt"
#
#
# def get_hero_symbol(hero_name):
#     """
#
#     :param hero_name:
#     :return:
#     """
#     output = ""
#     changed_directory = 0
#     main_path = os.getcwd()
#     if main_path != "C:\\Users\\andre\\PycharmProjects\\" \
#                     "The-Big-Book-of-Small-Python-Projects-solved-by-ramuica-\\Angelic Powers\\Your_characters":
#         os.chdir("Your_characters")
#         changed_directory = 1
#     for item_f in os.listdir():
#         if item_f == f"{hero_name}.txt":
#             with open(item_f, "r") as fr:
#                 content = fr.readlines()
#     hero_and_class = {"wizard": "🧙", "shadow": "👤", "vampire": "🧛", "fairy": "🧚", "triton": "🧜", "spirit": "🧞"}
#     for k, v in hero_and_class.item_fs():
#         if k == content[0].strip():
#             output = v
#     if changed_directory == 1:
#         os.chdir(main_path)
#     return output
#
#
# def get_item_f_symbol(item_f):
#     """
#
#     :param item_f:
#     :return:
#     """
#
#     output = ""
#     dict_item_fs = {"crown": "👑", "wand": "🎆",
#                   "the_eye": "🧿", "robe": "👘",
#                   "talisman": "🎐", "boots": "👢"}
#
#     for k, v in dict_item_fs.item_fs():
#         if item_f == k:
#             output = v
#             break
#     return output
#
#
# def play_existing_hero():
#     """
#
#     :return:
#     """
#     main_path = os.getcwd()
#     os.chdir("Your_characters")
#     while True:
#         print("\nChoose what hero do you want to play:")
#         for i, item_f in enumerate(os.listdir()):
#             symbol = get_hero_symbol(item_f[0:-4])
#             print(f"{item_f[0:-4]}{symbol}({i + 1})")
#         option = get_correct_int_input("\nChoose a hero by writing his corresponding number: ")
#         if 0 < option <= len(os.listdir()):
#             output = os.listdir()[option - 1]
#             break
#         else:
#             print("the option you choose doesn't correspond to any hero")
#     os.chdir(main_path)
#     return output
#
#
# def decide_what_hero_to_play():
#     """
#
#     :return:
#     """
#     while True:
#         print("Do you want to create a new hero or to play an existing one?\nCreate(c)\nChoose existing hero(e)")
#         option = input("\nChoose an option by writing his corresponding letter: ")
#         if option == "e":
#             print(play_existing_hero())
#             break
#         elif option == "c":
#             print(create_hero())
#             break
#         else:
#             print("\nthe letter you choose doesn't correspond to any option. Try again\n")
#
#
# def read_inventory(file):
#     """
#
#     :param file:
#     :return:
#     """
#     main_path = os.getcwd()
#     os.chdir("Your_characters")
#     with open(file, "r") as fr:
#         content = fr.readlines()
#     os.chdir(main_path)
#     inventory = [item_f.strip() for item_f in content]
#     return inventory
#
#
# def get_random_rarity(difficulty):
#     """
#
#     :param difficulty:
#     :return:
#     """
#     red_item_f = 10 * difficulty
#     grren_item_f = 50 * difficulty
#     yellow_item_f = 500 * difficulty
#     blue_item_f = 1300 * difficulty
#     black_chance = 10000 - blue_item_f - yellow_item_f - grren_item_f - red_item_f
#     list_chances = ["common"] * (black_chance) + ["normal"] * (blue_item_f) + ["rare"] * \
#                    (yellow_item_f) + ["legendary"] * (grren_item_f) + ["angelic"] * (red_item_f)
#     return random.choice(list_chances)
#
#
# def get_rarity_color(rarity):
#     if rarity == "common":
#         return "\033[40m", "\033[30m"
#     elif rarity == "normal":
#         return "\033[44m", "\033[34m"
#     elif rarity == "rare":
#         return "\033[43m", "\033[33m"
#     elif rarity == "legendary":
#         return "\033[42m", "\033[32m"
#     elif rarity == "angelic":
#         return "\033[41m", "\033[31m"
#
#
# def print_inventory(file):
#     """
#
#     :param file:
#     :return:
#     """
#
#     symbol = get_hero_symbol(file[0:-4])
#     inventory = read_inventory(file)
#     print(f"\033[4m{' ' * 30}\033[0;0m ")
#     print(f"|\033[95m{file[0:-4]}  lv: {inventory[1]}\033[0;0m "
#           f"{' ' * (21 - len(file[0:-4]) - len(str(inventory[1])))}|")
#     print(f"|  \033[1;30;45m|{symbol}|\033[2;37;0m{' ' * 10}\033[1;30;47m{item_f_colored_symbol(inventory[12])}\033[0;0m "
#           f"\033[1;30;47m{item_f_colored_symbol(inventory[7])}\033[2;37;0m{' ' * 7}|")
#     print(f"|\033[32mwood: {inventory[3]}\033[0;0m{' ' * (22 - len(str(inventory[3])))}|")
#     print(f"|\033[38msilver: {inventory[4]}\033[0;0m"
#           f"{' ' * (8 - len(str(inventory[4])))}\033[1;30;47m{item_f_colored_symbol(inventory[10])}\033[0;0m "
#           f"\033[1;30;47m{item_f_colored_symbol(inventory[8])}\033[0;0m \033[1;30;47m{item_f_colored_symbol(inventory[11])}\033[0;0m"
#           f"{' ' * 3}|")
#     print(f"|\033[34mdiamond: {inventory[5]}\033[0;0m{' ' * (19- len(str(inventory[5])))}|")
#     print(f"|\033[31mangelic dust: {inventory[6]}\033[0;0m{' ' * (5- len(str(inventory[6])))}\033[1;30;47m"
#           f"{item_f_colored_symbol(inventory[9])}\033[0;0m"
#           f"{' ' * 7}|")
#     print(f"|\033[33mgold: {inventory[2]}\033[0;0m{' ' * (22- len(str(inventory[2])))}|")
#     row_1 = ""
#     row_2 = ""
#     row_3 = ""
#     row_counter = 1
#     for item_f in inventory[13::]:
#         if row_counter <= 6:
#             row_1 += f"{item_f_colored_symbol(item_f)}  "
#         elif row_counter <= 12:
#             row_2 += f"{item_f_colored_symbol(item_f)}  "
#         elif row_counter <= 18:
#             row_3 += f"{item_f_colored_symbol(item_f)}  "
#         row_counter += 1
#     if row_counter < 7:
#         row_1 += "\033[1;30;47m  \033[0;0m  " * (7 - row_counter)
#         row_2 += "\033[1;30;47m  \033[0;0m  " * 6
#         row_3 += "\033[1;30;47m  \033[0;0m  " * 6
#     elif row_counter < 13:
#         row_2 += "\033[1;30;47m  \033[0;0m  " * (13 - row_counter)
#         row_3 += "\033[1;30;47m  \033[0;0m  " * 6
#     elif row_counter < 19:
#         row_3 += "\033[1;30;47m  \033[0;0m  " * (19 - row_counter)
#     print(f"|{' ' * 28}|")
#     print(f"|  {row_1} |")
#     print(f"|{' ' * 28}|")
#     print(f"|  {row_2} |")
#     print(f"|{' ' * 28}|")
#     print(f"|  {row_3} |")
#     print(f"|\033[4m{' ' * 28}\033[0;0m|")
#
#
# def random_primary_stat(rarity,):
#     """
#
#     :return:
#     """
#
#     if rarity == "common":
#         return f"primary: {random.choice(range(2, 5))}"
#     elif rarity == "normal":
#         return f"primary: {random.choice(range(4, 12))}"
#     elif rarity == "rare":
#         return f"primary: {random.choice(range(10, 25))}"
#     elif rarity == "legendary":
#         return f"primary: {random.choice(range(50, 100))}"
#     elif rarity == "angelic":
#         return f"primary: 200"
#
#
# def random_secondary_stat(rarity):
#     """
#
#     :param rarity:
#     :return:
#     """
#     stat_factor = {"armor": 1, "hp": 10, "crit": 0.2, "crit_dmg": 1, "speed": 1, "mr": 1,
#                    "dodge": 0.4, "cc_immun": 0.2, "mana": 0.2}
#
#     stat_name = random.choice(list(stat_factor.keys()))
#
#     if rarity == "common":
#         return f"{stat_name}: {round(random.choice(range(2, 5)) * stat_factor[stat_name], 1)}"
#     elif rarity == "normal":
#         return f"{stat_name}: {round(random.choice(range(4, 12)) * stat_factor[stat_name], 1)}"
#     elif rarity == "rare":
#         return f"{stat_name}: {round(random.choice(range(10, 25)) * stat_factor[stat_name], 1)}"
#     elif rarity == "legendary":
#         return f"{stat_name}: {round(random.choice(range(50, 100)) * stat_factor[stat_name], 1)}"
#     elif rarity == "angelic":
#         return f"{stat_name}: {round(200 * stat_factor[stat_name], 1)}"
#
#
# def create_item_f(item_f_name, difficulty):
#     """
#
#     :param item_f_name:
#     :param difficulty:
#     :return:
#     """
#     rarity = get_random_rarity(difficulty)
#     return f"{item_f_name} {rarity} {random_primary_stat(rarity)}" \
#            f" {random_secondary_stat(rarity)} {random_secondary_stat(rarity)} {random_secondary_stat(rarity)}"\
#
#
# def print_item_f(item_f):
#     """
#
#     :param item_f:
#     :return:
#     """
#     item_f_l = item_f.split()
#
#     item_f_color, text_color = get_rarity_color(item_f_l[1])
#     print(f" {text_color}{'_' * 16}\033[0;0m ")
#     print(f"{text_color}|\033[0;0m{item_f_l[0]}{' ' * (15 - len(item_f_l[0]) - len(item_f_l[1]))}{text_color}{item_f_l[1]} |")
#     print(f"{text_color}|\033[0;0m {item_f_color}{get_item_f_symbol(item_f_l[0]) }\033[0;0m{' ' * 13}{text_color}|\033[0;0m")
#     print(f"{text_color}|{' ' * 16}|\033[0;0m")
#     print(f"{text_color}|\033[0;0m {item_f_l[2]} {item_f_l[3]}\033[0;0m{' ' * (14 - len(item_f_l[2]) - len(item_f_l[3]))}{text_color}|\033[0;0m")
#     print(f"{text_color}|\033[0;0m {item_f_l[4]} {item_f_l[5]}\033[0;0m{' ' * (14 - len(item_f_l[4]) - len(item_f_l[5]))}{text_color}|\033[0;0m")
#     print(f"{text_color}|\033[0;0m {item_f_l[6]} {item_f_l[7]}\033[0;0m{' ' * (14 - len(item_f_l[6]) - len(item_f_l[7]))}{text_color}|\033[0;0m")
#     print(f"{text_color}|\033[0;0m {item_f_l[8]} {item_f_l[9]}\033[0;0m{' ' * (14 - len(item_f_l[8]) - len(item_f_l[9]))}{text_color}|\033[0;0m")
#     print(f"{text_color}|{'_' * 16}|\033[0;0m")
#
#
# def item_f_colored_symbol(item_f):
#     """
#
#     :param item_f:
#     :return:
#     """
#     if item_f == "empty":
#         return "\033[1;30;47m⬛\033[0;0m"
#     else:
#         item_f_l = item_f.split()
#         item_f_color, text_color = get_rarity_color(item_f_l[1])
#         return f"{item_f_color}{get_item_f_symbol(item_f_l[0])}\033[0;0m"
#
#
# def navigate_inventory(file):
#     """
#
#     :return:
#     """
#     full_inventory = read_inventory(file)
#     inventory = full_inventory[7::]
#
#     print("inventory option:\n-see stats of a weapon(s)\n-equip a weapon(e)\ngo back(b)")
#     option = input("choose one option by writing its corresponding value:")
#     while True:
#         if option == "s":
#             print("Choose item_f:\nhead(0)\nchest(1)\nfeet(2)\nmain hand(3)\n2nd hand(4)\n"
#                   "jewel(5)\ninventory(coresponding number)")
#             option_s = get_correct_int_input("choose one option by writing its corresponding value:")
#             if option_s <= 21:
#                 if inventory[option_s] == "empty":
#                     print("You don't have an item_f in that slot")
#                 else:
#                     print_item_f(inventory[option_s])
#             else:
#                 print("Wrong value entered")
#         elif option == "b":
#             break
#         else:
#             print("wrong value entered")
#         print("inventory option:\n-see stats of a weapon(s)\n-equip a weapon(e)\ngo back(b)")
#         option = input("choose one option by writing its corresponding value:")
#
#
# def hero_movement(file, column: int, row: int, max_column: int, max_row: int):
#     """
#
#     :param column:
#     :param row:
#     :param max_column:
#     :param max_row:
#     :return:
#     """
#     print("You can move by entering a sequence of movements:\n-go up(w)\n-go left(a)\n-go down(s)\n-go right(d)\n\n"
#           "Other options:\nsee inventory(i)\nexit(e)")
#     movement = str.lower(input("enter a sequence of movements:"))
#     correct_movement = 0
#     while True:
#         if movement == "i":
#             print_inventory(file)
#             navigate_inventory(file)
#         elif movement == "e":
#             print("Are you sure you want to exit?")
#             if get_answer():
#                 return 0, 0
#         else:
#             row_func = row
#             column_func = column
#             while True:
#                 for ch in movement:
#                     if ch not in "wasd":
#                         print("incorrect sequence")
#                         break
#                 else:
#                     for ch in movement:
#                         if ch == "w":
#                             row_func -= 1
#                         if ch == "s":
#                             row_func += 1
#                         if ch == "a":
#                             column_func -= 1
#                         if ch == "d":
#                             column_func += 1
#                 if 0 < column_func <= max_column and 0 < row_func <= max_row:
#                     return column_func, row_func
#                 else:
#                     print("incorrect movement")
#                     break
#         movement = str.lower(input("enter a sequence of movements:"))
#
#
# def village():
#     """
#
#     :return:
#     """
#     return ["", f"{'  ' * 2}⚒{'  ' * 3}‼", f"{'  ' * 7}", f"{'  ' * 3}⛲{'  ' * 3}", f"{'  ' * 7}", f"💍{'  ' * 2}💰{'  ' * 3}"]
#
#
# def print_village(village):
#     margin = f"\033[48;5;0m{' ' * 2}\033[0;0m"
#     print(f"\033[48;5;0m{' ' * 22}\033[0;0m")
#     print(f"\033[48;5;0m{'  ' * 2}\033[48;5;28m🏘🏠⛪\033[48;5;0m{'  ' * 2}\033[48;5;28m🏚🏤\033[48;5;0m   \033[0;0m")
#
#     print(f"{margin}{margin}\033[48;5;28m{village[1]}⛪{margin}")
#     print(f"{margin}{margin}\033[48;5;28m{village[2]}{margin}{margin}")
#     print(f"{margin}{margin}\033[48;5;28m{village[3]}{margin}{margin}")
#     print(f"{margin}\033[48;5;28m🏰{village[4]}{margin}{margin}")
#     print(f"{margin}\033[48;5;28m💒{village[5]}🏚{margin}")
#     print(f"\033[48;5;0m{'  ' * 1}\033[48;5;28m🏘🏠\033[48;5;0m{'  ' * 2}\033[48;5;28m🏚🏤\033[48;5;0m {'  ' * 3}\033[0;0m")
#     print(f"\033[48;5;0m{' ' * 22}\033[0;0m")
#
#
# def village_interface():
#
#     column_v, row_v = 1, 3
#     print(f"instructions")
#     village_with_hero = add_object_on_map(village(), "🧙‍", column_v, row_v)
#     print_village(village_with_hero)
#     while True:
#         column_v, row_v = hero_movement("ramulica.txt", column_v, row_v, 7, 5)
#         print(column_v, row_v)
#         if column_v == 0 and row_v == 0:
#             return False
#         else:
#             village_with_hero = add_object_on_map(village(), "🧙", column_v, row_v)
#             print_village(village_with_hero)
#             if column_v == 7 and row_v == 1:
#                 print("Do you want to go in a mission?")
#                 if get_answer():
#                     return True
#             elif column_v == 1 and row_v == 5:
#                 print("Do you want to buy something from jeweler?")
#                 if get_answer():
#                     print("make jeweler interface")
#             elif column_v == 4 and row_v == 5:
#                 print("Do you want to buy something from shop?")
#                 if get_answer():
#                     print("make shop interface")
#             elif column_v == 3 and row_v == 1:
#                 print("Do you want to craft something at the blacksmith?")
#                 if get_answer():
#                     print("make blacksmith interface")
#
#
# def margin_random_generator(column, row):
#     cl_rw = ["x", "y"]
#     random.shuffle(cl_rw)
#     if cl_rw[0] == "x":
#         return [random.choice([column, 1]), random.choice(range(1, row))]
#     else:
#         return [random.choice(range(1, column)), random.choice([row, 1])]
#
#
# def door_data(entrance, biome, column, row, next_room):
#
#     if entrance == "up":
#         return random.choice(range(2, column - 1)), 1, next_room, choose_door(biome)
#     elif entrance == "down":
#         return random.choice(range(2, column - 1)), row, next_room, choose_door(biome)
#     elif entrance == "right":
#         return column, random.choice(range(2, row - 1)), next_room, choose_door(biome)
#     elif entrance == "left":
#         return 1, random.choice(range(2, row - 1)), next_room, choose_door(biome)
#
#
# class Map:
#     room_index = 0
#     def __init__(self, room, entrance, exit, length, height):
#         self.entrance = entrance
#         room_m = add_object_on_map(room, self.entrance[3], self.entrance[0], self.entrance[1])
#         self.exit = exit
#         room_m = add_object_on_map(room_m, self.exit[3], self.exit[0], self.exit[1])
#
#         self.enemy_1 = margin_random_generator(length, height), choose_enemy()
#         room_m = add_object_on_map(room_m, self.enemy_1[1], self.enemy_1[0][0], self.enemy_1[0][1])
#         self.enemy_2 = margin_random_generator(length, height), choose_enemy()
#         room_m = add_object_on_map(room_m, self.enemy_2[1], self.enemy_2[0][0], self.enemy_2[0][1])
#         self.enemy_3 = margin_random_generator(length, height), choose_enemy()
#         room_m = add_object_on_map(room_m, self.enemy_3[1], self.enemy_3[0][0], self.enemy_3[0][1])
#         if random.choice([True, False]):
#
#             self.enemy_4 = [random.choice(range(1, length)), random.choice(range(1, height))], choose_enemy()
#             room_m = add_object_on_map(room_m, self.enemy_4[1], self.enemy_4[0][0], self.enemy_4[0][1])
#         if random.choice([True, False]):
#             self.enemy_5 = [random.choice(range(1, length)), random.choice(range(1, height))], choose_enemy()
#             room_m = add_object_on_map(room_m, self.enemy_5[1], self.enemy_5[0][0], self.enemy_5[0][1])
#         if random.choice([True, False]):
#             self.enemy_6 = [random.choice(range(1, length)), random.choice(range(1, height))], choose_enemy()
#             room_m = add_object_on_map(room_m, self.enemy_6[1], self.enemy_6[0][0], self.enemy_6[0][1])
#         self.room = room_m
#         self.room_index = Map.room_index
#         Map.room_index += 1
#
#     def move_to_room(self, room_index):
#         if self.room_index == room_index:
#             return self.room
#
#
#
# def add_random_doors():
#     door_wall = ["up", "down"]
#     for _ in range(5):
#         if door_wall[-1] == "down":
#             door_wall.extend(random.choice([['up', 'down'], ['right', 'left'], ['left', 'right']]))
#         elif door_wall[-1] == "up":
#             door_wall.extend(random.choice([['down', 'up'], ['right', 'left'], ['left', 'right']]))
#         elif door_wall[-1] == "left":
#             door_wall.extend(random.choice([['down', 'up'], ['right', 'left'], ['up', 'down']]))
#         elif door_wall[-1] == "right":
#             door_wall.extend(random.choice([['down', 'up'], ['up', 'down'], ['left', 'right']]))
#     return door_wall[1::]
#
#
# door_map_concatenation = add_random_doors()
# biome = get_random_biome()
# length_1, height_1 = generate_room_length_height()
# room_1 = Map(generate_rooms(biome, length_1, height_1),
#              door_data(door_map_concatenation[0], biome, length_1, height_1, "v"),
#              door_data(door_map_concatenation[1], biome, length_1, height_1, 1), length_1, height_1)
#
# length_2, height_2 = generate_room_length_height()
# room_2 = Map(generate_rooms(biome, length_2, height_2),
#              door_data(door_map_concatenation[2], biome, length_2, height_2, 0),
#              door_data(door_map_concatenation[3], biome, length_2, height_2, 1), length_2, height_2)
#
# length_3, height_3 = generate_room_length_height()
# room_3 = Map(generate_rooms(biome, length_3, height_3),
#              door_data(door_map_concatenation[4], biome, length_3, height_3, 0),
#              door_data(door_map_concatenation[5], biome, length_3, height_3, 1), length_3, height_3)
#
# length_4, height_4 = generate_room_length_height()
# room_4 = Map(generate_rooms(biome, length_4, height_4),
#              door_data(door_map_concatenation[6], biome, length_4, height_4, 0),
#              door_data(door_map_concatenation[7], biome, length_4, height_4, 1), length_4, height_4)

# room_p = Map.move_to_room()
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
    for item_f in room[1:-1]:
        print(f"{margins}{color}{item_f}{margins}\033[0;0m")
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
    last_ch = 0
    space_len = 1

    for i, item_f in enumerate(room):
        if i == row:
            if column == 0:
                if item_f[0] == " ":
                    output.append(f"{hero}{item_f[2::]}")
                else:
                    output.append(f"{hero}{item_f[1::]}")
            else:
                for i, ch in enumerate(item_f):

                    if ch == " ":
                        count_row_positions += 1
                        count_row_positions_actions += 1
                    elif ch != " ":
                        count_row_positions += 1
                        count_row_positions_actions += 2
                    last_ch = i

                    if count_row_positions_actions >= column * 2:
                        break
                try:
                    if item_f[i + 1] == " ":
                        space_len = 2
                except IndexError:
                        space_len = 1
                output.append(f"{item_f[0:count_row_positions]}{hero}{item_f[count_row_positions + space_len::]}")
        else:
            output.append(item_f)
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
    return random.choice(['💀', '👺', '👹', '🕷', '🦂', '👻', '👽', '😈', '🌬', '🎃', '👾', '🐲', "🎭"])


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
    for k, v in materials.item_fs():
        new_data.append(f"{v}")
    for k_1, v_1 in gear.item_fs():
        new_data.append(f"{v_1}")
    for item_f in inventory:
        new_data.append(item_f)
    os.chdir("Your_characters")

    with open(f"{hero_name}.txt", "w") as fw:
        for item_f in new_data:
            fw.write(item_f + "\n")

    os.chdir(main_path)


def read_abilities(selected_hero: str):
    """

    :param selected_hero:
    :return:
    """
    main_path = os.getcwd()
    os.chdir("heroes")
    for item_f in os.listdir():
        if item_f[0:4] == selected_hero[0:4]:
            with open(item_f, "r") as fr:
                content = fr.readlines()
    os.chdir(main_path)
    output = [item_f.strip() for item_f in content]
    for item_f in output:
        print(item_f)


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
        for item_f in content:
            if str.lower(item_f[0:4]) == str.lower(hero_class[0:4]):
                print(f"\n{item_f}\n")
        print("Choose one option:\ngo back(b)\nchoose class(c)\nread abilities(a)")
        option = str.lower(input("Your option:"))
        while option:
            if option not in ["c", "b", "a"]:
                print("option is incorrect")
            elif option == "a":
                read_abilities(hero_class)
            elif option == "c":
                item_fs_0 = {"helm": "empty_", "chest": "empty_", "boots": "empty_", "weapon": "empty_",
                           "sec_weapon": "empty_", "jewel": "empty_"}
                materials_0 = {"wood": '0', "iron": '0', "diamond": '0', "angelic dust": '0'}
                name = get_hero_name()
                write_hero_data(name, hero_class, "0", "500", materials_0, item_fs_0, ["empty_"] * 18)
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
    for item_f in os.listdir():
        if item_f == f"{hero_name}.txt":
            with open(item_f, "r") as fr:
                content = fr.readlines()
    hero_and_class = {"wizard": "🧙", "shadow": "👤", "vampire": "🧛", "fairy": "🧚", "triton": "🧜", "spirit": "🧞"}
    for k, v in hero_and_class.item_fs():
        if k == content[0].strip():
            output = v
    if changed_directory == 1:
        os.chdir(main_path)
    return output


def get_item_f_symbol(item_f):
    """

    :param item_f:
    :return:
    """

    output = ""
    dict_item_fs = {"crown": "👑", "wand": "🎆",
                  "the_eye": "🧿", "robe": "👘",
                  "talisman": "🎐", "boots": "👢"}

    for k, v in dict_item_fs.item_fs():
        if item_f == k:
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
        for i, item_f in enumerate(os.listdir()):
            symbol = get_hero_symbol(item_f[0:-4])
            print(f"{item_f[0:-4]}{symbol}({i + 1})")
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
    inventory = [item_f.strip() for item_f in content]
    return inventory


def get_random_rarity(difficulty):
    """

    :param difficulty:
    :return:
    """
    red_item_f = 10 * difficulty
    grren_item_f = 50 * difficulty
    yellow_item_f = 500 * difficulty
    blue_item_f = 1300 * difficulty
    black_chance = 10000 - blue_item_f - yellow_item_f - grren_item_f - red_item_f
    list_chances = ["common"] * (black_chance) + ["normal"] * (blue_item_f) + ["rare"] * \
                   (yellow_item_f) + ["legendary"] * (grren_item_f) + ["angelic"] * (red_item_f)
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
    print(f"|  \033[1;30;45m|{symbol}|\033[2;37;0m{' ' * 10}\033[1;30;47m{item_f_colored_symbol(inventory[12])}\033[0;0m "
          f"\033[1;30;47m{item_f_colored_symbol(inventory[7])}\033[2;37;0m{' ' * 7}|")
    print(f"|\033[32mwood: {inventory[3]}\033[0;0m{' ' * (22 - len(str(inventory[3])))}|")
    print(f"|\033[38msilver: {inventory[4]}\033[0;0m"
          f"{' ' * (8 - len(str(inventory[4])))}\033[1;30;47m{item_f_colored_symbol(inventory[10])}\033[0;0m "
          f"\033[1;30;47m{item_f_colored_symbol(inventory[8])}\033[0;0m \033[1;30;47m{item_f_colored_symbol(inventory[11])}\033[0;0m"
          f"{' ' * 3}|")
    print(f"|\033[34mdiamond: {inventory[5]}\033[0;0m{' ' * (19- len(str(inventory[5])))}|")
    print(f"|\033[31mangelic dust: {inventory[6]}\033[0;0m{' ' * (5- len(str(inventory[6])))}\033[1;30;47m"
          f"{item_f_colored_symbol(inventory[9])}\033[0;0m"
          f"{' ' * 7}|")
    print(f"|\033[33mgold: {inventory[2]}\033[0;0m{' ' * (22- len(str(inventory[2])))}|")
    row_1 = ""
    row_2 = ""
    row_3 = ""
    row_counter = 1
    for item_f in inventory[13::]:
        if row_counter <= 6:
            row_1 += f"{item_f_colored_symbol(item_f)}  "
        elif row_counter <= 12:
            row_2 += f"{item_f_colored_symbol(item_f)}  "
        elif row_counter <= 18:
            row_3 += f"{item_f_colored_symbol(item_f)}  "
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


def create_item_f(item_f_name, difficulty):
    """

    :param item_f_name:
    :param difficulty:
    :return:
    """
    rarity = get_random_rarity(difficulty)
    return f"{item_f_name}-{rarity}-{random_primary_stat(rarity)}-" \
           f"{random_secondary_stat(rarity)} {random_secondary_stat(rarity)}-{random_secondary_stat(rarity)}"\


def print_item_f(item_f):
    """

    :param item_f:
    :return:
    """
    item_f_l = item_f.split()

    item_f_color, text_color = get_rarity_color(item_f_l[1])
    print(f" {text_color}{'_' * 16}\033[0;0m ")
    print(f"{text_color}|\033[0;0m{item_f_l[0]}{' ' * (15 - len(item_f_l[0]) - len(item_f_l[1]))}{text_color}{item_f_l[1]} |")
    print(f"{text_color}|\033[0;0m {item_f_color}{get_item_f_symbol(item_f_l[0]) }\033[0;0m{' ' * 13}{text_color}|\033[0;0m")
    print(f"{text_color}|{' ' * 16}|\033[0;0m")
    print(f"{text_color}|\033[0;0m {item_f_l[2]} {item_f_l[3]}\033[0;0m{' ' * (14 - len(item_f_l[2]) - len(item_f_l[3]))}{text_color}|\033[0;0m")
    print(f"{text_color}|\033[0;0m {item_f_l[4]} {item_f_l[5]}\033[0;0m{' ' * (14 - len(item_f_l[4]) - len(item_f_l[5]))}{text_color}|\033[0;0m")
    print(f"{text_color}|\033[0;0m {item_f_l[6]} {item_f_l[7]}\033[0;0m{' ' * (14 - len(item_f_l[6]) - len(item_f_l[7]))}{text_color}|\033[0;0m")
    print(f"{text_color}|\033[0;0m {item_f_l[8]} {item_f_l[9]}\033[0;0m{' ' * (14 - len(item_f_l[8]) - len(item_f_l[9]))}{text_color}|\033[0;0m")
    print(f"{text_color}|{'_' * 16}|\033[0;0m")


def item_f_colored_symbol(item_f):
    """

    :param item_f:
    :return:
    """
    if item_f == "empty":
        return "\033[1;30;47m⬛\033[0;0m"
    else:
        item_f_l = item_f.split()
        item_f_color, text_color = get_rarity_color(item_f_l[1])
        return f"{item_f_color}{get_item_f_symbol(item_f_l[0])}\033[0;0m"


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
            print("Choose item_f:\nhead(0)\nchest(1)\nfeet(2)\nmain hand(3)\n2nd hand(4)\n"
                  "jewel(5)\ninventory(coresponding number)")
            option_s = get_correct_int_input("choose one option by writing its corresponding value:")
            if option_s <= 21:
                if inventory[option_s] == "empty":
                    print("You don't have an item_f in that slot")
                else:
                    print_item_f(inventory[option_s])
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
    correct_movement = 0
    while True:
        if movement == "i":
            print_inventory(file)
            navigate_inventory(file)
        elif movement == "e":
            print("Are you sure you want to exit?")
            if get_answer():
                return 0, 0
        else:
            row_func = row
            column_func = column
            while True:
                for ch in movement:
                    if ch not in "wasd":
                        print("incorrect sequence")
                        break
                else:
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
                    print(column_func, row_func)
                    return column_func, row_func
                else:
                    print("incorrect movement")
                    break
        movement = str.lower(input("enter a sequence of movements:"))


def village():
    """

    :return:
    """
    return ["", f"{'  ' * 2}⚒{'  ' * 3}‼", f"{'  ' * 7}", f"{'  ' * 3}⛲{'  ' * 3}", f"{'  ' * 7}", f"💍{'  ' * 2}💰{'  ' * 3}"]


def print_village(village):
    margin = f"\033[48;5;0m{' ' * 2}\033[0;0m"
    print(f"\033[48;5;0m{' ' * 22}\033[0;0m")
    print(f"\033[48;5;0m{'  ' * 2}\033[48;5;28m🏘🏠⛪\033[48;5;0m{'  ' * 2}\033[48;5;28m🏚🏤\033[48;5;0m   \033[0;0m")

    print(f"{margin}{margin}\033[48;5;28m{village[1]}⛪{margin}")
    print(f"{margin}{margin}\033[48;5;28m{village[2]}{margin}{margin}")
    print(f"{margin}{margin}\033[48;5;28m{village[3]}{margin}{margin}")
    print(f"{margin}\033[48;5;28m🏰{village[4]}{margin}{margin}")
    print(f"{margin}\033[48;5;28m💒{village[5]}🏚{margin}")
    print(f"\033[48;5;0m{'  ' * 1}\033[48;5;28m🏘🏠\033[48;5;0m{'  ' * 2}\033[48;5;28m🏚🏤\033[48;5;0m {'  ' * 3}\033[0;0m")
    print(f"\033[48;5;0m{' ' * 22}\033[0;0m")


def village_interface():

    column_v, row_v = 1, 3
    print(f"instructions")
    village_with_hero = add_object_on_map(village(), "🧙‍", column_v, row_v)
    print_village(village_with_hero)
    while True:
        column_v, row_v = hero_movement("ramulica.txt", column_v, row_v, 7, 5)
        if column_v == 0 and row_v == 0:
            return False
        else:
            village_with_hero = add_object_on_map(village(), "🧙", column_v, row_v)
            print_village(village_with_hero)
            if column_v == 7 and row_v == 1:
                print("Do you want to go in a mission?")
                if get_answer():
                    return True
            elif column_v == 1 and row_v == 5:
                print("Do you want to buy something from jeweler?")
                if get_answer():
                    print("make jeweler interface")
            elif column_v == 4 and row_v == 5:
                print("Do you want to buy something from shop?")
                if get_answer():
                    print("make shop interface")
            elif column_v == 3 and row_v == 1:
                print("Do you want to craft something at the blacksmith?")
                if get_answer():
                    print("make blacksmith interface")


def margin_random_generator(column, row):
    cl_rw = ["x", "y"]
    random.shuffle(cl_rw)
    if cl_rw[0] == "x":
        return [random.choice([column, 1]), random.choice(range(1, row))]
    else:
        return [random.choice(range(1, column)), random.choice([row, 1])]


def door_data(entrance, biome, column, row, next_room):
    if entrance == "up":
        return random.choice(range(2, column - 1)), 1, next_room, choose_door(biome)
    elif entrance == "down":
        return random.choice(range(2, column - 1)), row, next_room, choose_door(biome)
    elif entrance == "right":
        return column, random.choice(range(2, row - 1)), next_room, choose_door(biome)
    elif entrance == "left":
        return 1, random.choice(range(2, row - 1)), next_room, choose_door(biome)


class Map:

    def __init__(self, room, entrance, exit, length, height):
        self.entrance = entrance
        room_m = add_object_on_map(room, self.entrance[3], self.entrance[0], self.entrance[1])

        self.exit = exit
        room_m = add_object_on_map(room_m, self.exit[3], self.exit[0], self.exit[1])

        list_of_enemies = []

        self.enemy_1 = margin_random_generator(length, height), choose_enemy(), "alive"
        # room_m = add_object_on_map(room_m, self.enemy_1[1], self.enemy_1[0][0], self.enemy_1[0][1])
        list_of_enemies.append(self.enemy_1)

        self.enemy_2 = margin_random_generator(length, height), choose_enemy(), "alive"
        list_of_enemies.append(self.enemy_2)

        self.enemy_3 = margin_random_generator(length, height), choose_enemy(), "alive"
        list_of_enemies.append(self.enemy_3)

        if random.choice([True, False]):
            self.enemy_4 = [random.choice(range(1, length)), random.choice(range(1, height))], choose_enemy(), "alive"
            list_of_enemies.append(self.enemy_4)

        if random.choice([True, False]):
            self.enemy_5 = [random.choice(range(1, length)), random.choice(range(1, height))], choose_enemy(), "alive"
            list_of_enemies.append(self.enemy_5)

        if random.choice([True, False]):
            self.enemy_6 = [random.choice(range(1, length)), random.choice(range(1, height))], choose_enemy(), "alive"
            list_of_enemies.append(self.enemy_6)

        self.room_m = room_m
        self.list_of_enemies = list_of_enemies

        for item_f in self.list_of_enemies:
            if item_f[-1] == "alive":
                room_e = add_object_on_map(room_m, item_f[1], item_f[0][0], item_f[0][1])

        self.room = room_e


def add_random_doors():
    door_wall = ["up", "down"]
    for _ in range(5):
        if door_wall[-1] == "down":
            door_wall.extend(random.choice([['up', 'down'], ['right', 'left'], ['left', 'right']]))
        elif door_wall[-1] == "up":
            door_wall.extend(random.choice([['down', 'up'], ['right', 'left'], ['left', 'right']]))
        elif door_wall[-1] == "left":
            door_wall.extend(random.choice([['down', 'up'], ['right', 'left'], ['up', 'down']]))
        elif door_wall[-1] == "right":
            door_wall.extend(random.choice([['down', 'up'], ['up', 'down'], ['left', 'right']]))
    return door_wall[1::]

def generate_arena(player, enemies):
    arena = [f"{' '* 54}"] * 15
    column_row_l = [[14, 12], [10, 11], [18, 11], [6, 10], [22, 10], [2, 9], [26, 9]]
    effects_coordinates = [[0, 1], [-1, 1], [1, 1], [0, 2], [-1, 2], [1, 2]]
    for i, item_f in enumerate(player):
        for i_1, effect in enumerate(item_f[1::]):
            arena = add_object_on_map(arena, effect, column_row_l[i][0] + effects_coordinates[i_1][0],
                                      column_row_l[i][1] - effects_coordinates[i_1][1])

        arena = add_object_on_map(arena, player[i][0], column_row_l[i][0], column_row_l[i][1])
    for i, item_f in enumerate(enemies):
        for i_1, effect in enumerate(item_f[1::]):
            arena = add_object_on_map(arena, effect, column_row_l[i][0] + effects_coordinates[i_1][0],
                                      column_row_l[i][1] - effects_coordinates[i_1][1] - 6)
        arena = add_object_on_map(arena, enemies[i][0], column_row_l[i][0], column_row_l[i][1] - 6)
    return arena
"""
player: [[][]]
"""
def ordonate_hp(entities):
    coordinates = [7, 5, 9, 3, 11, 1, 13]
    life_row = ["  ", "      "] * 7
    life_str = ""
    for i in range(len(entities)):

        life_row[coordinates[i]] = str(int(entities[i].life[0])).zfill(6)
    for item_f in life_row:
        life_str += item_f
    return life_str


def printe_arena(arena, ally_l, enemy_l):
    margin = f"\033[48;5;16m  \033[0;0m"
    print(f"\033[38;5;34m{ordonate_hp(enemy_l)}\033[0;0m")
    print(f"{margin}\033[48;5;16m{arena[0]}\033[0;0m{margin}")
    for item_f in arena[1:-1]:
        line = ""
        for ch in item_f:
            if ch != " ":
                line += f"\033[48;5;246m{ch}\033[48;5;236m"
            else:
                line += ch
        print(f"{margin}\033[48;5;236m{line}\033[0;0m{margin}")
    print(f"{margin}\033[48;5;16m{arena[-1]}\033[0;0m{margin}")
    print(f"\033[38;5;34m{ordonate_hp(ally_l)}\033[0;0m")

    print("\nabilities")
    print(ally_l[0].life, ally_l[0].mana)

def get_effect_symbol(effect):
    effects = {"freeze": "❄", "burn": "🔥", "bleed": "🩸", "blind": "✨", "stun": "💫", "sleep": "💤", "taunt": "💢", "charm": "💞"}
    for k, v in effects.item_fs():
        if effect == k:
            return v

def stats_from_item_fs(inventory):

    added_stats = {"primary": 0, "armor": 0, "hp": 0, "crit": 0, "crit_dmg": 0, "speed": 0, "mr": 0,
                   "dodge": 0, "cc_immun": 0, "mana": 0}
    for item_f in inventory[7:13]:
        item_f_stats = item_f.split("-")
        print(item_f_stats)
        for stat in item_f_stats[2::]:
            added_stats[stat[0:stat.find(":")]] += float(stat[stat.rfind(" ") + 1::])
    return added_stats




class Combatant_izoteric:
    def __init__(self, symbol, life, mana, data, good_bad_side, bonus = {"primary": 0, "armor": 0, "hp": 0, "crit": 0, "crit_dmg": 0, "speed": 0, "mr": 0,
                   "dodge": 0, "cc_immun": 0, "mana": 0}):
        self.symbol = symbol
        self.primary = data[0] + bonus["primary"]
        self.life = [life + bonus["hp"]] + [data[1] + bonus["hp"]]
        self.damage = data[2] + bonus["primary"]
        self.speed = data[3] + bonus["speed"]
        self.crit = data[4]  + bonus["crit"]
        self.crit_dmg = data[5] + bonus["crit_dmg"]
        self.armor = data[6] + bonus["armor"]
        self.mr = data[7] + bonus["mr"]
        self.dodge = data[8] + bonus["dodge"]
        self.cc_immun = data[9] + bonus["cc_immun"]
        self.mana = [mana + bonus["mana"]] + [data[10] + bonus["mana"]]
        self.side = good_bad_side
        self.effects = {}

    def deal_damage_heal(self, damage):
        if self.life[0] + damage <= self.life[1]:
            self.life = [self.life[0] + damage] + [self.life[1]]
        else:
            self.life = [self.life[1]] + [self.life[1]]

    def get_lose_mana(self, mana_difference):
        if self.mana[0] + mana_difference <= self.mana[1]:
            self.mana = [self.mana[0] + mana_difference] + [self.mana[1]]
        else:
            self.mana = [self.mana[1]] + [self.mana[1]]

    def round_end_effect(self):
        output = {}
        if 'burn' in self.effects:
            Combatant_izoteric.deal_damage_heal(self, -self.damage)
        if 'bleed' in self.effects:
            Combatant_izoteric.deal_damage_heal(self, -(self.life[0] * 0.1))
        for k, v in self.effects.item_fs():
            if v > 0:
                output[k] = v - 1
        self.effects = output

    def printable_symbols(self):
        return [self.symbol] + [get_effect_symbol(k) for k, v in self.effects.item_fs()]

    def crit_mechanic(self):
        if self.crit >= 100:
            return self.damage + (self.damage * (self.crit_dmg + self.crit - 100) / 100)
        else:
            x = random.choice([1] * int(self.crit) + [0] * (100 - int(self.crit)))
            if x == 1:
                return self.damage + (self.damage * self.crit_dmg / 100)
            else:
                return self.damage

    def basic_attack_class(self, hero_class, enemies_l):
        output = []
        if hero_class == "wizard":
            Combatant_izoteric.get_lose_mana(self, 15)
            for _ in range(len(enemies_l)):
                output.append([Combatant_izoteric.crit_mechanic(self)/len(enemies_l), []])
        return output, "magical", "all"

    def first_ability(self, hero_class, enemies_l):
        output = []
        if hero_class == "wizard":
            if self.mana[0] >= 25:
                Combatant_izoteric.get_lose_mana(self, -25)
                for _ in range(len(enemies_l)):
                    output.append([Combatant_izoteric.crit_mechanic(self), [f'{random.choice(["freeze"] * 70 + ["none"] * 30)}2']])
            else:
                print("not enough mana")
                return 'error'

        return output, "magical", "damage"

    def second_ability(self, hero_class, enemies_l):
        output = []
        if hero_class == "wizard":
            if self.mana[0] >= 35:
                Combatant_izoteric.get_lose_mana(self, -35)
                try:
                    attack_eneies = random.sample(range(len(enemies_l)), 2)
                except:
                    attack_eneies = [0]
                for i in range(len(enemies_l)):
                    if i in attack_eneies:
                        if "freeze" in [item_f[0:-1] for item_f in enemies_l[i]]:
                            output.append([Combatant_izoteric.crit_mechanic(self) * 4, ["burn3"]])
                        else:
                            output.append([Combatant_izoteric.crit_mechanic(self) * 2, ["burn3"]])
                    else:
                        output.append([0, []])
            else:
                print("not enough mana")
                return 'error'

        return output, "magical", "damage"

    def third_ability(self, hero_class, enemies_effects_l):
        output = []
        if hero_class == "wizard":
            if self.mana[0] == self.mana[1]:
                Combatant_izoteric.get_lose_mana(self, self.mana[1])
                for item_f in enemies_effects_l:
                    new_effects = []
                    for effect in item_f:
                        if effect[0:-1] == "freeze":
                            new_effects.append("freeze2")
                        elif effect[0:-1] == "burn":
                            new_effects.append("burn3")
                        else:
                            new_effects.append(effect)
                    output.append([0, new_effects])
                return output, "magical", "round"
            else:
                print("Not enough mana")
                return 'error'


    def forth_ability(self, hero_class, enemies_l):
        output = []
        if hero_class == "wizard":
            if self.mana[0] >= 50:
                Combatant_izoteric.get_lose_mana(self, -50)
                attack_enemy = random.choice(range(len(enemies_l)))

                for i in range(len(enemies_l)):
                    if i == attack_enemy:
                        if "burn" in [item_f[0:-1] for item_f in enemies_l[i]]:
                            Combatant_izoteric.deal_damage_heal(self, int(self.damage * 15 * 0.1))
                        output.append([Combatant_izoteric.crit_mechanic(self) * 15, ["blind2"]])
                    else:
                        output.append([0, []])
            else:
                print("not enough mana")
                return 'error'

        return output, "pure", "damage"

    def use_ability(self, hero_class, enemiy_l):
        option = input("choose ability")
        while True:
            if option == "a": #  and "blind" not in self.effects:
                ability_0 = Combatant_izoteric.basic_attack_class(self, hero_class, enemiy_l)
                if ability_0 != "error":
                    return ability_0

            elif option == "q":
                ability_1 = Combatant_izoteric.first_ability(self, hero_class, enemiy_l)
                if ability_1 != "error":
                    return ability_1
                else:
                    print('\033[38;5;160mYou do not have enough mana\033[0;0m')
                    option = input("choose ability")

            elif option == "w":
                ability_2 = Combatant_izoteric.second_ability(self, hero_class, enemiy_l)
                if ability_2 != "error":
                    return ability_2
                else:
                    print('\033[38;5;160mYou do not have enough mana\033[0;0m')
                    option = input("choose ability")

            elif option == "e":
                ability_3 = Combatant_izoteric.third_ability(self, hero_class, enemiy_l)
                if ability_3 != "error":
                    return ability_3
                else:
                    print('\033[38;5;160mYou do not have enough mana\033[0;0m')
                    option = input("choose ability")

            elif option == "r":
                ability_4 = Combatant_izoteric.forth_ability(self, hero_class, enemiy_l)
                if ability_4 != "error":
                    return ability_4
                else:
                    print('\033[38;5;160mYou do not have enough mana\033[0;0m')
                    option = input("choose ability")

            else:
                option = input("choose ability")

    def enemy_attack(self, allies):
        output = []
        if self.mana[0] == self.mana[1]:
            for i in range(len(allies)):

                output.append([Combatant_izoteric.crit_mechanic(self) * 1.2,
                               [f"{random.choice(['stun'] * 5 + ['burn'] * 5 + ['blind'] * 5 + ['none'] * 85)}2"]])

        else:

            Combatant_izoteric.get_lose_mana(self, 15)
            attack_ally = random.choice(range(len(allies)))

            for i in range(len(allies)):
                if i == attack_ally:
                    output.append([Combatant_izoteric.crit_mechanic(self) * 1.2,
                                   [f"{random.choice(['stun'] * 5 + ['burn'] * 5 + ['blind'] * 5 + ['none'] * 85)}2"]])
                else:
                    output.append([0, []])
        return output, "pure", "damage"

    def list_of_effects(self):
        output = []
        for k, v in self.effects.item_fs():
            output.append(f"{k}{v}")
        return output



def ability_effect(enemy_list, damage_effects):
    if damage_effects[1] == "magical":
        for i, item_f in enumerate(enemy_list):
            damage = damage_effects[0][i][0] - int(item_f.mr)

            Combatant_izoteric.deal_damage_heal(item_f, -damage)
            for effect in damage_effects[0][i][1]:
                if effect[0:-1] != "none":
                    item_f.effects[effect[0:-1]] = int(effect[-1])
    elif damage_effects[1] == "pure":
        for i, item_f in enumerate(enemy_list):
            damage = damage_effects[0][i][0]
            Combatant_izoteric.deal_damage_heal(item_f, -damage)
            for effect in damage_effects[0][i][1]:
                if effect[0:-1] != "none":
                    item_f.effects[effect[0:-1]] = int(effect[-1])
    elif damage_effects[1] == "error":
        return "again"



def remove_dead_body(enemy_list):
    for item_f in enemy_list:
        if item_f.life[0] <= 0:
            enemy_list.remove(item_f)
    return enemy_list


def enter_a_turn(meesage):
    x = input(meesage)
    while True:
        if x == "c":
            break
        else:
            print("You entered a wrong answer")
            x = input(meesage)
    return True


difficulty = 1

enemies_len = random.choice(range(1, 7))
enemy_l = [Combatant_izoteric("🤖", 90000 / enemies_len , 0, [40 / enemies_len, 90000 / enemies_len, 45 / enemies_len, 200, 0, 0, 3, 5, 0, 0, 45], "evil") for i in range(enemies_len)]




ally_l = []
enemy_2 = Combatant_izoteric("🧙‍", 850, 70, [40, 850, 45, 200, 0, 0, 3, 5, 0, 0, 70], "good", stats_from_item_fs(read_inventory("ramulica.txt")))
print(enemy_2.primary)
ally_l.append(enemy_2)



print(enemy_2.mana)

list_of_e = [Combatant_izoteric.list_of_effects(item_f) for item_f in enemy_l]
printe_arena(generate_arena([Combatant_izoteric.printable_symbols(enemy_2)], [Combatant_izoteric.printable_symbols(item_f) for item_f in enemy_l]), ally_l, enemy_l)
outcome = "Lose"
turn = 0
while True:
    turn += 1
    print(f"\n\033[38;5;220mIt's turn {turn}\033[0;0m\n")
    if "freeze" in enemy_2.effects or "stun" in enemy_2.effects:
        print(f"you are unable to attack because of your condition{enemy_2.effects}")
    else:
        if enter_a_turn("It's your turn to attack, enter c to continue"):

            damage_u_deal = Combatant_izoteric.use_ability(enemy_2, 'wizard', list_of_e)
            if damage_u_deal != "again":

                ability_effect(enemy_l, damage_u_deal)
                print(f"\n\033[38;5;27mYour mana pool is {enemy_2.mana[0]}/{enemy_2.mana[1]}\033[0;0m")
                print(f"You did \033[38;5;196m{damage_u_deal} damage\n\033[0;0m")

    enemy_l = remove_dead_body(enemy_l)
    list_of_e = [Combatant_izoteric.list_of_effects(item_f) for item_f in enemy_l]
    printe_arena(generate_arena([Combatant_izoteric.printable_symbols(enemy_2)], [Combatant_izoteric.printable_symbols(item_f) for item_f in enemy_l]), ally_l, enemy_l)

    if len(enemy_l) == 0:
        outcome = "Victory"
        break

    if enter_a_turn("It's enemy's turn to attack, enter c to continue"):

        for i, item_f in enumerate(enemy_l):
            if "freeze" in item_f.effects or "stun" in item_f.effects:
                print(f"enemy {i+1} is unable to attack because of his condition{item_f.effects}")
            else:
                damage_dealt_by_enemy = Combatant_izoteric.enemy_attack(item_f, [enemy_2])
                ability_effect([enemy_2], damage_dealt_by_enemy)
                print(f"Enemy {i + 1} did \033[38;5;196m{damage_dealt_by_enemy} damage\033[0;0m to you")

    printe_arena(generate_arena([Combatant_izoteric.printable_symbols(enemy_2)],
                                [Combatant_izoteric.printable_symbols(item_f) for item_f in enemy_l]), ally_l, enemy_l)

    for item_f in enemy_l:
        Combatant_izoteric.round_end_effect(item_f)
    for item_f in ally_l:
        Combatant_izoteric.round_end_effect(item_f)







