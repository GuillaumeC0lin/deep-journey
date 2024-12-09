from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.metrics import dp
from kivy.graphics import Rectangle
from kivy.uix.scatter import Scatter
from kivy.core.window import Window
import json
from kivy.graphics import PushMatrix, PopMatrix, Rotate
from kivy.graphics.transformation import Matrix
from kivy.properties import NumericProperty
from random import randint
from pathfinding.core.grid import Grid
from pathfinding.finder.best_first import BestFirst
from player import Player


# Charger le fichier de configuration JSON pour la carte
true_map = []
matrix = []
a = 0
with open('projectDungeoneering/config/new_testmap.json', encoding='utf-8') as jsonfile:
    matrix = json.load(jsonfile)
for i in matrix["1"]:
    true_map.append([])
    for j in range(len(i)-1):
        true_map[a].append(int(i[j]))
    a += 1

# Classe Cell pour chaque tuile du donjon
class Cell(Widget):
    def __init__(self, type_cellule, pos, **kwargs):
        super().__init__(**kwargs)
        self.type = type_cellule  # Type de la cellule : mur, salle, etc.
        self.size_hint = (None, None)  # Désactiver size_hint pour pouvoir spécifier une taille fixe
        self.size = (dp(40), dp(40))  # Taille fixe de chaque cellule
        self.pos = pos  # Position manuelle définie au moment de la création
        self.update_color_or_texture()

    def update_color_or_texture(self):
        # Liste des textures pour les salles
        source = [
            "../../assets/sheets/floor_tile.png",
            "../../assets/sheets/floor_tile2.png",
            "../../assets/sheets/floor_tile3.png"
        ]

        # Effacer le canvas avant de redessiner
        self.canvas.clear()

        with self.canvas:
            res = 0
            if self.type == 0:  # Mur
                Rectangle(pos=self.pos, size=self.size, source="../../assets/sheets/wall_tile1.png")
            elif self.type == 1:  # Salle
                # Texture aléatoire pour les salles
                src_val = randint(0, 100)
                if(src_val<10):
                    res=2
                if(10<src_val<20):
                    res=0
                if(src_val>20):
                    res=1
                random_texture = source[res]
                random_angle = randint(0, 3) * 90  # Rotation aléatoire (0°, 90°, 180°, 270°)

                # Appliquer la rotation
                PushMatrix()
                Rotate(origin=self.center, angle=random_angle)  # Rotation autour du centre de la cellule
                Rectangle(pos=self.pos, size=self.size, source=random_texture)
                PopMatrix()

# Fonction pour vérifier si une cellule doit être affichée
def should_display_cell(dungeon_map, x, y):
    rows = len(dungeon_map)
    cols = len(dungeon_map[0])

    # Si la cellule elle-même est 1, on l'affiche
    if dungeon_map[y][x] == 1:
        return True

    # Vérifier les voisins (directs et diagonaux)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),  # Diagonale haut-gauche, haut, haut-droite
        (0, -1),           (0, 1),   # Gauche, droite
        (1, -1), (1, 0), (1, 1)     # Diagonale bas-gauche, bas, bas-droite
    ]
    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if 0 <= ny < rows and 0 <= nx < cols:  # Assurez-vous que le voisin est dans les limites
            if dungeon_map[ny][nx] == 1:
                return True

    # Si aucun voisin n'est connecté, ne pas afficher
    return False

# Classe Scatter personnalisé avec gestion du zoom via molette
class CustomScatter(Scatter):
    def on_touch_down(self, *args):
        touch = args[0]
        factor = None
        if touch.button == 'scrolldown':
            if self.scale < self.scale_max:
                factor = 1.2
        elif touch.button == 'scrollup':
            if self.scale > self.scale_min:
                factor = 1 / 1.2
        if factor is not None:
            self.apply_transform(Matrix().scale(factor, factor, factor),
                             anchor=touch.pos)
        else:
            super(CustomScatter,self).on_touch_down(touch)
# Classe principale de l'application DungeonApp
class DungeonApp(App):
    def build(self):
        self.dungeon_map = true_map  # Charge la carte depuis la variable true_map
        return self.create_zoomable_map(self.dungeon_map)

    def create_zoomable_map(self, dungeon_map):
        # Créer un FloatLayout pour positionner les cellules
        layout = FloatLayout(size_hint=(None, None), size=(len(dungeon_map[0]) * dp(40), len(dungeon_map) * dp(40)))

        # Positionner chaque cellule en fonction de son index dans true_map
        for y, row in enumerate(dungeon_map):
            for x, cell_type in enumerate(row):
                if should_display_cell(dungeon_map, x, y):
                    pos_x = x * dp(40)  # Position en X
                    pos_y = (len(dungeon_map) - y - 1) * dp(40)  # Position en Y (inversé pour que (0,0) soit en bas à gauche)
                    cell = Cell(type_cellule=cell_type, pos=(pos_x, pos_y))
                    layout.add_widget(cell)

        # Utiliser CustomScatter pour gérer le zoom avec la molette
        player_layout = self.addPlayer(dungeon_map)
        scatter = CustomScatter(size_hint=(None, None), size=layout.size,scale=1)
        scatter.add_widget(layout)
        scatter.add_widget(player_layout)


        # Rediriger les événements de défilement vers le Scatter
        Window.bind(on_scroll=scatter.on_touch_down)

        return scatter
    
    def addPlayer(self,grid):
        layout = FloatLayout(size_hint=(None, None), size=(len(grid[0]) * dp(40), len(grid) * dp(40)))
        my_play = Player("henry","mag")
        my_play.spawn(grid)
        print(my_play.pos)
        print(my_play.char.pos)
        print(layout.size)
        print(layout.pos)
        my_play.set_char()
        layout.add_widget(my_play.char)
        return layout


if __name__ == "__main__":
    # Redimensionner la fenêtre pour s'assurer qu'il y a assez d'espace pour l'affichage
    Window.size = (800, 800)  # Taille de la fenêtre ajustée pour que la grille soit visible

    DungeonApp().run()
