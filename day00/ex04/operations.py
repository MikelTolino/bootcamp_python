# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: miguel <miguel@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/15 08:20:14 by miguel            #+#    #+#              #
#    Updated: 2020/04/15 08:43:31 by miguel           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def main():
    	
	if len(sys.argv) != 3:
		print("Usage: python operations.py\nExample: python operations.py 10 3")
		sys.exit()
	#"234" "hola"
	x = int(sys.argv[1])	
	y = int(sys.argv[2])
	print("Sum:\t{}".format(x + y))
	print("Difference:\t{}".format(x - y))
	print("Product:\t{}".format(x * y))
	try:
		print("Quotient:\t{}".format(x / y))
		print("Remainder:\t{}".format(x % y))
	except ZeroDivisionError:
		print("Quotiente:\tERROR (Division by 0)")
		print("Remainder:\tERROR (modulo by 0)")
	sys.exit()
		
main()