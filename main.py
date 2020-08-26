import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.textinput import TextInput
# from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
# from kivy.graphics import Rectangle
# from kivy.graphics import Color
# from kivy.graphics import Line
# from kivy.lang import Builder
# from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup

# class MainWindow(Screen):
#     pass
# class SecondWindow(Screen):
#     pass
# class WindowManager(ScreenManager):
#     pass

# kv = Builder.load_file("my.kv")

# class MyGrid(Widget):
    # name = ObjectProperty(None)
    # email = ObjectProperty(None)

    # def btn(self):
    #     print("Name:", self.name.text, "Email:", self.email.text)
    #     self.name.text = ""
    #     self.email.text = ""
    # def __init__(self, **kwargs):
    #     super(MyGrid, self).__init__(**kwargs)
    #     self.cols = 1

    #     self.inside = GridLayout()
    #     self.inside.cols = 2

    #     self.inside.add_widget(Label(text='First Name: '))
    #     self.name = TextInput(multiline=False)
    #     self.inside.add_widget(self.name)

    #     self.inside.add_widget(Label(text='Last Name: '))
    #     self.lastName = TextInput(multiline=False)
    #     self.inside.add_widget(self.lastName)

    #     self.inside.add_widget(Label(text='Email: '))
    #     self.email = TextInput(multiline=False)
    #     self.inside.add_widget(self.email)

    #     self.add_widget(self.inside)

    #     self.submit = Button(text='Submit', font_size=40)
    #     self.submit.bind(on_press=self.pressed)
    #     self.add_widget(self.submit)

    # def pressed(self, instance):
    #     name = self.name.text
    #     last = self.lastName.text
    #     email = self.email.text 

    #     print("Name: ", name, " Last Name: ", last, " Email: ", email)
    #     self.name.text = ""
    #     self.lastName.text = ""
    #     self.email.text = ""

# class Touch(Widget):
#     def __init__(self, **kwargs):
#         super(Touch, self).__init__(**kwargs)

#         with self.canvas:
#             Color(1, 0, 5, .5, mode='rgba')
#             Line(points=(20, 30, 400, 500, 60, 30))
#             Color(1, 0, 0, .5, mode='rgba')
#             self.rect = Rectangle(pos=(0,0), size=(50, 50))
            # Color(1, 1, 0, .5, mode='rgba')
            # self.rect = Rectangle(pos=(200,300), size=(150, 50))



    # btn = ObjectProperty(None)
    # def on_touch_down(self, touch):
    #     self.rect.pos = touch.pos
    #     print("Mouse Down", touch)
    #     # self.btn.opacity = 0.5
    # def on_touch_move(self, touch):
    #     self.rect.pos = touch.pos
    #     print("Mouse Move", touch)
    # def on_touch_up(self, touch):
    #     self.btn.opacity = 1

class Widgets(Widget):
    def btn(self):
        show_popup()

class P(FloatLayout):
    pass

class MyApp (App):
    def build(self):
        # return MyGrid()
        # return FloatLayout()
        # return kv
        return Widgets()

def show_popup():
    show = P()

    popupWindow = Popup(title="Popup Window", content=show, size_hint=(None,None), size=(400,400))
    
    popupWindow.open()

if __name__ == "__main__":
    MyApp().run()