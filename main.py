from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup

color_digit = {
    "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
    "green": 5, "blue": 6, "violet": 7, "gray": 8, "white": 9
}
color_multiplier = {
    "silver": 0.01, "gold": 0.1, "black": 1, "brown": 10, "red": 100,
    "orange": 1_000, "yellow": 10_000, "green": 100_000,
    "blue": 1_000_000, "violet": 10_000_000,
    "gray": 100_000_000, "white": 1_000_000_000
}
color_tolerance = {
    "silver": "±10%", "gold": "±5%", "brown": "±1%", "red": "±2%",
    "green": "±0.5%", "blue": "±0.25%", "violet": "±0.1%", "gray": "±0.05%"
}

class ResistorApp(App):
    def build(self):
        main = BoxLayout(orientation='vertical', padding=20, spacing=10)
        main.add_widget(Label(text='Select Resistor Type', font_size=22))
        btn4 = Button(text='4‑Band Resistor', size_hint_y=None, height=50)
        btn5 = Button(text='5‑Band Resistor', size_hint_y=None, height=50)
        btn4.bind(on_release=lambda _: self.open_calculator(4))
        btn5.bind(on_release=lambda _: self.open_calculator(5))
        main.add_widget(btn4)
        main.add_widget(btn5)
        return main

    def open_calculator(self, bands):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=5)
        spinners = []
        layout.add_widget(Label(text=f"Select {bands}‑Band Colors", font_size=20))
        for _ in range(bands - 2):
            spinner = Spinner(text='Select', values=list(color_digit.keys()))
            layout.add_widget(spinner)
            spinners.append(spinner)
        spinner_mul = Spinner(text='Select', values=list(color_multiplier.keys()))
        spinner_tol = Spinner(text='Select', values=list(color_tolerance.keys()))
        layout.add_widget(spinner_mul); spinners.append(spinner_mul)
        layout.add_widget(spinner_tol); spinners.append(spinner_tol)
        result_label = Label(text='', font_size=18)
        layout.add_widget(result_label)

        def calculate(_):
            try:
                if bands == 4:
                    d1 = color_digit[spinners[0].text]; d2 = color_digit[spinners[1].text]
                    mul = color_multiplier[spinners[2].text]; tol = color_tolerance[spinners[3].text]
                    value = (d1 * 10 + d2) * mul
                else:
                    d1 = color_digit[spinners[0].text]; d2 = color_digit[spinners[1].text]
                    d3 = color_digit[spinners[2].text]; mul = color_multiplier[spinners[3].text]
                    tol = color_tolerance[spinners[4].text]
                    value = (d1 * 100 + d2 * 10 + d3) * mul
                unit = "Ω"
                if value >= 1_000_000:
                    value /= 1_000_000; unit = "MΩ"
                elif value >= 1_000:
                    value /= 1_000; unit = "kΩ"
                result_label.text = f"Resistance: {value} {unit} {tol}"
            except:
                result_label.text = "Select all bands!"

        btn_calc = Button(text="Calculate", size_hint_y=None, height=40)
        btn_calc.bind(on_release=calculate)
        layout.add_widget(btn_calc)

        popup = Popup(title=f"{bands}‑Band Calculator", content=layout, size_hint=(0.9, 0.9))
        popup.open()

if __name__ == '__main__':
    ResistorApp().run()
