from kivymd.app import MDApp
from kivy.lang import Builder

class SoundButton():
	pass

class MenuApp(MDApp):
	def __init__(self, **kw):
		super().__init__(**kw)
		# loading layouts
		self.screen = Builder.load_file("layout\\main.kv")
	def build(self):
		self.theme_cls.primary_palette = "LightGreen"
		return self.screen
    

MenuApp().run()
