import pyglet

from game import load, resources

# Load game window.
game_window = pyglet.window.Window()

# Create game labels.
score_label = pyglet.text.Label(text='Score: 0', x=10, y=575)
level_label = pyglet.text.Label(text='An Asteroids Game!',
                                x=400, y=575, anchor_x='center')


# Bind our on_draw event to the game window.
@game_window.event
def on_draw():
    game_window.clear()

    level_label.draw()
    score_label.draw()

if __name__ == '__main__':
    pyglet.app.run()