from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout

Window.size = (	375, 700)

class MenuScreen(Screen):
    pass
class SplashScreen(Screen):
    pass
class ProfileScreen(Screen):
    pass
class SignScreen(Screen):
    pass
class SearchScreen(Screen):
    pass
class GoodsScreen(Screen):
    pass
class ServiceScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(SplashScreen(name='splash'))
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(MenuScreen(name='login'))
sm.add_widget(SignScreen(name='sign'))
sm.add_widget(SearchScreen(name='search'))
sm.add_widget(GoodsScreen(name='goods'))
sm.add_widget(ServiceScreen(name='service'))

class Finder(MDApp):
     def build(self):
         global sm
         sm = Builder.load_file('Main.kv')
         sm = Builder.load_file('splash.kv')
         sm = Builder.load_file('signin.kv')
         sm = Builder.load_file('search.kv')
         sm = Builder.load_file('goods.kv')
         sm = Builder.load_file('service.kv')
         
         return sm
     
     def on_start(self):
         Clock.schedule_once(self.menu,2)
    
     def menu (self, *args):
         sm.current = "menu"
     
if __name__ == "__main__":
    Finder().run()

#HEEEERRRRRRRRRRRRRRRREEEEE
