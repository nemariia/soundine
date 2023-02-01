from kivymd.app import MDApp
from kivy.lang import Builder
import sounddevice as sd
import numpy as np
import math

class SoundButton():
	pass

class MenuApp(MDApp):
	def __init__(self, **kw):
		super().__init__(**kw)
		# loading layouts
		self.screen = Builder.load_file("layout\\main.kv")
		sd.default.samplerate = 44100
		signal = self.sinewawe(150, 3)
		sd.play(signal)
		# get a output stream where we can play samples
		self.stream = sd.Stream()


	def playback(signal):
		sd.play(signal)

	def sinewawe(self, f, t, fs = 44100):
		time = np.arange(t * fs) / fs
		signal = np.sin(2 * np.pi * f * time)
		return signal
		

	def build(self):
		self.theme_cls.primary_palette = "LightGreen"
		return self.screen
    

MenuApp().run()
