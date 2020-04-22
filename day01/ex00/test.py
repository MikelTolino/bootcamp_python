# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mmateo-t <mmateo-t@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/16 17:15:00 by miguel            #+#    #+#              #
#    Updated: 2020/04/22 01:54:33 by mmateo-t         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from book import Book
from recipe import Recipe


def main():
    tourte = Recipe("Lasana", 2, 20, ["leche", "huevos", "jamon"], "MEjor receta", 'dessert')
    tourte2 = Recipe("Pizza", 2, 20, ["leche", "huevos", "jamon"], "MEjor receta", 'lunch')
    to_print = str(tourte)
    #print(to_print)
    
    libro = Book("Librito")
    libro.add_recipe(tourte)
    libro.add_recipe(tourte2)
    recipe = libro.get_recipes_by_types("lunch")
    receta = libro.get_recipe_by_name("Pizzza")
    print(recipe)
    
if __name__ == '__main__':
    main()