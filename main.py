from kivymd.app import MDApp
from kivy.lang import Builder

class MenuApp(MDApp):
	def __init__(self, **kw):
		super().__init__(**kw)
		self.screen = Builder.load_file("layout\\main.kv")
	def build(self):
		self.theme_cls.primary_palette = "LightGreen"
		return self.screen
    

MenuApp().run()