from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.uix.scrollview import ScrollView
from kivy.uix.slider import Slider
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import StringProperty,BooleanProperty
from kivy.clock import Clock
import json
import os
from kivy.metrics import dp
#import game
lang_path = "../interface/"
DSH = False
DIH = False
with open('projectDungeoneering/config/text_content.json',encoding='utf-8') as jsonfile:
    full_textcontent=json.load(jsonfile)
actual_lang = "en"
formerlang="en"

for i in full_textcontent:
    if(i == actual_lang):
        textcontent=full_textcontent[i]
class Game(Screen):
    pass
class Menu(Screen):
    lang = StringProperty()
    chg = StringProperty()
    play = StringProperty()
    set = StringProperty()
    badge = StringProperty()
    cred = StringProperty()
    quit = StringProperty()
    def on_enter(self):
        super(Menu, self).__init__()
        self.lang = textcontent["Menu_Content"]["lang"]
        self.chg = textcontent["Menu_Content"]["chg"]
        self.play = textcontent["Menu_Content"]["pl"]
        self.set = textcontent["Menu_Content"]["set"]
        self.badge = textcontent["Menu_Content"]["badges"]
        self.cred = textcontent["Menu_Content"]["credit"]
        self.quit = textcontent["Menu_Content"]["quit"]


class Options(Screen):
    DIH_val=BooleanProperty(DIH)
    DSH_val=BooleanProperty(DSH)
    (gamma,icon,volume,music,DSH_,DIH_) = (StringProperty(textcontent["Options_content"]["gamma"]),StringProperty(textcontent["Options_content"]["gamma"]),StringProperty(textcontent["Options_content"]["gamma"]),StringProperty(textcontent["Options_content"]["gamma"]),StringProperty(textcontent["Options_content"]["DIH"]),StringProperty(textcontent["Options_content"]["DSH"]))
    menu = StringProperty(textcontent["mainmenu"])
    def on_enter(self):
        global DIH,DSH
        self.DIH_val=DIH
        self.DSH_val=DSH
        self.menu = textcontent["mainmenu"]
        self.gamma = textcontent["Options_content"]["gamma"]
        self.icon = textcontent["Options_content"]["icon"]
        self.volume = textcontent["Options_content"]["volume"]
        self.music = textcontent["Options_content"]["music"]
        self.DIH_ = textcontent["Options_content"]["DIH"]+" : "+str(self.DIH_val)
        self.DSH_ = textcontent["Options_content"]["DSH"]+" : "+str(self.DSH_val)

        self.ids.DIH_but.bind(on_release=noDIH)
        self.ids.DSH_but.bind(on_release=noDSH)


    def noDSH(instance,self):
        global DSH
        DSH= not DSH
        self.DSH_ = textcontent["Options_content"]["DSH"]+" : "+str(self.DSH)

    def noDIH(instance,self):
        global DIH
        DIH = not DIH
        self.DIH_ = textcontent["Options_content"]["DIH"]+" : "+str(self.DIH)


class Credits(Screen):
    pass

class Record(Screen):
    pass

class Changelog(Screen):
    pass

class Lang(Screen):  
    savestate=0 
    mainmenu = StringProperty(textcontent["mainmenu"])
    def on_enter(self):
        self.mainmenu = textcontent["mainmenu"]
        if self.savestate == 0:
            for i in (language):
                button = Button(text=i,valign="center",size_hint_max=(1000, dp(40)), size_hint=(1, 1))
                button.bind(on_release=switch_lang)
                self.ids.scroll_lang.add_widget(button)
        self.savestate+=1
    


class FullApp(ScreenManager):
    pass

    


def noDSH(instance):
    global DSH 
    DSH = not DSH

def noDIH(instance):
    global DIH
    DIH= not DIH



language = ["en","fr"]
settings = {"gamma":Slider(min=0, max=100, value=0,step=1),
            "icon size":Slider(min=1, max=4, value=1,step = 1),
            "volume":Slider(min=0, max=100, value=0,step=1),
            "music":Slider(min=0, max=100, value=0,step=1),
            "DSH":Button(text=(textcontent["Options_content"]["DSH"]+" : "+str(DSH)),valign="center",size_hint_max=(1000, dp(40)), size_hint=(1, 1)),
            "DIH":Button(text=(textcontent["Options_content"]["DIH"]+" : "+str(DIH)),valign="center",size_hint_max=(1000, dp(40)), size_hint=(1, 1))}

kv = Builder.load_file(lang_path+"menu/menu.kv")

def switch_lang(instance):
    global actual_lang
    global textcontent
    global full_textcontent
    global kv

    #App.get_running_app().stop()
    actual_lang=instance.text
    for i in full_textcontent:
        if(i == actual_lang):
            textcontent=full_textcontent[i]
    print(textcontent)
    #return Myapp().run()

def OnSliderValueChange(instance,value):
    instance.parent.children[0].text=str(int(value))

class Myapp(App):
    def build(self):
        return kv
    
if __name__=='__main__':
    Myapp().run()