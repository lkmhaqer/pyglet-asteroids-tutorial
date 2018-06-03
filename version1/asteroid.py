import pyglet

from game import load, resources


# Load game window.
game_window = pyglet.window.Window()

# Create game labels.
score_label = pyglet.text.Label(text='Score: 0', x=10, y=575)
level_label = pyglet.text.Label(text='An Asteroids Game!',
                                x=400, y=575, anchor_x='center')

# Draw the player, and asteroids on screen.
player_ship = pyglet.sprite.Sprite(img=resources.player_image, x=400, y=300)
asteroids = load.asteroids(3, player_ship.position)

# Bind our on_draw event to the game window.
@game_window.event
def on_draw():
    game_window.clear()

    player_ship.draw()
    for asteroid in asteroids:
        asteroid.draw()

    level_label.draw()
    score_label.draw()

if __name__ == '__main__':
    pyglet.app.run()