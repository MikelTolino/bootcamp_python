# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: miguel <miguel@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/14 19:54:36 by miguel            #+#    #+#              #
#    Updated: 2020/04/15 08:18:03 by miguel           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def text_analyzer(text):
    """This function counts the number of upper characters, lower characters, spaces
    and punctuaction points in a given text"""
    #if no param print "What is the text"
    spaces = upper = lower = p_mark = num = 0
    for c in text:
        num+=1
        if c is ' ':
            spaces+=1
        elif c.isupper():
            upper+=1
        elif c.islower():
            lower+=1
        elif c is '.' or ',':
            p_mark+=1
    
    print("The text contains {} characters".format(num))
    print("- {} upper letters".format(upper))
    print("- {} lower letters".format(lower))
    print("- {} puntuation marks".format(p_mark))
    print("- {} spaces".format(spaces))