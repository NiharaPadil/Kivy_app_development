from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class Touch(Widget):
    btn = ObjectProperty(None)

    def on_touch_down(self, touch):
        print("MOUSE DOWN", touch)
        self.btn.opacity = 1

    def on_touch_move(self, touch):
        print("MOUSE MOVE", touch)

    def on_touch_up(self, touch):
        print("MOUSE UP", touch)
        self.btn.opacity = 0.5


class mouseApp(App):
    def build(self):
        return Touch()


if __name__ == "__main__":
    mouseApp().run()
