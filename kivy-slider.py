from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle

class ColorMixer(BoxLayout):

    def __init__(self, **kwargs):
        super(ColorMixer, self).__init__(orientation='vertical', **kwargs)

        # Vytvoření sliderů
        self.sliders = [Slider(min=0, max=255, value=125) for _ in range(3)]
        for slider in self.sliders:
            slider.bind(value=self.on_color_change)
            self.add_widget(slider)

        # Vytvoření widgetu pro zobrazení barvy
        self.color_display = Widget()
        self.add_widget(self.color_display)

    def on_color_change(self, instance, value):
        self.color_display.canvas.before.clear()
        with self.color_display.canvas.before:
            Color(self.sliders[0].value/255.0, self.sliders[1].value/255.0, self.sliders[2].value/255.0, 1)
            self.rect = Rectangle(pos=self.color_display.pos, size=self.color_display.size)

class ColorMixerApp(App):
    def build(self):
        return ColorMixer()

if __name__ == '__main__':
    ColorMixerApp().run()
