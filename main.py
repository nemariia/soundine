from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
import sounddevice as sd
import numpy as np
import math
from kivy.uix.colorpicker import ColorPicker

class SoundButton():
	pass

class MenuApp(MDApp):
	def __init__(self, **kw):
		super().__init__(**kw)
		# loading layouts
		self.screen = Builder.load_file("layout\\main.kv")
		sd.default.samplerate = 44100
		signal = self.sinewawe(150, 1)

		# get a output stream where we can play samples
		self.stream = sd.Stream()


	def playback(signal):
		sd.play(signal)

	def sinewawe(self, f, t, fs = 44100):
		time = np.arange(t * fs) / fs
		signal = np.sin(2 * np.pi * f * time)
		return signal

	def set_color(self, ev):
		clr_picker = ColorPicker()
		clr_picker.bind(color=self.on_color)
		# get a reference to the whole composit button
		self.btn_clicked = ev.parent.parent
        # set the dialog component
		self.color = MDDialog(
			title="Choose a color",
			type="custom",
			content_cls=MDBoxLayout(
				clr_picker,
				orientation="vertical",
				spacing="12dp",
				size_hint_y=None,
				height="120dp",
                ),
            buttons=[
                MDFlatButton(
                    text="OK",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=lambda x: self.color.dismiss()
                ),
            ],
        )
		self.color.open()
		
	def on_color(self, instance, value):
		self.btn_clicked.md_bg_color = value

	def build(self):
		self.theme_cls.primary_palette = "LightGreen"
		return self.screen
    

MenuApp().run()
