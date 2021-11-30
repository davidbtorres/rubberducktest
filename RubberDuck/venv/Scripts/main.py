from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import NumericProperty
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
import time

class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    breakTimeValue = NumericProperty(10)

    pass

class WindowManager(ScreenManager):
    pass

class MyApp(App):
    def build(self):
        self.playSound_quack()
        self.title = 'Rubber Duck'
        Window.clearcolor = (5/255, 45/255, 60/255, 1)    # app background color
        Window.size = (500, 400)                          # size of entire app window
        return Builder.load_file("./../Kivy/my.kv")

    # alarm sound effect
    def playSound_alarm(self):
        sound = SoundLoader.load("../Assets/alarmclock_sound.wav")
        if sound:
            sound.play()

    # quack sound effect
    def playSound_quack(self):
        sound = SoundLoader.load("../Assets/duckquack_sound.wav")
        if sound:
            sound.play()

    # behavior for 'break' action
    def timedBreak(self, time):
        #self.greeting.text = "See you in 30 minutes!"
        App.get_running_app().root_window.minimize()
        Clock.schedule_once(self.breakOver, time) # time reduced to seconds for testing

    # restoring app on break finish
    def breakOver(self, instance):
        self.playSound_quack()
        self.playSound_alarm()
        App.get_running_app().root_window.restore()
        #self.greeting.text = "Welcome back!"

    # 'dismiss' handling
    def checkBackLater(self):
        Clock.schedule_once(self.checkIn, 5) # time set to 5 seconds for testing and demoing
        App.get_running_app().root_window.minimize()

    # 'check in' handling
    def checkIn(self, instance):
        self.playSound_quack()
        App.get_running_app().root_window.restore()
        #self.greeting.text = "Quack!\n\nChecking in!\nYou Have Been Working For a While Now"

if __name__ == "__main__":
    MyApp().run()