# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: miguel <miguel@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/15 11:13:34 by miguel            #+#    #+#              #
#    Updated: 2020/04/16 00:44:53 by miguel           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os

cookbook = {'sandwich': {'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'], 'meal': 'lunch', 'prep_time': 20},
            'cake': {'ingredients': ['flour', 'sugar', 'eggs'], 'meal': 'dessert', 'prep_time': 60},
            'salad': {'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'], 'meal': 'lunch', 'prep_time': 15}}


def print_recipe(name):

    if name in cookbook.keys():
        recipe = dict(cookbook[name])
        print(name)
        print("The ingredients we will need are:\t", end='')
        print(','.join(recipe['ingredients']))
        print("To be eaten for {meal}".format(**recipe))
        print("It takes {prep_time} minutes of cooking".format(**recipe))

    else:
        print("Your recipe is not in our list, please try again")
        exit(0)


def del_recipe(name):
    if name in cookbook.keys():
        cookbook.pop(name)
        print("Recipe was deleted sucessfully")
    else:
        print("Recipe cannot be found")
        exit(0)


def add_recipe(name, ingredients, meal, prep_time):
    recipe = {name: {'ingredients': ingredients,
                     'meal': meal, 'prep_time': prep_time}}
    cookbook.update(recipe)
    print("Added recipe.\n")


def print_all_recipes():
    for k in cookbook.keys():
        print_recipe(k)
        print()

def menu():
 
    print("Please select an option by typing the corresponding number:")
    print("1: Add Recipe")
    print("2: Delete Recipe")
    print("3: Print recipe")
    print("4: Print all recipes")
    print("5: Quit")

def main():

    while True:
        
        menu()
        num = int(input("\nType a number: "))
        os.system("clear")
        if num == 1:
            name = input("Recipe's name: ")
            amount = int(
                input("How many ingredients does your recipe have?\n"))
            if num > 0:
                ingredients = []
                print("Which are the ingredients?\n")
                for i in range(1, amount + 1):
                    print("{}.-".format(i), end='')
                    ingredients.append(input())
                meal = input("What kind of meal?\n")
                prep_time = input(
                    "How long do you spend cooking this recipe?\n")
                add_recipe(name, ingredients, meal, prep_time)
            else:
                print("You have to insert at least one ingredient")
                exit(0)
        elif num == 2:
            name = input("What recipe would you like to delete?\n")
            del_recipe(name)
        elif num == 3:
            name = input("What recipe would you like to see?\n")
            os.system("clear")
            print_recipe(name)
        elif num == 4:
            print_all_recipes()
        elif num == 5:
            print("Cookbook closed.")
            exit(0)
        else:
            print("To quit press 5.")


main()
