from copy import deepcopy
from random import choice

def check_winner(plateau, decalage):
    """
    Renvoie le gagnent de la partie representée dans le plateau et le décalage
    ou -1 si il y a égalité
    ou 0 si il n'y a pas de gagnent

    :param plateau: matrice 4x4 de 0, 1 et 2
    :param decalage: liste de longueur 4 contenant les valeurs -3 <= n <= 3
    :return: -1, 0, 1 ou 2 (gagnant)
    """
    # creation d'une matrice 4 x 10 afin de faciliter la verification
    temp_grid = [[0 for _ in range(3+decalage[i])] + [plateau[i][j] for j in range(4)] + [0 for _ in range(3 - decalage[i])] for i in range(4)]

    l = []
    # lignes
    for line in range(len(plateau)):
        l.append(set([plateau[line][x] for x in range(4)]))

    # colonnes
    for col in range(10):
        l.append(set([temp_grid[line][col] for line in range(4)]))

    # diagonales
    for col in range(7):
        l.append(set([temp_grid[i][col+i] for i in range(4)]))

    for col in range(6, -1, -1):
        l.append(set([temp_grid[i][col-i] for i in range(4)]))

    res = []
    for i in l:
        if len(i) == 1 and i != {0}:
            res.append(list(i)[0])

    # return le gagnant, 0 si pas de gagnant ou -1 si egalite
    return res[0] if len(res) == 1 else -1 if len(res) >= 2 else 0

def coup_AI(plateau, decalage, joueur, coup):
    """
    Effectue le coup donné en parametre sur le plateau et le veteur de décalage.

    :param plateau: matrice 4x4 de 0, 1 et 2
    :param decalage: liste de longueur 4 contenant les valeurs -3 <= n <= 3
    :param joueur: (int) joueur à représenter (1 ou 2)
    :param coup: (tuble) le coup à affectuer en format (y, x)
    :return: None
    """
    if coup[1] == -1:
        decalage[coup[0]] -= 1
    elif coup[1] == -2:
        decalage[coup[0]] += 1
    else:
        plateau[coup[0]][coup[1]] = joueur

def minimax(plateau, decalage, dernier_coup, j, profondeur=2, maxi=True):
    """
    Simule tout les coups possibles, essaye de prévoir le coup suivant et évalue le meilleur coup pour le joueur 2.

    :param plateau: matrice 4x4 de 0, 1 et 2
    :param decalage: liste de longueur 4 contenant les valeurs -3 <= n <= 3
    :param dernier_coup: (tuple) dernier coup en format (y, x)
    :param profondeur: (int) Combien de coups suivants prévoir (2 par défaut)
    :param maxi: (bool) True pour trouver le meilleur coup ou False pour trover le pire (True par defaut)
    :return: ((tuple len = 2), int) Le meilleur coup et son score (0,1 ou -1)
    """

    # Crée la liste de coups possibles
    coups_possibles = [(x, y) for x in range(4) for y in range(4) if (plateau[y][x] != j and (x, y) != dernier_coup) ]  + \
                          [(line, -1) for line in range(4) if dernier_coup != (line, -2) and decalage[line] > -3] + \
                          [(line, -2) for line in range(4) if dernier_coup != (line, -1) and decalage[line] < 3]

    # Evalue le score du plateau
    gagnant = check_winner(plateau, decalage)
    if maxi:
        score = 1 if gagnant == j else -1 if gagnant == (j%2)+1 else 0
    else:
        score = -1 if gagnant == j else 1 if gagnant == (j%2)+1 else 0

    if profondeur == 0 or score == 1 or score == -1:
        return (None, score)

    else:
        if maxi:
            meilleurscore = -1
            meilleurcoup = []
            for coup in coups_possibles:
                plateau_test = deepcopy(plateau)
                decal_test = deepcopy(decalage)

                coup_AI(plateau_test, decal_test, j, coup)

                score = minimax(plateau_test, decal_test, coup, (j % 2) + 1, profondeur-1, False)[1]
                if meilleurscore < score:
                    meilleurscore = score
                    meilleurcoup = [(coup, score)]
                elif meilleurscore == score:
                    meilleurcoup.append((coup, score))

        else:
            meilleurscore = 1
            meilleurcoup = []
            for coup in coups_possibles:
                plateau_test = deepcopy(plateau)
                decal_test = deepcopy(decalage)
                
                coup_AI(plateau_test, decal_test, j, coup)

                score = minimax(plateau_test, decal_test, coup, (j % 2) + 1, profondeur-1, True)[1]
                if meilleurscore > score:
                    meilleurscore = score
                    meilleurcoup = [(coup, score)]
                elif meilleurscore == score:
                    meilleurcoup.append((coup, score))

    # si plusieurs coup, utilise choice pour en tirer un au hazard
    return choice(meilleurcoup) if len(meilleurcoup) > 0 else choice(coups_possibles)
