"""
Programme fait par Sandor Balogh
Groupe: 403
Description : Ce code est un jeu de devinette où le joueur doit deviner un nombre entre deux nombres de son choix
et faire cela jusqu'au temps qu'il soit capable de le deviner. À la fin, on lui demande s'il voudrait continuer
ou arrêter. Dans le cas où il veut continuer le programme recommence, mais dans le cas où il veut arrêter la
boucle s'arrête. On dit également le nombre d'essaie qu'il falait pour que le joueur puisse deviner le nombre.
"""

from random import randint

boucle_jeu = True

borne_minimale = 0
borne_maximale = 0


def bornes_minimale_et_maximale():
    """
    Cette fonction est invoquée au début du jeu afin de permettre à l'utilisateur de choisir les bornes du nombre
    à trouver. On retourne à la fin le borne minimale et le borne maximale, pour continuer le jeu.
    """
    global borne_minimale
    global borne_maximale
    borne_minimal = int(input('Choisisez la valeur minimale a deviner : '))
    borne_maximal = int(input('\nChoisisez la valeur maximale a deviner : '))


while boucle_jeu:
    bornes_minimale_et_maximale()
    valeur_cherche = randint(borne_minimale, borne_maximale)

    print('\nVous devez deviner une valeur entre', borne_minimale, 'et', borne_maximale)

    valeur_non_trouver = True
    nombre_de_essaies = 0
    while valeur_non_trouver:
        nombre_de_essaies += 1
        essaie = int(input('\nEntrez votre essaie : '))

        if essaie == valeur_cherche:
            print('\nBravo! Vous avez trouvez la valeur en', nombre_de_essaies, 'essaies!')
            recommencer = str(input('\nVoulez-vous recommencer (oui ou non)? '))

            if recommencer == 'oui':
                valeur_non_trouver = False

            elif recommencer == 'non':
                print('\nMerci et aurevoir!')
                valeur_non_trouver = False
                boucle_jeu = False

        elif essaie > valeur_cherche:
            print('\nOups! Le nombre que vous cherchez est plus petit que', essaie)
            continue

        else:
            print('\nOups! Le nombre que vous cherchez est plus grand que', essaie)
            continue
