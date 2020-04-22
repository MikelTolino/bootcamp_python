# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.pytest.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mmateo-t <mmateo-t@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/21 20:36:07 by mmateo-t          #+#    #+#              #
#    Updated: 2020/04/22 02:39:57 by mmateo-t         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Vector:
	def __init__(self, values):
		self.values = self.set_attributes(values) 
		self.size = None

	def set_attributes(self, values):
		if type(values) is list:
			return values
		elif type(values) is tuple:
			pass
		
			

def main():
	vector = Vector(3)
	print(vector.values)

if __name__ == "__main__":
	main()