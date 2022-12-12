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
#     for item in room[1:-1]:
#         print(f"{margins}{color}{item}{margins}\033[0;0m")
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
#     for i, item in enumerate(room):
#         if i == row:
#
#             output.append(len(item))
#
#         else:
#             output.append(item)
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
#     for k, v in materials.items():
#         new_data.append(f"{v}")
#     for k_1, v_1 in gear.items():
#         new_data.append(f"{v_1}")
#     for item in inventory:
#         new_data.append(item)
#     os.chdir("Your_characters")
#
#     with open(f"{hero_name}.txt", "w") as fw:
#         for item in new_data:
#             fw.write(item + "\n")
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
#     for item in os.listdir():
#         if item[0:4] == selected_hero[0:4]:
#             with open(item, "r") as fr:
#                 content = fr.readlines()
#     os.chdir(main_path)
#     output = [item.strip() for item in content]
#     for item in output:
#         print(item)
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
#         for item in content:
#             if str.lower(item[0:4]) == str.lower(hero_class[0:4]):
#                 print(f"\n{item}\n")
#         print("Choose one option:\ngo back(b)\nchoose class(c)\nread abilities(a)")
#         option = str.lower(input("Your option:"))
#         while option:
#             if option not in ["c", "b", "a"]:
#                 print("option is incorrect")
#             elif option == "a":
#                 read_abilities(hero_class)
#             elif option == "c":
#                 items_0 = {"helm": "empty", "chest": "empty", "boots": "empty", "weapon": "empty", "sec_weapon": "empty",
#                            "jewel": "empty"}
#                 matirials_0 = {"wood": '0', "iron": '0', "diamond": '0', "angelic dust": '0'}
#                 name = get_hero_name()
#                 write_hero_data(name, hero_class, "0", "500",matirials_0, items_0, [])
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
#     for item in os.listdir():
#         if item == f"{hero_name}.txt":
#             with open(item, "r") as fr:
#                 content = fr.readlines()
#     hero_and_class = {"wizard": "🧙", "shadow": "👤", "vampire": "🧛", "fairy": "🧚", "triton": "🧜", "spirit": "🧞"}
#     for k, v in hero_and_class.items():
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
#     for item in os.listdir():
#         if item == f"{hero_name}.txt":
#             with open(item, "r") as fr:
#                 content = fr.readlines()
#     hero_and_class = {"wizard": "🧙", "shadow": "👤", "vampire": "🧛", "fairy": "🧚", "triton": "🧜", "spirit": "🧞"}
#     for k, v in hero_and_class.items():
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
#         for i, item in enumerate(os.listdir()):
#             symbol = get_hero_symbol(item[0:-4])
#             print(f"{item[0:-4]}{symbol}({i + 1})")
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
#     red_item = 15 * difficulty
#     grren_item = 50 * difficulty
#     yellow_item = 500 * difficulty
#     blue_item = 1300 * difficulty
#     black_chance = 10000 - blue_item - yellow_item - grren_item - red_item
#     list_chances = ["\033[1;30;40m"] * (black_chance) + ["\033[1;30;44m"] * (blue_item) + ["\033[1;30;43m"] * \
#                    (yellow_item) + ["\033[1;30;42m"] * (grren_item) + ["\033[1;30;41m"] * (red_item)
#     return random.choice(list_chances)
#
# for _ in range(1000):
#     print(f"{get_random_rarity(5)}item")


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

list_1 = ['empt',' empt', 'empt']

print(list_1.index("empty"))
