from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MyBoxLayoutDemoApp(App):
    def build(self):
        return BoxLayout()

    def handle_greet(self):
        print('greet')
        name = self.root.ids.input_name.text
        self.root.ids.output_label.text = f"Hello {name}"

    def handle_clear(self):
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = ''

if __name__ == '__main__':
    MyBoxLayoutDemoApp().run()