"""
Programme fait par Sandor Balogh
Groupe: 403
Description : Ce code est un jeu de devinette où le joueur doit deviner un nombre entre 1 et 100 et faire cela
jusqu'au temps qu'il soit capable de le deviner. À la fin, on lui demande s'il voudrait continuer ou arrêter.
Dans le cas où il veut continuer le programme recommence, mais dans le cas où il veut arrêter la boucle s'arrête.
On dit également le nombre d'essaie qu'il falait pour que le joueur puisse deviner le nombre.
"""


from random import randint

boucle_jeu = True

while boucle_jeu:
    valeur_cherche = randint(0, 100)

    valeur_non_trouver = True
    nombre_de_essaies = 0

    while valeur_non_trouver:
        nombre_de_essaies += 1
        essaie = int(input('Devinez le nombre choisi entre 1 et 100 : '))

        if essaie == valeur_cherche:
            print('\nBravo! Vous avez trouvez la valeur en', nombre_de_essaies, 'essaies!')
            recommencer = str(input('\nVoulez-vous recommencer (oui ou non)?'))

            if recommencer == 'oui':
                valeur_non_trouver = False

            elif recommencer == 'non':
                print('Merci et aurevoir!')
                valeur_non_trouver = False
                boucle_jeu = False

        elif essaie > valeur_cherche:
            print('\nOups! Le nombre que vous cherchez est plus petit que', essaie)
            continue

        else:
            print('\nOups! Le nombre que vous cherchez est plus grand que', essaie)
            continue
