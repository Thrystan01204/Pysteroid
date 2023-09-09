import socket
import pyglet
from pyglet.window import key


w, h = 640, 480
config = pyglet.gl.Config(
    sample_buffers=1, samples=8, depth_size=16, double_buffer=True
)
window = pyglet.window.Window(config=config, width=w, height=h)
keys = key.KeyStateHandler()
window.push_handlers(keys)

player = pyglet.shapes.Circle(w / 2, h / 2, 16, color=(255, 0, 0))
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 65432))


@window.event
def on_draw():
    window.clear()
    player.draw()


def update(dt):
    speed = 256
    player.y += speed * dt * (keys[key.Z] - keys[key.S])
    player.x += speed * dt * (keys[key.D] - keys[key.Q])


def send(dt):
    txt = f"{player.x},{player.y}"
    conn.sendall(txt.encode())


pyglet.clock.schedule_interval(update, 1.0 / 60.0)
pyglet.clock.schedule_interval(send, 1.0 / 4.0)

pyglet.app.run()

conn.close()
