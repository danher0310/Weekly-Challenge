# /*
#  * Escribe una función que reciba dos palabras (String) y retorne
#  * verdadero o falso (Bool) según sean o no anagramas.
#  * - Un Anagrama consiste en formar una palabra reordenando TODAS
#  *   las letras de otra palabra inicial.
#  * - NO hace falta comprobar que ambas palabras existan.
#  * - Dos palabras exactamente iguales no son anagrama.
#  */

def checkAnagram():
    string1 = input("Please write the first word: ")
    string2 = input("Please write the second word: ")
    if (string1 != string2):
        string1 = "".join(sorted(string1.lower()))
        string2 = "".join(sorted(string2.lower()))
        if(string1 == string2):
            return(True)
        else:
            return(False)

    else:
        return "The same word can't be a anagram"

    

print(checkAnagram())