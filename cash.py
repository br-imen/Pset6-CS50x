from cs50 import get_float


def main():

    # how many cents the customer is owed
    cents = get_cents()
    cents = cents*100

    # calculate the number of quarters to give to customer
    quarters = calculate_quarters(cents)
    cents = cents - quarters * 25

    # calculate the number of dimes to give
    dimes = calculate_dimes(cents)
    cents = cents - dimes * 10

    # calculate the number of nickels to give
    nickels = calculate_nickels(cents)
    cents = cents - nickels * 5

    # calculate the number of pennies to give
    pennies = calculate_pennies(cents)
    cents = cents - pennies * 1

    # Sum coins
    coins = quarters + dimes + nickels + pennies

    # print totale number of coins to give
    coins = int(coins)
    print(coins)


def get_cents():

    while True:
        x = get_float("change owed : ")
        if x > 0:
            return x


def calculate_quarters(cents):

    q = cents / 25
    return int(q)


def calculate_dimes(cents):

    d = cents / 10
    return int(d)


def calculate_nickels(cents):
    n = cents / 5
    return int(n)


def calculate_pennies(cents):
    return cents


main()
