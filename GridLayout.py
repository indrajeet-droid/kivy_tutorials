from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


# layout
# Grid Layout is similar to Box layout where the widgets are placed in a matrix of rows and column
# here we can't explicitly place the widgets in a specific row/column

class Gird_Layout_Demo(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 2
        self.cols = 1

        self.l1 = Label(
            text="please click the button"
        )

        self.add_widget(self.l1)

        self.b1 = Button(
            text="click Me",
            background_color=(0, 24, 67, 1),
            color=(0, 0, 0, 1)
        )

        self.add_widget(self.b1)


class DemoApp(App):

    # build method execute first and load all widgets on window
    def build(self):
        return Gird_Layout_Demo()


demo = DemoApp()
demo.run()
