from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934

class RootWidget(BoxLayout):
    default_miles = StringProperty('0')

class ConvertMilesKmApp(App):
    km_text = StringProperty('0.0')

    def build(self):
        self.root_widget = RootWidget()
        return self.root_widget

    def get_miles_value(self):
        text = self.root_widget.ids.miles_input.text
        try:
            return float(text)
        except ValueError:
            return 0.0

    def calculate_km(self):
        miles = self.get_miles_value()
        km = miles * MILES_TO_KM
        self.km_text = f"{km:.3f}"

    def handle_increment(self, delta):
        try:
            value = float(self.root_widget.ids.miles_input.text)
        except ValueError:
            value = 0.0
        new_value = value + delta
        self.root_widget.ids.miles_input.text = str(int(new_value)) if new_value.is_integer() else str(new_value)
        self.calculate_km()

if __name__ == '__main__':
    ConvertMilesKmApp().run()