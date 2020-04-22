# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: miguel <miguel@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/15 09:11:14 by miguel            #+#    #+#              #
#    Updated: 2020/04/15 09:32:57 by miguel           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def main():
	
	languages = {
	'Python': 'Guido van Rossum',
	'Ruby': 'Yukihiro Matsumoto',
	'PHP': 'Rasmus Lerdorf',
	}
	for key, value in languages.items():
	   print("{} was created by {}".format(key, value))

main()