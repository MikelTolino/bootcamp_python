# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sos.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: miguel <miguel@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/16 01:57:50 by miguel            #+#    #+#              #
#    Updated: 2020/04/16 02:30:49 by miguel           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


def main():

    """
    This program will convert your string to morse code given some strings
    passed by argument.
    """
    error = False
    spaces = 0
    morse = {
        'a': '.-',
        'b': '-...',
        'c': '-.-.',
        'd': '-..',
        'e': '.',
        'f': '..-.',
        'g': '--.',
        'h': '....',
        'i': '..',
        'j': '.---',
        'k': '-.-',
        'l': '.-..',
        'm': '--',
        'n': '-.',
        'o': '---',
        'p': '.--.',
        'q': '--.-',
        'r': '.-.',
        's': '...',
        't': '-',
        'u': '..-',
        'v': '...-',
        'w': '.--',
        'x': '-..-',
        'y': '-.--',
        'z': '--..',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ' ': ' '
    }

    if len(sys.argv) < 2:
        pass
    else:
        string = ''
        for element in range(1, len(sys.argv)):
            string += sys.argv[element].lower()
        for c in string:
            if c not in morse:
                error = True
                break
            if c == ' ':
                spaces += 1

        if not error and spaces < len(string):
            for c in string:
                print(morse.get(c), end="")
            print("")
        else:
            print("ERROR")

    sys.exit()
