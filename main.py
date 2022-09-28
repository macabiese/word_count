# Emile Macabies 2022
# Compter le nombre de mots dans la phrase

def count_word():

    # Definition des variables en demandant a l'utilisateur d'ecrir une phrase
    phrase = input("Ecrire une phrase:")

    # Transforme la phrase en chaine de caractere
    nbr_mots = len(phrase.split(" "))

    # retourne le nombre de mots
    return str(nbr_mots)

# Definition de variable
x = count_word()

# Imprimer le nb de mots
print(x)