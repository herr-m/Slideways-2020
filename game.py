class Slideways:
    """
    Classe d'un jeu Slideways
    """
    def __init__(self):
        """
        Initaialise l'objet avec:
            - un plateau nul
            - un vecteur de décalage nul
            - joueur 1
            - pas de dernier coup
        :return: None
        """
        self.plateau = [[0 for _ in range(4)] for _ in range(4)]
        self.decalage = [0 for _ in range(4)]
        self.joueur = 1
        self.dernier_coup = None

    def coup(self, coup):
        """
        Effectue de coup donné en parametre sur le plateau et le décalage, et swap de joueur
        :param: (tuple len = 2) coup: en format (y, x) pour un coup classique, ou (ligne, -1 ou -2) pour décler une ligne
        :return: None
        """
        if coup[1] == -1:
            self.decalage[coup[0]] -= 1
        elif coup[1] == -2:
            self.decalage[coup[0]] += 1
        else:
            self.plateau[coup[0]][coup[1]] = self.joueur

        self.dernier_coup = coup
        self.joueur = (self.joueur % 2) + 1

    def check_winner(self):
        """
        Renvoie le gagnent de la partie ou -1 si il y a égalité ou 0 si il n'y a pas de gagnant
        :return: -1, 0, 1 ou 2 (gagnant)
        """
        
        temp_grid = [[0 for _ in range(3 + self.decalage[i])] + [self.plateau[i][j] for j in range(4)] + [0 for _ in range(3 - self.decalage[i])] for i in range(4)]

        l = []

        # lignes
        for line in range(len(self.plateau)):
            l.append(set([self.plateau[line][x] for x in range(4)]))

        # colonnes
        for col in range(10):
            l.append(set([temp_grid[line][col] for line in range(4)]))

        #diagonales
        for col in range(7):
            l.append(set([temp_grid[i][col+i] for i in range(4)]))

        for col in range(6, -1, -1):
            l.append(set([temp_grid[i][col-i] for i in range(4)]))

        res = []
        for i in l:
            if len(i) == 1 and i != {0}:
                res.append(list(i)[0])

        return res[0] if len(res) == 1 else -1 if len(res) >= 2 else 0

    def reset(self):
        """
        Crée un nouveu plateau, vecteur de déalage et remet le joueur à 1
        :return: None
        """
        self.plateau = [[0 for _ in range(4)] for _ in range(4)]
        self.decalage = [0 for _ in range(4)]
        self.joueur = 1
        self.dernier_coup = None
