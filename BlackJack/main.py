import random


def bet_or_quit(amount: int) -> str:
    """

    :return:
    """
    print(f"You have {amount} money")
    cash = input(f"How much do you bet? (1-{amount}, or QUIT)\n")
    while True:
        if str.lower(cash) == "quit":
            return str.lower(cash)
        try:
            cash = int(cash)
            if 1 < cash <= amount:
                return str(cash)
            else:
                print("You don't have enouh money")
        except ValueError:
            print('Error: your option is wrong')
        cash = input(f"How much do you bet? (1-{amount}, or QUIT)\n")


def deck_of_cards() -> list:
    """
    a list with all the cards in a deck
    :return:
    """
    symbols = ['♥', '♦', '♠', '♣']
    value_c = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return [f"{item_1}{item_2}" for item_2 in symbols for item_1 in value_c]


def take_a_card(deck_of_card: list):
    """
    take a random card from deck
    :return:
    """
    card = deck_of_card.pop(deck_of_card.index(random.choice(deck_of_card)))
    return card, deck_of_card


def options(bet, all_money):
    """
    Lets you choose what do you want to do
    :return:
    """
    option = input("(H)it, (S)tand, (D)ouble down\n")
    while option not in ["h", "s", "H", "S"]:
        if option in ["d", "D"] and int(bet) * 2 <= int(all_money):
            break
        else:
            print("You don,t have enough money")
        option = input("(H)it, (S)tand, (D)ouble down\n")

    return str.lower(option)


def options_1(bet, all_money):
    """
    Lets you choose what do you want to do
    :return:
    """
    option = input("(H)it, (S)tand\n")
    while option not in ["h", "s", "H", "S"]:
        option = input("(H)it, (S)tand\n")

    return str.lower(option)


def print_cards(list_of_cards):
    """
    shows the cads you have
    :return:
    """
    print(" ____   " * len(list_of_cards))
    second_row = ""
    third_row = ""
    forth_row = ""
    for item in list_of_cards:
        second_row = second_row + f"|{item[0:-1]}" + " " * (4 - len(item[0:-1])) + "|  "
        third_row += f"| {item[-1]} |  "
        forth_row = forth_row + "|" + "_" * (4 - len(item[0:-1])) + f"{item[0:-1]}|  "
    print(second_row)
    print(third_row)
    print(forth_row)
    print("")


def sum_cards(list_cards):
    """
    calculates the sum of your cards
    :param list_cards:
    :return:
    """
    how_many_A = 0
    sum_cards = 0
    for item in list_cards:
        if item[0:-1] in ["K", "Q", "J"]:
            sum_cards += 10
        elif item[0:-1] == "A":
            how_many_A += 1
        else:
            sum_cards += int(item[0:-1])
    for _ in range(how_many_A):
        if sum_cards + 11 <= 21:
            sum_cards += 11
        else:
            sum_cards += 1
    return sum_cards


def prints_dealer_cards(list_of_cards):
    """
    shows dealer's cards
    :param list_of_cards:
    :return:
    """
    print(" ____   " * len(list_of_cards))
    second_row = "|XXXX|  "
    third_row = "|XXXX|  "
    forth_row = "|XXXX|  "
    for item in list_of_cards[1::]:
        second_row = second_row + f"|{item[0:-1]}" + " " * (4 - len(item[0:-1])) + "|  "
        third_row += f"| {item[-1]} |  "
        forth_row = forth_row + "|" + "_" * (4 - len(item[0:-1])) + f"{item[0:-1]}|  "
    print(second_row)
    print(third_row)
    print(forth_row)
    print("")


def game_round(amount, all_money) -> int:
    """
    The player's options for playing his or her hand are:

    Hit: Take another card.
    Stand: Take no more cards.
    Double down: Double the wager, take exactly one more card, and then stand.
    :param amount:
    :param all_money:
    :return:
    """
    your_hand = []
    dealers_hand = []
    round_count = 0
    deck = deck_of_cards()
    for _ in range(2):
        card, deck = take_a_card(deck)
        your_hand.append(card)
    for _ in range(2):
        card, deck = take_a_card(deck)
        dealers_hand.append(card)
    print("Dealer has ? points")
    prints_dealer_cards(dealers_hand)

    print(f"You have {sum_cards(your_hand)} points")
    print_cards(your_hand)
    your_option = options(amount, all_money)
    while your_option == "h":
        round_count += 1
        card, deck = take_a_card(deck)
        your_hand.append(card)
        print("Dealer has ? points")
        prints_dealer_cards(dealers_hand)

        print(f"You have {sum_cards(your_hand)} points")
        print_cards(your_hand)
        if sum_cards(your_hand) > 21:
            break
        your_option = options_1(amount, all_money)

    else:
        if your_option == "d" and round_count == 0:
            amount = int(amount) * 2
            card, deck = take_a_card(deck)
            your_hand.append(card)
    while sum_cards(dealers_hand) < 17:
        card, deck = take_a_card(deck)
        dealers_hand.append(card)

    print(f"Dealer has {sum_cards(dealers_hand)} points")
    print_cards(dealers_hand)

    print(f"You have {sum_cards(your_hand)} points")
    print_cards(your_hand)

    if sum_cards(your_hand) > 21:
        print(f"You lost {amount} money")
        amount = int(amount) - int(amount) * 2
        return int(amount)
    elif sum_cards(dealers_hand) > 21:
        print(f"You won {amount} money")
        return int(amount)
    elif sum_cards(dealers_hand) > sum_cards(your_hand):
        print(f"You lost {amount} money")
        amount = int(amount) - int(amount) * 2
        return int(amount)
    elif sum_cards(dealers_hand) < sum_cards(your_hand):
        print(f"You won {amount} money")
        return int(amount)
    elif sum_cards(dealers_hand) == sum_cards(your_hand):
        print("Draw, the bet is returned to you")
        return 0


deck = deck_of_cards()
your_money = 5000
g_option = bet_or_quit(your_money)
while g_option != "quit":
    your_money = your_money + int((game_round(g_option, your_money)))
    if your_money == 0:
        break
    g_option = bet_or_quit(your_money)
else:
    print(f"Your balance is {your_money}")

