from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.graphics.instructions import Canvas
from kivy.graphics import Rectangle
from kivy.uix.slider import Slider
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import StringProperty,NumericProperty,ListProperty,BooleanProperty
from kivy.clock import Clock
import json
import os
from kivy.metrics import dp

class Game(Screen):
    def __init__(self,save,Runner):
        super().__init__()
        self.UIX = Game_UI()
        self.Save = save
        self.Runner = Runner
    pass

class Game_PauseMenu(Widget):
    pass

class Game_UI(FloatLayout):
    def __init__(self):
        super().__init__()
        self.All_ActionButton = {}
        self.All_Gauges = {}
        self.All_ToUIButton = {}
        self.All_QuickSlots = {}
    
    def add_smth(self,definer,identifier,smth):
        match(definer):
            case "ACTB":
                self.All_ActionButton[identifier] = smth
            case "Gauge":
                self.All_Gauges[identifier] = smth
            case "TUIB":
                self.All_ToUIButton[identifier] = smth
            case "QS":
                self.All_QuickSlots[identifier] = smth
    pass

class Game_Quickslot(Button):
    invslot = NumericProperty(0)  

class Game_action_button(Button):
    icon = StringProperty("")
    callback =() 

class Game_toUI_Button(Button):
    icon = StringProperty("")
    toward = StringProperty("")        

class Game_Gauge(Widget):      # 4 of them health,food,mana,exp
    value = NumericProperty(0)
    max = NumericProperty(0)
    Do_Show = BooleanProperty(False)
    color = ListProperty([])

class Game_Runner(FloatLayout):
    pass
    
class Game_Map(Canvas):
    NodeArray = NewNodeArray(10,10)
    pass

class Game_Tile(Rectangle):
    icon =StringProperty("")

class NewNodeArray:
    def __init__(length,width):
        super().__init__()
        pass
    pass