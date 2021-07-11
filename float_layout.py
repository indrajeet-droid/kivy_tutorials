from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button


# float layout allows us to determine the size and position of the child widgets
# by default, the widgets are placed at the bottom left corner of the window

class Float_layout_Demo(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.b1 = Button(
            text="Button1",
            size_hint=(0.4, 0.4),
            pos_hint={"x": 0.3, "y": 0.3}
        )

        self.add_widget(self.b1)

        self.b2 = Button(
            text = "Button 2",
            size_hint = (0.1,0.2),
            pos_hint={"x":0.8,"y":0.7}
        )

        self.add_widget(self.b2)


class DemoApp(App):
    # build method execute first and load all widgets on window
    def build(self):
        return Float_layout_Demo()


demo = DemoApp()
demo.run()
