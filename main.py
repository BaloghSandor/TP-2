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


def recommencer():
    """
    Cette fonction est invoquée au moment oû le joueur a pas réussi leur essaie, et on le demande s'il veut
    quitter ou joueur une nouvelle partie.
    """
    global valeur_non_trouver
    global boucle_jeu
    global nombre_de_essaies
    print('\nBravo! Vous avez trouvez la valeur en', nombre_de_essaies, 'essaies!')
    demande_du_joueur = str(input('\nVoulez-vous recommencer (oui ou non)? '))

    if demande_du_joueur == 'oui':
        valeur_non_trouver = False

    elif demande_du_joueur == 'non':
        print('\nMerci et aurevoir!')
        valeur_non_trouver = False
        boucle_jeu = False


while boucle_jeu:

    borne_minimale = int(input('Donner la valeur minimale à deviner : '))
    borne_maximale = int(input('Donner la valeur maximale à deviner : '))

    valeur_cherche = randint(borne_minimale, borne_maximale)

    print('\nVous devez deviner une valeur entre', borne_minimale, 'et', borne_maximale)

    valeur_non_trouver = True
    nombre_de_essaies = 0

    while valeur_non_trouver:
        nombre_de_essaies = nombre_de_essaies + 1
        essaie = int(input('\nEntrez votre essaie : '))

        if essaie == valeur_cherche:
            recommencer()

        elif essaie > valeur_cherche:
            print('\nOups! Le nombre que vous cherchez est plus petit que', essaie)
            continue

        else:
            print('\nOups! Le nombre que vous cherchez est plus grand que', essaie)
            continue
