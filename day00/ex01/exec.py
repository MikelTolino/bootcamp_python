# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: miguel <miguel@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/13 23:57:47 by miguel            #+#    #+#              #
#    Updated: 2020/04/14 20:44:56 by miguel           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

import sys
#Does not work with !

def main():
	str = ''
	if len(sys.argv) >= 2:
			str = ' '.join(sys.argv[1:])
	str_inv = str[::-1]
	final_str = ''
	for c in str_inv:
		if c.isupper() and c.isalpha():
			final_str += c.lower()
		elif c.islower() and c.isalpha():
			final_str += c.upper()
		else:
			final_str += c

	print(final_str)

main()
