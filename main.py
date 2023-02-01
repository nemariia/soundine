from kivymd.app import MDApp
from kivy.lang import Builder
import Nsound as ns

class MenuApp(MDApp):
	def __init__(self, **kw):
		super().__init__(**kw)
		# loading layouts
		self.screen = Builder.load_file("layout\\main.kv")
		# setting an audiostreem
		a = ns.AudioStream(44100.0)
		# simple sine sound
		s = ns.Sine(44100.0)
		a << s.generate(1.0, 50.0)
		# playback
		a >> ns.AudioPlayback(a.getSampleRate(), a.getNChannels(), 16)
	def build(self):
		self.theme_cls.primary_palette = "LightGreen"
		return self.screen
    

MenuApp().run()