# x = "\033[1;31;40m"
#
# print(f'{x} L \033[0;0m {x} L \033[0;0m')


def change_game_log(win_lose: bool, guess_round: str):
    """

    :param guess_round:
    :param win_lose:
    :return:
    """
    with open("winning streak.txt", "r") as fr:
        content_1 = fr.readlines()
    content = [item.strip() for item in content_1]
    new_content = [f"{content[0][0:-1]}{int(content[0][-1]) + 1}"]
    if win_lose:
        if int(content[2][-1]) + 1 > int(content[1][-1]):
            new_content.append(f"{content[1][0:-1]}{str(int(content[2][-1]) + 1)}")
        new_content.append(f"{content[2][0:-1]}{str(int(content[2][-1]) + 1)}")
        new_content.append(content[3])
        for item in content[4::]:
            if str(guess_round) == item[0]:
                new_content.append(f"{item[0:-1]}{str(int(item[-1]) + 1)}")
            else:
                new_content.append(item)
    else:
        new_content.append(content[1])
        for item in content[2::]:

            if item == "Guess distribution:":
                new_content.append("Guess distribution:")
            else:
                new_content.append(f"{item[0:-1]}0")
    with open("winning streak.txt", "w") as fw:
        for item in new_content:
           fw.write(item + "\n")


change_game_log(False, "2")
