#variables
my_var = "mi variable string"
print(my_var)#variable tipo string  

my_int = 5
print(my_int)#variable tipo entera

my_bool = True
print(my_bool)#variable tipo booleana

#concatenación de variables en un print
print(my_var,my_int,my_bool)

my_int_to_str = str(my_int)
print(my_int_to_str)
print(type(my_int_to_str))

#algunas funciones del sistema
print(len(my_var))

#variables en una sola linea 
name, surname, alias, age = "nicolas", "polo", "nico", 26
print("me llamo:", name, surname, ".mi edad es de ", age, "y mi alias es ", alias)

#input, para ingresar valores
first_name = input('cual es tu nombre: ')
age1 = input('cual es tu edad? ')

print(first_name)
print(age1)
