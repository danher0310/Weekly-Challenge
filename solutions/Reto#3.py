# /*
#  * Escribe un programa que se encargue de comprobar si un número es o no primo.
#  * Hecho esto, imprime los números primos entre 1 y 100.
#  */

def prime(n):
    primo = False
    if(n < 1):
        primo = False
    elif(n == 2):
        primo = True
        return n
    else:
        for i in range(2,n):                           
            if(n%i == 0):                
                primo = False  
                break             
            else:
                primo = True
    if(primo):
        return(n)   
                

result =""
for i in range(0,101):    
    check= prime(i)
    if(check != None):
        result += f'{str(check)}, '
    
print(result)
        
