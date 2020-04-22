# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: miguel <miguel@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/16 01:01:00 by miguel            #+#    #+#              #
#    Updated: 2020/04/16 02:32:12 by miguel           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string
import re


def main():
    """
    Using list comprehensions,this program removes 
    all the words in a string that are shorter than or equal to n letters, and returns the filtered list with no punctuation.
    The program will accept only two parameters: a string, and an integer n.
    """
    if len(sys.argv) != 3 or sys.argv[1].isdigit() or not sys.argv[2].isdigit():
        print("ERROR")
        sys.exit()
    else:
        lista = [word for word in re.sub('[%s]' % re.escape(
            string.punctuation), ' ', sys.argv[1]).split(" ") if len(word) > len(sys.argv[2])]
        print(lista)


if __name__ == '__main__':
    main()
