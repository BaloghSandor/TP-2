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

while boucle_jeu:

    borne_minimale = int(input('Donner la valeur minimale à deviner : '))
    borne_maximale = int(input('Donner la valeur maximale à deviner : '))

    def score():
        """
        Cette fonction est invoquée au moment oû le joueur n'a pas réussi leur essaie, afin de compter le nombre
        de fois que le joueur a essayer, lui montrant son score à la fin du jeu.
        """
        global nombre_de_essaies
        nombre_de_essaies = nombre_de_essaies + 1

    valeur_cherche = randint(borne_minimale, borne_maximale)

    print('\nVous devez deviner une valeur entre', borne_minimale, 'et', borne_maximale)

    valeur_non_trouver = True
    nombre_de_essaies = 0

    while valeur_non_trouver:
        score()
        essaie = int(input('\nEntrez votre essaie : '))

        if essaie == valeur_cherche:
            print(f'\nBravo! Vous avez trouvez la valeur en {nombre_de_essaies} essaies!')
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
