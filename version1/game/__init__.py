import pyglet

def center_image(image):
    image.anchor_x = image.width
    image.anchor_y = image.height

# Update our assets directory.
pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

# Loading game assets.
player_image = pyglet.resource.image('player.png')
bullet_image = pyglet.resource.image('bullet.png')
asteroid_image = pyglet.resource.image('asteroid.png')

# Center game images.
center_image(player_image)
center_image(bullet_image)
center_image(asteroid_image)

# Load game window.
game_window = pyglet.window.Window()

if __name__ == '__main__':
    pyglet.app.run()