from kivy.app import App
from kivy.uix.button import Button


class MainApp(App):

  def build(self):
    # Creates a button centered on the screen
    return Button(
        text='Hello, Android!',
        font_size=32,
        background_color=(0.1, 0.5, 0.8, 1),
    )


if __name__ == '__main__':
  MainApp().run()