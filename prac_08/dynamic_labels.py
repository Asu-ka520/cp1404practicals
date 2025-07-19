from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    def build(self):

        self.names = ["Alice", "Bob", "Charlie", "Diana", "Eva"]
        root = BoxLayout()

        self.root = root = self.load_kv('dynamic_labels.kv')

        main_box = root.ids.main

        for name in self.names:
            main_box.add_widget(Label(text=name, font_size=28))
        return root

if __name__ == '__main__':
    DynamicLabelsApp().run()