# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.pytest.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mmateo-t <mmateo-t@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/21 20:36:07 by mmateo-t          #+#    #+#              #
#    Updated: 2020/04/25 17:06:26 by mmateo-t         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Vector:
	
	def __init__(self, values):
		self.values = self.set_attributes(values) 
		self.size = len(self.values)
	
	def __add__(self, other):
		lista = []
		if self.size != other.size:
			print("Different vectors size")
			exit()
		else:
			for i in range(self.size):
				lista.append(self.values[i] + other.values[i])
		return Vector(lista)

	def __radd__(self, other):
		lista = []
		if self.size != other.size:
			print("Different vectors size")
			exit()
		else:
			for i in range(self.size):
				lista.append(other.values[i] + self.values[i])
		return Vector(lista)

		
	def __sub__(self, other):
		lista = []
		if self.size != other.size:
			print("Different vectors size")
			exit()
		else:
			for i in range(self.size):
				lista.append(self.values[i] - other.values[i])
		return Vector(lista)

	def __rsub__(self, other):
		lista = []
		if self.size != other.size:
			print("Different vectors size")
			exit()
		else:
			for i in range(self.size):
				lista.append(other.values[i] - self.values[i])
		return Vector(lista)

	def __truediv__(self, other):
		lista = []
		if not other:
			print("Divider must be a scalar")
			exit()
		else:	
			for i in range(self.size):
				try:
					lista.append(self.values[i] / other)
				except ZeroDivisionError:
					print("Error. Division by 0")
					exit()
		return Vector(lista)

	def __rtruediv__(self, other):
		lista = []
		if not other:
			print("Divider must be a scalar")
			exit()
		else:
			for i in range(self.size):
				try:
					lista.append(other / self.values[i])
				except ZeroDivisionError:
					print("Error. Division by 0")
					exit()
		return Vector(lista)

	def __mul__(self, other):
		lista = []
		if type(other) is int:
			for i in range(self.size):
				lista.append(self.values[i] * other)
		else:
			for i in range(self.size):
				if self.size == other.size:
					lista.append(self.values[i] * other.values[i])
				elif other.size == 1:
					lista.append(self.values[i] * other.values[0])
				else:
					print("Operation unsucessful.")
					exit()
		return Vector(lista)

	def __rmul__(self, other):
		lista = []
		if type(other) is int:
			for i in range(self.size):
				lista.append(other * self.values[i])
		else:
			for i in range(self.size):
				if self.size == other.size:
					lista.append(other.values[i] * self.values[i])
				elif other.size == 1:
					lista.append(other.values[0] * self.values[i])
				else:
					print("Operation unsucessful.")
					exit()
		return Vector(lista)

	def __str__(self):
		return ("(Vector " + str(self.values) + ")")

	def __repr__(self):
		return([self.values, self.size])
		
	def conv2float(self,values):
		lista = []
		try:
			for i in values:
				lista.append(float(i))
		except:
			print("It should be a number")
			exit()
		return(lista)
			
	def set_attributes(self, values):
		if type(values) is list:
			return self.conv2float(values)
			
		elif type(values) is tuple:
			if values[0] > values[1]:
				return (self.conv2float(list(range(values[0], values[1], -1))))
			else:
				return (self.conv2float(list(range(values[0], values[1]))))
		elif type(values) is int:
			return (self.conv2float(list(range(values))))
		else:
			print("Bad value")
			exit()
		

def main():
	v1 = Vector(5)
	v2 = Vector(5)

	print(v1 - v2)
	print(v1 + v2)
	print(v2 - v1)
	print(v2 + v1)
	print(v1 * v2)
	print(v2 * v1)
	print(5 / v1)


if __name__ == "__main__":
	main()