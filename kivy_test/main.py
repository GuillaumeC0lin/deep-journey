import kivy
from kivy.app import App
from kivy.uix.slider import Slider

slider =Slider(min=0, max=100, value=50)
class SliderApp(App):
    def build(self):
        slider.bind(value=OnSliderValueChange)
        return slider

def OnSliderValueChange(instance,value):
    print(slider.value)

if __name__ == '__main__':
    SliderApp().run()