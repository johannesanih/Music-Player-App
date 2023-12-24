import pygame
from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.screen import Screen
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import MDList, OneLineIconListItem
from kivy.lang import Builder

pygame.init()

class AudioPlayerLayout(Screen, MDFloatLayout):
    pass

class ContentLayout(Screen, MDFloatLayout):
    pass


sm = ScreenManager()

sm.add_widget(AudioPlayerLayout(name="audio screen"))
sm.add_widget(ContentLayout(name="content screen"))

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        screen = Builder.load_file('new.kv')
        return screen

    
        

if __name__ == "__main__":
    MainApp().run()