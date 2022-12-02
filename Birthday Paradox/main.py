import random


def get_random_month() -> str:
    """
    This returns a random month
    :return:month
    """
    month_l = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
    return random.choice(month_l)


def get_random_date(month: str) -> str:
    """
    This returns a random day from a month
    :param month:
    :return: day
    """
    if month in ["jan", "mar", "may", "jul", "aug", "oct", "dec"]:
        return f"{month} {random.choice(range(1, 32))}"
    elif month in ["apr", "jun", "sep", "nov"]:
        return f"{month} {random.choice(range(1, 31))}"
    elif month == "feb":
        return f"{month} {random.choice(range(1, 29))}"


def get_group_size():
    """
    returns an input
    :return:
    """
    while True:
        try:
            group_size = int(input("What is your group size?:"))
        except ValueError:
            print(f'Your group_size must be written with digits')
        else:
            break
    return group_size


def find_if_date_repeats(group_size: int) -> int:
    """
    gives a date to everyone from group size. if a date
    repeats it returns 100 if not it returns 0
    :param group_size:
    :return: 0/100
    """
    output = 0
    date_list = [get_random_date(get_random_month()) for _ in range(group_size)]
    if len(date_list) != len(set(date_list)):
        output = 100
    return output


def average_from_list(number_list: list) -> int:
    """
    calculates avarge from alist
    :param number_list:
    :return:
    """
    l_sum = sum(number_list)
    return l_sum / len(number_list)


group_size = get_group_size()
list_chances = []
for _ in range(10000):
    list_chances.append(find_if_date_repeats(group_size))

print(f"There’s a {average_from_list(list_chances)} percent chance of a matching birthday.")
