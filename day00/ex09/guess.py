# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: miguel <miguel@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/16 02:33:44 by miguel            #+#    #+#              #
#    Updated: 2020/04/16 03:15:33 by miguel           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random


def menu():
    print("""This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!""")


def main():

    i = 0
    secret = random.randint(1, 99)
    menu()
    while True:

        num = (input("Insert a number between 1-99\n"))
        if num == 'exit':
            exit()
        while not num.isdigit():
            num = input("This is not a digit, please use another: ")

        num = int(num)
        while num < 0 or num > 99:
            num = int(input("Not valid number, try again: "))
        if num == secret:
            if secret == 42:
                print("The answer to the ultimate question of life, the universe and everything is 42.Congratulations! You got it on your first try!")
            else:
                print("Congratulations!!! You won in {} attemps".format(str(i)))
            exit()
        elif num < secret:
            print("Too low!")
        elif num > secret:
            print("Too high!")
        i += 1


if __name__ == '__main__':
    main()
