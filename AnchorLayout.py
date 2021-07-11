from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button


# layout
#     - layouts are containers
#     - help to organize and arrange widgets to our need
#     - types
#         -Anchor Layout
#         -Float Layout
#         -Grid Layout
#         -Page Layout


class DemoApp(App):

    # build method execute first and load all widgets on window
    def build(self):
        l = AnchorLayout()
        l.anchor_x ="left"
        l.anchor_y = "top"
        b = Button()
        b.text = "Anchor layout demo"
        b.size_hint = (0.2, 0.2)
        b.backgroud_color = (0.0, 25.86, 1.0,0)
        # font color
        b.color = (0, 0, 0, 1)
        l.add_widget(b)
        return l


demo = DemoApp()
demo.run()
