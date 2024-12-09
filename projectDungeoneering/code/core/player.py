from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivy.graphics import Rectangle
from kivy.properties import NumericProperty
from kivy.uix.floatlayout import FloatLayout

class Player:
    def __init__(self, name, chosen_class, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.myclass = chosen_class
        self.hp = 10
        self.mana = 10
        self.size = (dp(40), dp(40))  # Taille de l'icône du joueur
        self.char = Widget(size=self.size)
        self.pos = (0, 0)  # Position initiale en termes de indices de grille (lignes, colonnes)
        self.orient = 0  # Orientation du joueur

    def movement(self, code, grid):
        y, x = self.pos

        directions = [
            (-1, -1), (-1, 0), (-1, 1),  # Diagonale haut-gauche, haut, haut-droite
            (0, -1), (0, 1),             # Gauche, droite
            (1, -1), (1, 0), (1, 1)      # Diagonale bas-gauche, bas, bas-droite
        ]
        dx, dy = directions[code]
        ny, nx = y + dy, x + dx
        if grid[ny][nx] == 1:
            self.pos = (ny, nx)  # Mettre à jour la position du joueur
        else:
            return False

    def set_char(self):
        self.char.canvas.clear()
        canva = self.char.canvas
        with canva:
            if self.myclass == "mag":
                Rectangle(pos=self.pos, size=self.size, source="../../assets/sheets/player1.png", color=(0, 0, 0, 0))

    def spawn(self, grid):
        # Trouver la position de départ dans la grille (en supposant que la valeur 2 indique le spawn)
        spawn_position = [(index, row.index(2)) for index, row in enumerate(grid) if 2 in row]
        if spawn_position:
            self.pos = dp(40*spawn_position[0][1]),dp(40*(len(grid)-spawn_position[0][0]-1))  # Position du joueur dans la grille
        self.setpos()  # Mettre à jour la position de l'objet `char`

    def setpos(self):
        # Convertir les coordonnées de la grille en coordonnées d'écran
        row, col = self.pos
        print(row,col)
        self.char.pos = (row,col)  
    
    def newpos(self,position):
        self.pos = position
        self.setpos() 
