import sys
import ai
from game import Slideways
from gui import QApplication, MainWindow
from time import sleep

class Partie:
    """
    Classe d'une partie, relie le jeu avec le GUI
    """
    def __init__(self):
        """
        Initialise les objet jeu (base du jeux) et app + game_window (GUI front-end)
        :return: None
        """
        self.jeu = Slideways()
        self.app = QApplication(sys.argv)
        self.game_window = MainWindow()
        self.aiPlayers = (0, 0)
        self.winner = 0
        self.fini = False

        # Add restart buttons listener
        self.game_window.restartButton.clicked.connect(lambda:self.restart())

    def restart(self):
        """
        (Re)commence une partie avec les paramètres choisis dans le UI.
        :return: None
        """
        self.fini = False
        self.winner = 0
        self.jeu.reset()
        try:
            self.unloadListeners()
        except:
            pass
        self.game_window.update(self.jeu.plateau, self.jeu.decalage, self.jeu.dernier_coup, self.jeu.joueur)
        self.aiPlayers = (self.game_window.p1Input.currentIndex(), self.game_window.p2Input.currentIndex())

        if self.aiPlayers[0] == self.aiPlayers[1] == 1:
            self.aiGame()
        else:
            self.loadListeners()
            if self.aiPlayers[0] == 1:
                self.jeu.coup(ai.minimax(self.jeu.plateau, self.jeu.decalage, self.jeu.dernier_coup, self.jeu.joueur)[0])
                self.game_window.update(self.jeu.plateau, self.jeu.decalage, self.jeu.dernier_coup, self.jeu.joueur)

        #Changer le text du boutton start
        self.game_window.restartButton.setText("Restart")

    def coup(self, coords):
        """
        Effectue le coup coords, et met à jour le UI. 
        Si le joueur suivant est controllé par l'AI et le jeu n'est pas terminé, effectue aussi le coup suivant.
        :param: (tuple len = 2) coup: en format (y, x) pour un coup classique, ou (ligne, -1 ou -2) pour décler une ligne
        :return: None
        """
        self.jeu.coup(coords)
        self.game_window.update(self.jeu.plateau, self.jeu.decalage, self.jeu.dernier_coup, self.jeu.joueur)
        self.winner = self.jeu.check_winner()
        if self.winner != 0:
            self.game_window.update(self.jeu.plateau, self.jeu.decalage, self.jeu.dernier_coup, self.jeu.joueur, True)
            self.game_window.showGameOver((self.winner))
            self.fini = True

        if self.aiPlayers[self.jeu.joueur - 1] == 1 and not self.fini:
            coupAI = ai.minimax(self.jeu.plateau, self.jeu.decalage, self.jeu.dernier_coup, self.jeu.joueur)[0]
            if coupAI != None:
                sleep(self.game_window.aiSpeed.value() / 100)
                self.jeu.coup(coupAI)
                self.game_window.update(self.jeu.plateau, self.jeu.decalage, self.jeu.dernier_coup, self.jeu.joueur)
                self.winner = self.jeu.check_winner()
                if self.winner != 0:
                    self.game_window.update(self.jeu.plateau, self.jeu.decalage, self.jeu.dernier_coup, self.jeu.joueur, True)
                    self.game_window.showGameOver((self.winner))
                    self.fini = True


    def aiGame(self):
        """
        Lance une partie AI vs AI
        :return: None
        """
        while self.winner == 0:
            self.jeu.coup(ai.minimax(self.jeu.plateau, self.jeu.decalage, self.jeu.dernier_coup, self.jeu.joueur)[0])
            self.game_window.update(self.jeu.plateau, self.jeu.decalage, self.jeu.dernier_coup, self.jeu.joueur)
            sleep(self.game_window.aiSpeed.value() / 100)

            self.winner = self.jeu.check_winner()
            self.app.processEvents()
        
        self.game_window.update(self.jeu.plateau, self.jeu.decalage, self.jeu.dernier_coup, self.jeu.joueur, True)
        self.game_window.showGameOver(self.winner)
        self.fini = True

    def loadListeners(self):
        """
        Lie les boutons aux fontions adaptées.
        :retuen: None
        """
        # Add left buttons listeners
        self.game_window.left0.clicked.connect(lambda:self.coup((0, -1)))
        self.game_window.left1.clicked.connect(lambda:self.coup((1, -1)))
        self.game_window.left2.clicked.connect(lambda:self.coup((2, -1)))
        self.game_window.left3.clicked.connect(lambda:self.coup((3, -1)))
        
        # Add right buttons listeners
        self.game_window.right0.clicked.connect(lambda:self.coup((0, -2)))
        self.game_window.right1.clicked.connect(lambda:self.coup((1, -2)))
        self.game_window.right2.clicked.connect(lambda:self.coup((2, -2)))
        self.game_window.right3.clicked.connect(lambda:self.coup((3, -2)))
        
        # Add cell buttons listeners
        self.game_window.cell0.clicked.connect(lambda:self.coup((0, 0)))
        self.game_window.cell1.clicked.connect(lambda:self.coup((0, 1)))
        self.game_window.cell2.clicked.connect(lambda:self.coup((0, 2)))
        self.game_window.cell3.clicked.connect(lambda:self.coup((0, 3)))
        self.game_window.cell4.clicked.connect(lambda:self.coup((1, 0)))
        self.game_window.cell5.clicked.connect(lambda:self.coup((1, 1)))
        self.game_window.cell6.clicked.connect(lambda:self.coup((1, 2)))
        self.game_window.cell7.clicked.connect(lambda:self.coup((1, 3)))
        self.game_window.cell8.clicked.connect(lambda:self.coup((2, 0)))
        self.game_window.cell9.clicked.connect(lambda:self.coup((2, 1)))
        self.game_window.cell10.clicked.connect(lambda:self.coup((2, 2)))
        self.game_window.cell11.clicked.connect(lambda:self.coup((2, 3)))
        self.game_window.cell12.clicked.connect(lambda:self.coup((3, 0)))
        self.game_window.cell13.clicked.connect(lambda:self.coup((3, 1)))
        self.game_window.cell14.clicked.connect(lambda:self.coup((3, 2)))
        self.game_window.cell15.clicked.connect(lambda:self.coup((3, 3)))

    def unloadListeners(self):
        """
        Déconnecte tous les bouttons de leurs fontions.
        :retuen: None
        """
        # Add left buttons listeners
        self.game_window.left0.clicked.disconnect()
        self.game_window.left1.clicked.disconnect()
        self.game_window.left2.clicked.disconnect()
        self.game_window.left3.clicked.disconnect()
        
        # Add right buttons listeners
        self.game_window.right0.clicked.disconnect()
        self.game_window.right1.clicked.disconnect()
        self.game_window.right2.clicked.disconnect()
        self.game_window.right3.clicked.disconnect()
        
        # Add cell buttons listeners
        self.game_window.cell0.clicked.disconnect()
        self.game_window.cell1.clicked.disconnect()
        self.game_window.cell2.clicked.disconnect()
        self.game_window.cell3.clicked.disconnect()
        self.game_window.cell4.clicked.disconnect()
        self.game_window.cell5.clicked.disconnect()
        self.game_window.cell6.clicked.disconnect()
        self.game_window.cell7.clicked.disconnect()
        self.game_window.cell8.clicked.disconnect()
        self.game_window.cell9.clicked.disconnect()
        self.game_window.cell10.clicked.disconnect()
        self.game_window.cell11.clicked.disconnect()
        self.game_window.cell12.clicked.disconnect()
        self.game_window.cell13.clicked.disconnect()
        self.game_window.cell14.clicked.disconnect()
        self.game_window.cell15.clicked.disconnect()

# Code de base
if __name__ == "__main__":
    slideways = Partie()
    sys.exit(slideways.app.exec_()) # Execute le code tant que la fenêtre n'est pas fermée