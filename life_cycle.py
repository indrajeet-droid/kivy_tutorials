from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout


# life cycle of an App
# below are the event handler which called automatically(no need to handle or call below events)
class DemoApp(App):

    # build method execute first and load all widgets on window
    def build(self):
        f = FloatLayout()
        s = Scatter()
        l = Label(text="Hello !", font_size=150)
        f.add_widget(s)
        s.add_widget(l)
        return f

    def on_start(self):
        pass

    def on_stop(self):
        pass

    def on_resume(self):
        pass

    def on_pause(self):
        return True


demo = DemoApp()
# run method
#    -prepare the app for run
#    -load config file if any
#    -load window
#    -run the app

demo.run()
