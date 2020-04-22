# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mmateo-t <mmateo-t@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/16 17:15:08 by miguel            #+#    #+#              #
#    Updated: 2020/04/21 23:44:54 by mmateo-t         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


class Recipe:

    def __init__(self, name, cooking_level, cooking_time, ingredients, description, recipe_type):

        self.name = self.check_name(name)
        self.cooking_level = self.check_cooking_level(cooking_level)
        self.cooking_time = self.check_cooking_time(cooking_time)
        self.ingredients = self.check_ingredients(ingredients)
        self. description = description
        self.recipe_type = self.check_recipe_type(recipe_type)

    def check_name(self, name):
        if not name:
            print("Name is empty")
            exit()
        return (name)

    def check_cooking_level(self, cooking_level):
        if cooking_level in range(1, 6):
            return cooking_level
        else:
            print("Cooking level is not ranked")
            exit()

    def check_cooking_time(self, cooking_time):
        if cooking_time > 0:
            return cooking_time
        else:
            print("Cooking time must be greater than 0")
            exit()

    def check_ingredients(self, ingredients):
        if not ingredients:
            print("The recipe has not ingredients")
            exit()
        else:
            return ingredients
    def check_recipe_type(self, recipe_type):
        if recipe_type == 'starter' or recipe_type == 'dessert' or recipe_type == 'lunch':
            return(recipe_type)
        else:
            print("Recipe type have to be 'starter' ,'dessert', 'lunch'")
            exit()

    def __str__(self):
        """Return the string to print with the recipe info"""
        string = """Recipe name: """ + self.name + "\nCooking level: " + str(self.cooking_level) + "\nCooking time: " + str(self.cooking_time) + "\nIngredients:" + str(self.ingredients) + "\nDescription: " + self.description + "\nRecipe Type: " + self.recipe_type
        return string