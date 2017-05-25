#!/usr/bin/env python
# -*- coding: utf-8 -*-
import kivy
from kivy.app import App
from kivy.app import Widget
from datetime import date
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.base import runTouchApp
from kivy.core.window import Window;
from kivy.uix.bubble import Bubble, BubbleButton


hoje = date.today()
amanha = hoje.day
ontem = hoje.month
semana = hoje.weekday
dias = (0, 1, 2, 3, 4, 5, 6)
feira = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
x = dias[hoje.weekday()]
n = NumericProperty(35)
class PrimeiroScreen(Screen):
	def __init__(self, **kwargs):
		self.name = 'um'
		super(Screen,self).__init__(**kwargs)

	def dia(self):
		
		if x == 0:
			App.get_running_app().root.current = 'seg'
		elif x == 1:
			App.get_running_app().root.current = 'ter'
		elif x == 2:
			App.get_running_app().root.current = 'qua'
		elif x == 3:
			App.get_running_app().root.current = 'qui'
		elif x == 4:
			App.get_running_app().root.current = 'sex'
		elif x == 5:
			App.get_running_app().root.current = 'sab'
		elif x == 6:
			App.get_running_app().root.current = 'dom'
	

class SegundoScreen(Screen):
	def __init__(self, **kwargs):
		self.name = 'dois'
		super(Screen,self).__init__(**kwargs)

	def mucarela(self, *args):
		screen4 = self.manager.get_screen('carrinho')
		screen4.btn1 = BubbleButton(text="Muçarela", font_size='20dp', size_hint=(1,None), background_normal='1.png', background_down='2.png')
		screen4.lb1 = Label(text="25,00", font_size='20dp', size_hint=(1,None))
		screen4.ids.lb5.value += 25
		screen4.ids.grid.add_widget(screen4.btn1)
		screen4.ids.grid.add_widget(screen4.lb1)
		print(n)
	
	def catupiry(self, *args):
		screen4 = self.manager.get_screen('carrinho')
		screen4.btn2 = BubbleButton(text="Catupiry",font_size='20dp', size_hint=(1,None), background_normal='2.png', background_down='1.png')
		screen4.lb2 = Label(text="25,00",font_size='20dp', size_hint=(1,None))
		screen4.ids.lb5.value += 25
		screen4.ids.grid.add_widget(screen4.btn2)
		screen4.ids.grid.add_widget(screen4.lb2)
	
	def peru(self, *args):
		screen4 = self.manager.get_screen('carrinho')
		screen4.btn2 = BubbleButton(text="Peito de peru",font_size='20dp', size_hint=(1,None), background_normal='1.png', background_down='2.png')
		screen4.lb2 = Label(text="95,00",font_size='20dp', size_hint=(1,None))
		screen4.ids.lb5.value += 35
		screen4.ids.grid.add_widget(screen4.btn2)
		screen4.ids.grid.add_widget(screen4.lb2)
	
	def portuguesa(self, *args):
		screen4 = self.manager.get_screen('carrinho')
		screen4.btn2 = BubbleButton(text="Portuguesa",font_size='20dp', size_hint=(1,None), background_normal='2.png', background_down='1.png')
		screen4.lb2 = Label(text="17,00",font_size='20dp', size_hint=(1,None))
		screen4.ids.lb5.value += 27
		screen4.ids.grid.add_widget(screen4.btn2)
		screen4.ids.grid.add_widget(screen4.lb2)
		
	def toscana(self, *args):
		screen4 = self.manager.get_screen('carrinho')
		screen4.btn2 = BubbleButton(text="Toscana",font_size='20dp', size_hint=(1,None), background_normal='1.png', background_down='2.png')
		screen4.lb2 = Label(text="5,50",font_size='20dp', size_hint=(1,None))
		screen4.ids.lb5.value += 35
		screen4.ids.grid.add_widget(screen4.btn2)
		screen4.ids.grid.add_widget(screen4.lb2)
class TerceiroScreen(Screen):
	def __init__(self, **kwargs):
		self.name = 'carrinho'
		super(Screen,self).__init__(**kwargs)

class SegundaScreen(Screen):
	def __init__(self, **kwargs):
		self.name = 'seg'
		super(Screen,self).__init__(**kwargs)

class TercaScreen(Screen):
	def __init__(self, **kwargs):
		self.name = 'ter'
		super(Screen,self).__init__(**kwargs)

class QuartaScreen(Screen):
	def __init__(self, **kwargs):
		self.name = 'qua'
		super(Screen,self).__init__(**kwargs)

class QuintaScreen(Screen):
	def __init__(self, **kwargs):
		self.name = 'qui'
		super(Screen,self).__init__(**kwargs)

class SextaScreen(Screen):
	def __init__(self, **kwargs):
		self.name = 'sex'
		super(Screen,self).__init__(**kwargs)
	
	def promo2(self, *args):
		screen4 = self.manager.get_screen('carrinho')
		screen4.btnp1 = Button(text="Muçarela(+Refri)", font_size='20dp', size_hint=(1,None), background_normal='1.png', background_down='2.png')
		screen4.lbp1 = Label(text="20,00", font_size='20dp', size_hint=(1,None))
		screen4.ids.lb5.value += 20
		screen4.ids.grid.add_widget(screen4.btnp1)
		screen4.ids.grid.add_widget(screen4.lbp1)
	
	def promo1(self, *args):
		screen4 = self.manager.get_screen('carrinho')
		screen4.btn2 = BubbleButton(text="Catupiry(+Refri)",font_size='20dp', size_hint=(1,None), background_normal='2.png', background_down='1.png')
		screen4.lb2 = Label(text="25,00",font_size='20dp', size_hint=(1,None))
		screen4.ids.lb5.value += 20
		screen4.ids.grid.add_widget(screen4.btn2)
		screen4.ids.grid.add_widget(screen4.lb2)
	
class SabadoScreen(Screen):
	def __init__(self, **kwargs):
		self.name = 'sab'
		super(Screen,self).__init__(**kwargs)

class DomingoScreen(Screen):
	def __init__(self, **kwargs):
		self.name = 'dom'
		super(Screen,self).__init__(**kwargs)
				
class MyLabel1(Label):
	value = NumericProperty(0)
	

class RootScreen(ScreenManager):
    pass
    
class pizzoideApp(App):
	title = 'Pizzoide!'
	def on_pause(self):
		return True
		
	def on_resume(self):
	   
	   pass
      
	def build(self):
		return RootScreen()
if __name__ == '__main__':
    appVar = pizzoideApp()
    pizzoideApp().run()
