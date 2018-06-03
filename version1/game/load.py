import pyglet
import random

from . import resources


def asteroids(num_asteroids):
    asteroids = []
    for i in range(num_asteroids):
        asteroid_x = random.randint(0, 800)
        asteroid_y = random.randint(0, 600)
        new_asteroid = pyglet.sprite.Sprite(img=resources.asteroid_image,
                                            x=asteroid_x, y=asteroid_y)
        new_asteroid.rotation = random.randint(0, 360)
        asteroids.append(new_asteroid)
    return asteroids