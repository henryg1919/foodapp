import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import random


class FoodApp(App):
    def build(self):
        return MyGrid()


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2

        self.label = Label(text="Food")
        self.button = Button(text="submit", font_size=20, pos=(200, 400), size_hint=(.8, .8))
        self.button.bind(on_press=self.pressed)

        self.add_widget(self.label)
        self.add_widget(self.button)

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.label1 = Label(text="Restaurant")
        self.inside.text = TextInput(multiline=False)
        self.inside.B_Add = Button(text="Add", font_size=20, pos=(200, 400), size_hint=(2, 2))
        self.inside.B_Add.bind(on_press=self.add)
        self.inside.B_Display = Button(text="Display", font_size=20, pos=(200, 400), size_hint=(2, 2))
        self.inside.B_Display.bind(on_press=self.display)

        self.add_widget(self.inside.text)
        self.add_widget(self.inside.label1)
        self.add_widget(self.inside.B_Add)
        self.add_widget(self.inside.B_Display)
        self.add_widget(self.inside)

        self.food = ["Olive Garden", "Mods Pizza", "Jason's Deli", "Faddis"]
        self.add_food = [""]
        self.r_num = random.randint(0, 3)
        self.random = random.choices(self.add_food)

    def pressed(self, instance):
        self.r_num = random.randint(0, 3)
        self.label.text = self.food[self.r_num]
        print(self.food[self.r_num])

    def add(self, instance):
        content = self.inside.text.text
        self.add_food.append(content)
        self.inside.text.text = ""
        print(self.add_food)

    def display(self, instance):
        self.r_num = random.randint(0, 3)
        self.inside.label1.text = random.choice(self.add_food)
        print(self.food[self.r_num])


if __name__ == "__main__":
    FoodApp().run()