#Ejemplos de la funcion PRINT.

print("hola mundo")
print("hola mundo" , "otra vez")
print("son las", 9 , "de la mañana")
print("El resultado de 3 * 4 es:" , 3*4)

#Ejemplos de cadenas formatedas
print("El numero 15 en sistena decimal es %d, en sistemas octal %o, en el sistemas hexdecimal es %x" % (15, 15, 15))

pi = 3.1416
r = 5
print(f"el radio de un circulo es {r} y el area de ese circulo es {pi * r ** 2 : .2f}")
print(" la letra beta es: \n\t \u03b2")

#Caracteres de escape
print("hola mundo" , end = " ")
print("otra vez" , end = "\t")
