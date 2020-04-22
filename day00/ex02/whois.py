# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: miguel <miguel@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/13 23:57:42 by miguel            #+#    #+#              #
#    Updated: 2020/04/14 00:17:37 by miguel           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

import sys

def main():
    
    if len(sys.argv) > 2:
        print ("ERROR")
        sys.exit()
    elif len(sys.argv) < 2:
        pass
    elif len(sys.argv) == 2 and sys.argv[1].isdigit():
        num = int(sys.argv[1])
        if num == 0:
            print("I'm zero")
        elif num % 2 == 0:
            print("I'm Even")
        elif num % 2 != 0:
            print("I'm Odd")
    else:
        print("ERROR")
    sys.exit()

main()