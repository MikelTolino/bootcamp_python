# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: miguel <miguel@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/16 03:39:20 by miguel            #+#    #+#              #
#    Updated: 2020/04/16 16:55:20 by miguel           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time
import os
from time import sleep


def ft_progress(lst):

    bar = '>'
    t1 = time.time()
    for i in lst:
        percent = round((i / len(lst)) * 100)
        if i % 100 == 0:
            bar = '=' + bar
        print("ETA: {} [{}%] [{}] {}/{} | elapsed time {}".format(round(time.time() - t1,2), percent, bar.ljust(11, " "), i, len(lst), round(time.time() - t1,2)))
        yield i

def main():
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        
        ret += (elem + 3) % 5
        sleep(0.01)
        if elem < len(listy) - 1:
            os.system("clear")            
    print("...")
    print(ret)

main()