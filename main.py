# Emile Macabies 2022
# Compter le nombre de mots dans la phrase

# Definition des variables en demandant a l'utilisateur d'ecrire une phrase
phrase = input("Ecrire une phrase:")

# Fonction qui prend un input string et qui retourne le nombre de mots dans la phrase
def count_word(phrase):

    # Transforme la phrase en chaine de caractere
    nbr_mots = len(phrase.split(" "))

    # retourne le nombre de mots
    return str(nbr_mots)

# Definition de variable
x = count_word(phrase)

# Imprimer le nb de mots
print(x)