# /*
#  * Escribe un programa que imprima los 50 primeros números de la sucesión
#  * de Fibonacci empezando en 0.
#  * - La serie Fibonacci se compone por una sucesión de números en
#  *   la que el siguiente siempre es la suma de los dos anteriores.
#  *   0, 1, 1, 2, 3, 5, 8, 13...
#  */

def fibonnacci(n):
    n1 = 0
    n2 = 1
    count =0
    while count < n:
        print(n1)
        new = n1+n2
        n1 = n2 
        n2= new 
        count += 1

# valor = int(input("Write the limit for fibonnacci secuence: "))
fibonnacci(50)



