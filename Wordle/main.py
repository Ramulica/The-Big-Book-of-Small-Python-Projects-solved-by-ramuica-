import random


def list_all_5_letter_words():
    """
    returns a list with all the 5 letters words
    :return:
    """

    with open("5 letters words.txt", "r") as fr:
        content = fr.readlines()
    return [item.strip() for item in content]


def random_word(word_list):
    """
    gets a random word which you have to guess
    :param word_list:
    :return:
    """
    return random.choice(word_list)


def words_you_chose(old_word_list: list, all_word_list: list):
    """
    this function ensures that you enter an existing 5 letters word
    :param old_word_list:
    :return:
    """
    new_word = input("Guess a word:")
    while new_word not in all_word_list:
        if len(new_word) == 5:
            print("Word doesn't exist")
        else:
            print("Word must have 5 letters")
        new_word = input("Guess a word:")
    old_word_list.append(new_word)
    return old_word_list


def decide_square_color(letter: str, correct_word: str, correct_letter: str):
    """
    if you have the right letter in the right spot, it shows up green.
    A correct letter in the wrong spot shows up yellow. A letter that
    isn't in the word in any spot shows up black.
    :param letter:
    :param correct_word:
    :param correct_letter:
    :return:
    """
    if letter == correct_letter:
        return "\033[1;30;42m"
    elif letter in correct_word:
        return "\033[1;30;43m"
    else:
        return "\033[1;37;40m"


def print_words(guessed_list: list, correct_word: str):
    """
    shows you the words entered
    :param guessed_list:
    :param correct_word:
    :return:
    """
    print("")
    for item in guessed_list:
        letter_l = str.upper(item)
        correct_word_up = str.upper(correct_word)
        colored_letters = ""

        for i in range(len(letter_l)):
            x = decide_square_color(letter_l[i], correct_word_up, correct_word_up[i])
            colored_letters += f"{x} {letter_l[i]} \033[0;0m "
        print(colored_letters,"\n")
    for i in range(6 - len(guessed_list)):
        print("\033[1;31;40m   \033[0;0m " * 5, "\n")


def change_game_log(win_lose: bool, guess_round: str):
    """
    it changes your game log
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
        else:
            new_content.append(content[1])
        new_content.append(f"{content[2][0:-1]}{str(int(content[2][-1]) + 1)}")
        new_content.append(content[3])
        for item in content[4::]:
            if str(guess_round) == item[0]:
                new_content.append(f"{item[0:-1]}{str(int(item[-1]) + 1)}")
            else:
                new_content.append(item)
    else:
        for item in content[1::]:
            if item[0:-1] == "Current winning streak: ":
                new_content.append("Current winning streak: 0")
            else:
                new_content.append(item)
    with open("winning streak.txt", "w") as fw:
        for item in new_content:
           fw.write(item + "\n")


def read_log():
    """
    it shows you the game log
    :return:
    """
    with open("winning streak.txt", "r") as fr:
        content_1 = fr.readlines()
    content = [item.strip() for item in content_1]
    for item in content:
        print(item)

print("Wordle gives players six chances to guess a randomly selected five-letter word."
      "If you have the right letter in the right spot, it shows up green."
      "A correct letter in the wrong spot shows up yellow. A letter that isn't in the word "
      "in any spot shows up gray.\n\nYou can enter a total of six words, meaning you can enter "
      "five burner words from which you can learn hints about the letters and their placements. "
      "Then you get one chance to put those hints to use. Or you can try for performance and "
      "guess the word of the day in three, two or even one go.")

all_words = list_all_5_letter_words()
correct_word = random_word(all_words)
words_guessed = []
print_words(words_guessed, correct_word)
for _ in range(6):
    words_you_chose(words_guessed, all_words)
    print_words(words_guessed, correct_word)
    if words_guessed[-1] == correct_word:
        print("You guessed the right word")
        change_game_log(True, str(len(words_guessed)))

        break
else:
    print(f"You lost, the correct word was {correct_word}")
    change_game_log(False, "0")
read_log()

