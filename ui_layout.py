from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.image import Image

# Ui Elements
#
# -customisable at every level
# -widgets take actions as input and provide appropriate response
# -kivy provides support for various type of widgets
#     -Lable widgets
#     -TextInput widgets
#     -PopUp widgets
#     -Button widgets
#     -Image widgets


class Kivy_UI(GridLayout):
    def __init__(self , **kwags):
        super().__init__(**kwags)
        self.cols = 1
        self.rows = 4

        self.img = Image(
            source="robot_PNG3.png"
        )

        self.lab = Label(
            text = "Enter your name"
        )

        self.txt = TextInput(
            text="",
            font_size = 40
        )
# button widgets has callback function. callback function does, when certain action perform on button that callback
# method get triggered
        self.btn = Button(
            text="Submit",

        )
        self.btn.bind(on_press=self.call_back)

        self.pop = Popup(
            title="pop-up window",
            size_hint = (None,None),
            size= (400,400),
            content=Label(
                text=""
            )
        )
        self.add_widget(self.img)
        self.add_widget(self.lab)
        self.add_widget(self.txt)
        self.add_widget(self.btn)

    def call_back(self,elem):
        self.pop.content.text= self.txt.text
        self.pop.open()


class DemoApp(App):
    # build method execute first and load all widgets on window
    def build(self):
        return Kivy_UI()


demo = DemoApp()
demo.run()
