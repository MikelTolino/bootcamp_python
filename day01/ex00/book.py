# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mmateo-t <mmateo-t@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/16 17:15:06 by miguel            #+#    #+#              #
#    Updated: 2020/04/22 01:53:19 by mmateo-t         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import datetime
from recipe import Recipe

class Book:
	def __init__(self, name):
		
		self.name = self.check_name(name)
		self.last_update = datetime.datetime.now()
		self.creation_date = datetime.datetime.now()
		self.recipes_list = {"starter" : [] , "dessert" : [] , "lunch" : []}

	def check_name(self, name):
		if  not name:
			print("No name has been written")
			exit()
		return name
		
	#We must identify which is the name and print only that recipe, now we print all recipes
	def get_recipe_by_name(self, name):
		for recipe in self.recipes_list.get("lunch"):
			if recipe.name == name:
				print(str(recipe))
			return recipe
		
		for recipe in self.recipes_list.get("dessert"):
			if recipe.name == name:
				print(str(recipe))
			return recipe

		for recipe in self.recipes_list.get("starter"):
			if recipe.name == name:
				print(str(recipe))
			return recipe
		
			
	def get_recipes_by_types(self, recipe_type):
		"""Get all recipe names for a given recipe_type """
		lista = []
		if recipe_type not in self.recipes_list.keys():
			print("There is not any recipe type")
			exit()
		for recipe in self.recipes_list.get(recipe_type):
			lista.append(recipe.name)
		return lista
		
	def add_recipe(self, recipe):
		try:
			if isinstance(recipe, Recipe):
				pass
				try:

					if recipe.recipe_type == "lunch":
						self.recipes_list["lunch"].append(recipe)
					elif recipe.recipe_type == "dessert":
						self.recipes_list["dessert"].append(recipe)
					elif recipe.recipe_type == "starter": 
						self.recipes_list["starter"].append(recipe)
					self.last_update = datetime.datetime.now()
				except KeyError as ke:
					print("There is not any recipe type, {}".format(ke))
					exit()
		except:
			print("Recipe is not instance")
			exit()
			