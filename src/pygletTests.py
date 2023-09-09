import pyglet
from pyglet.window import mouse

window = pyglet.window.Window()

label = pyglet.text.Label(
    "hello, world",
    font_name="Times New Roman",
    font_size=36,
    x=window.width // 2,
    y=window.height // 2,
    anchor_x="center",
    anchor_y="center",
)

image = pyglet.resource.image("assets/fantasyred.jpg")

event_logger = pyglet.window.event.WindowEventLogger()
window.push_handlers(event_logger)


# @window.event
# def on_key_press(symbol, modifiers):
#     print(f"A key was pressed : {chr(symbol)}")


# @window.event
# def on_mouse_press(x, y, button, modifiers):
#     if button == mouse.LEFT:
#         print(f"The left mouse button was pressed at (x,y) = ({x},{y})")


@window.event
def on_draw():
    window.clear()
    image.blit(0, 0)
    label.draw()


pyglet.app.run()
