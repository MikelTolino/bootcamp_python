# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    game.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mmateo-t <mmateo-t@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/21 19:46:28 by mmateo-t          #+#    #+#              #
#    Updated: 2020/04/22 02:09:16 by mmateo-t         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class GotCharacter:
	"""A class that represents a Game of thrones Character"""
	def __init__(self, first_name, is_alive = True):
		self.first_name = first_name
		self.is_alive = is_alive


class Stark(GotCharacter):
	"""A class representing the Stark family. Or when bad things happen to good people."""
	def __init__(self, first_name=None, is_alive=True):
		super().__init__(first_name=first_name, is_alive=is_alive)
		self.family_name = "Stark"
		self.house_words = "Winter is Coming"
		
	def print_house_words(self):
		print(self.house_words)
		
	def die(self):
		self.is_alive = False

class Lannister(GotCharacter):
	def __init__(self, first_name=None, is_alive=True):
		super().__init__(first_name=first_name, is_alive=is_alive)
		self.family_name = "Lannister"
		self.house_words = "Hear Me Roar!"	

	def print_house_words(self):
		print(self.house_words)
		
	def die(self):
		self.is_alive = False
	
Arya = Stark("Arya")
print(Arya.house_words)