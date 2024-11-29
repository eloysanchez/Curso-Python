# Variables
"""
Seguir normas de python
minusculas con _ de separador
llamado snake case
"""

my_string_variable = "My string variable"
print(my_string_variable)

my_int_variable = 5

print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenacion de variables
print(my_string_variable, my_int_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Funciones del sistema
print(len(my_int_to_str_variable)) # Numero de caracteres

# Variables en una sola linea (No abusar)
name, surname, alias, age = "Eloy", "Sanchez", "Esanchez", 48
print("Me llamo:", name, surname, ". Mi edad es:", age)

print(type(age))