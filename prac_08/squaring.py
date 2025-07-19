"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Lindsay Ward, IT@JCU
Started 13/10/2015
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class SquareApp(App):
    def build(self):
        return BoxLayout()

    def handle_calculate(self, number_text):
        try:
            num = float(number_text)
            result = num ** 2
            self.root.ids.output_label.text = f"{result:.2f}"
        except ValueError:
            self.root.ids.output_label.text = "Invalid input"

if __name__ == '__main__':
    SquareApp().run()
