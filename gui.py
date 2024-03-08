from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QComboBox, QSlider, QLabel, QPushButton
from PyQt5.QtCore import QRect, Qt

class MainWindow(QMainWindow):
    """
    Classe de la fenêtre du jeu.
    """
    def __init__(self):
        """
        Initialise un UI PyQT
        :return: None
        """
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        Fixe la taille de a fenêtre à 800x600, son titre, et appelle les methode qui chargent les bouttons.
        :return: None
        """
        self.setGeometry(50, 50, 800, 600)
        self.setFixedSize(800, 600)
        self.setWindowTitle('Slideways')

        self.loadSettingsTab()
        self.loadLeftTab()
        self.loadGameTab()
        self.loadRightTab()
        self.loadRestartButton()
        self.loadGameOver()
        
        self.show()

    def loadSettingsTab(self):
        """
        Charge les options du choix des joueurs et du delais de l'AI
        :return: None
        """
        self.settingsTab = QWidget(self)
        self.settingsTab.setGeometry(QRect(5, 5, 790, 80))

        self.p1Label = QLabel(self.settingsTab)
        self.p1Label.setGeometry(QRect(5, 5, 50, 20))
        self.p1Label.setText('Joueur 1 :')
        self.p1Input = QComboBox(self.settingsTab)
        self.p1Input.setGeometry(QRect(100, 5, 685, 20))
        self.p1Input.addItems(("Joueur", "AI"))

        self.p2Label = QLabel(self.settingsTab)
        self.p2Label.setGeometry(QRect(5, 30, 50, 20))
        self.p2Label.setText('Joueur 2 :')
        self.p2Input = QComboBox(self.settingsTab)
        self.p2Input.setGeometry(QRect(100, 30, 685, 20))
        self.p2Input.addItems(("Joueur", "AI"))

        self.speedLabel = QLabel(self.settingsTab)
        self.speedLabel.setGeometry(QRect(5, 55, 50, 20))
        self.speedLabel.setText('Delais :')
        self.aiSpeed = QSlider(self.settingsTab)
        self.aiSpeed.setGeometry(QRect(100, 55, 685, 20))
        self.aiSpeed.setOrientation(Qt.Horizontal)


    def loadLeftTab(self):
        """
        Charge les boutons de décalage vers la gauche
        :return: None
        """
        self.leftTab = QWidget(self)
        self.leftTab.setGeometry(QRect(10, 150, 25, 315))

        self.left0 = QPushButton(self.leftTab)
        self.left0.setGeometry(QRect(0, 0, 25, 70))
        self.left0.setText('<')

        self.left1 = QPushButton(self.leftTab)
        self.left1.setGeometry(QRect(0, 75, 25, 70))
        self.left1.setText('<')

        self.left2 = QPushButton(self.leftTab)
        self.left2.setGeometry(QRect(0, 150, 25, 70))
        self.left2.setText('<')

        self.left3 = QPushButton(self.leftTab)
        self.left3.setGeometry(QRect(0, 225, 25, 70))
        self.left3.setText('<')

    def loadRightTab(self):
        """
        Charge les boutons de décalage vers la droite
        :return: None
        """
        self.rightTab = QWidget(self)
        self.rightTab.setGeometry(QRect(765, 150, 25, 315))

        self.right0 = QPushButton(self.rightTab)
        self.right0.setGeometry(QRect(0, 0, 25, 70))
        self.right0.setText('>')

        self.right1 = QPushButton(self.rightTab)
        self.right1.setGeometry(QRect(0, 75, 25, 70))
        self.right1.setText('>')

        self.right2 = QPushButton(self.rightTab)
        self.right2.setGeometry(QRect(0, 150, 25, 70))
        self.right2.setText('>')

        self.right3 = QPushButton(self.rightTab)
        self.right3.setGeometry(QRect(0, 225, 25, 70))
        self.right3.setText('>')

    def loadGameTab(self):
        """
        Charge les lignes et les bouttons pour les cases de couleurs.
        :return: None
        """
        self.gameTab = QWidget(self)
        self.gameTab.setGeometry(QRect(50, 150, 700, 315))

        #Line 1
        self.line0 = QWidget(self.gameTab)
        self.line0.setGeometry(QRect(210, 0, 280, 70))
        self.line0.setStyleSheet("QWidget {background-color: blue}")

        self.cell0 = QPushButton(self.line0)
        self.cell0.setGeometry(QRect(15, 15, 40, 40))
        self.cell0.setStyleSheet("QWidget {background-color: darkblue; color: darkblue;}")

        self.cell1 = QPushButton(self.line0)
        self.cell1.setGeometry(QRect(85, 15, 40, 40))
        self.cell1.setStyleSheet("QWidget {background-color: darkblue; color: darkblue;}")

        self.cell2 = QPushButton(self.line0)
        self.cell2.setGeometry(QRect(155, 15, 40, 40))
        self.cell2.setStyleSheet("QWidget {background-color: darkblue; color: darkblue;}")

        self.cell3 = QPushButton(self.line0)
        self.cell3.setGeometry(QRect(225, 15, 40, 40))
        self.cell3.setStyleSheet("QWidget {background-color: darkblue; color: darkblue;}")

        #Line 2
        self.line1 = QWidget(self.gameTab)
        self.line1.setGeometry(QRect(210, 75, 280, 70))
        self.line1.setStyleSheet("QWidget {background-color: blue}")
        
        self.cell4 = QPushButton(self.line1)
        self.cell4.setGeometry(QRect(15, 15, 40, 40))
        self.cell4.setStyleSheet("QWidget {background-color: darkblue; color: darkblue;}")

        self.cell5 = QPushButton(self.line1)
        self.cell5.setGeometry(QRect(85, 15, 40, 40))
        self.cell5.setStyleSheet("QWidget {background-color: darkblue; color: darkblue;}")

        self.cell6 = QPushButton(self.line1)
        self.cell6.setGeometry(QRect(155, 15, 40, 40))
        self.cell6.setStyleSheet("QWidget {background-color: darkblue; color: darkblue;}")

        self.cell7 = QPushButton(self.line1)
        self.cell7.setGeometry(QRect(225, 15, 40, 40))
        self.cell7.setStyleSheet("QWidget {background-color: darkblue; color: darkblue;}")

        #Line 3
        self.line2 = QWidget(self.gameTab)
        self.line2.setGeometry(QRect(210, 150, 280, 70))
        self.line2.setStyleSheet("QWidget {background-color: blue}")

        self.cell8 = QPushButton(self.line2)
        self.cell8.setGeometry(QRect(15, 15, 40, 40))
        self.cell8.setStyleSheet("QWidget {background-color: darkblue; color: darkblue;}")

        self.cell9 = QPushButton(self.line2)
        self.cell9.setGeometry(QRect(85, 15, 40, 40))
        self.cell9.setStyleSheet("QWidget {background-color: darkblue; color: darkblue;}")

        self.cell10 = QPushButton(self.line2)
        self.cell10.setGeometry(QRect(155, 15, 40, 40))
        self.cell10.setStyleSheet("QWidget {background-color: darkblue; color: darkblue;}")

        self.cell11 = QPushButton(self.line2)
        self.cell11.setGeometry(QRect(225, 15, 40, 40))
        self.cell11.setStyleSheet("QWidget {background-color: darkblue; color: darkblue;}")

        #Line 4
        self.line3 = QWidget(self.gameTab)
        self.line3.setGeometry(QRect(210, 225, 280, 70))
        self.line3.setStyleSheet("QWidget {background-color: blue}")

        self.cell12 = QPushButton(self.line3)
        self.cell12.setGeometry(QRect(15, 15, 40, 40))
        self.cell12.setStyleSheet("QWidget {background-color: darkblue; color: darkblue;}")

        self.cell13 = QPushButton(self.line3)
        self.cell13.setGeometry(QRect(85, 15, 40, 40))
        self.cell13.setStyleSheet("QWidget {background-color: darkblue; color: darkblue;}")

        self.cell14 = QPushButton(self.line3)
        self.cell14.setGeometry(QRect(155, 15, 40, 40))
        self.cell14.setStyleSheet("QWidget {background-color: darkblue; color: darkblue;}")

        self.cell15 = QPushButton(self.line3)
        self.cell15.setGeometry(QRect(225, 15, 40, 40))
        self.cell15.setStyleSheet("QWidget {background-color: darkblue; color: darkblue;}")

    def loadRestartButton(self):
        """
        Charge le boutton de start/restart
        :return: None
        """
        self.restartButton = QPushButton(self)
        self.restartButton.setGeometry(300, 550, 200, 40)
        self.restartButton.setText("Start")

    def loadGameOver(self):
        """
        Charge l'écran de fin de jeu sans l'afficher
        :return: None
        """
        self.gameOverScreen = QWidget(self)
        self.gameOverText = QLabel(self.gameOverScreen)
        self.closeButton = QPushButton(self.gameOverScreen)
        self.closeButton.clicked.connect(lambda:self.closeGameOver())
        self.closeButton.setText("Fermer")
        self.closeButton.setGeometry(0,0,0,0)

    def showGameOver(self, gagnant):
        """
        Affiche l'écran de fin de jeu avec le gagnant
        :param: (int) gagnant: 1, 2 ou -1 (si égalité)
        :return: None
        """
        self.gameOverScreen.setGeometry(QRect(0,0,800,600))
        self.gameOverScreen.setStyleSheet("QWidget{background-color: rgba(0,0,0,0.50); font-weight: 900; color: white;}")
        self.gameOverText.setGeometry(0,0,800,600)
        self.gameOverText.setAlignment(Qt.AlignCenter)
        self.gameOverText.setText("Game Over \n" + ("Gagnant: Joueur " + str(gagnant)) if gagnant == 1 or gagnant == 2 else "Égalité!")
        self.closeButton.setGeometry(300, 350, 200, 40)

    def closeGameOver(self):
        """
        Cache l'écran de fin de jeu
        :return: None
        """
        self.gameOverScreen.setGeometry(QRect(0,0,0,0))
        self.gameOverText.setGeometry(0,0,0,0)
        self.closeButton.setGeometry(0,0,0,0)

    def update(self, grid, decal, last_move, player, ended = False):
        """
        Met à jour la position des lignes, les couleurs des cases et le statut des bouttons.
        :param: (matrice 4x4) grid: Plateau de jeu
        :param: (liste len 4) decal: Vecteur de décalage
        :param: (tuple len 2) last_move: Dernier coup (format: (y, x))
        :param: (int) player: Le joueur actuel
        :param: (bool) ended: True si la partie est terminée, False sinon
        :return: None
        """
        lines = (self.line0, self.line1, self.line2, self.line3)
        cells = ((self.cell0, self.cell1, self.cell2, self.cell3), 
                (self.cell4, self.cell5, self.cell6, self.cell7), 
                (self.cell8, self.cell9, self.cell10, self.cell11), 
                (self.cell12, self.cell13, self.cell14, self.cell15))
        leftButtons = (self.left0, self.left1, self.left2, self.left3)
        rightButtons = (self.right0, self.right1, self.right2, self.right3)

        if ended:
            # Déctiver tout les bouttons si la partie est finie
            for button in leftButtons + rightButtons:
                button.setEnabled(False)

            for i in range(4):
                for j in range(4):
                    cells[i][j].setEnabled(False) 
        else:
            # Activer tout les autres
            for button in leftButtons + rightButtons:
                button.setEnabled(True)

            for i in range(4):
                for j in range(4):
                    cells[i][j].setEnabled(True)

            #decalage
            for i in range(4):
                lines[i].setGeometry(QRect(70*decal[i] + 210, 75*i , 280, 70))

                # Desactiver le decalage si decalé de 3 cases ou si dernier coup
                if decal[i] == 3 or last_move == (i, -1):
                    rightButtons[i].setEnabled(False)
                if decal[i] == -3 or last_move == (i, -2):
                    leftButtons[i].setEnabled(False)


            #couleur des cases
            for i in range(4):
                for j in range(4):
                    colour = 'yellow' if grid[i][j] == 1 else 'red' if grid[i][j] == 2 else 'darkblue'
                    cells[i][j].setStyleSheet("QWidget{background-color:" + colour + "}")

                    # Désactiver le dernier coup et les cases du joueur
                    if grid[i][j] == player or grid[i][j] == last_move:
                        cells[i][j].setEnabled(False)
