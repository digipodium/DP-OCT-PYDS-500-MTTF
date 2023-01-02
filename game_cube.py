# ursina rotating cube
from ursina import *
import random

app = Ursina()
camera.orthographic = True
camera.fov = 20
cubes = []
for i in range(10):
    cube = Entity(
        model='cube',
        color=color.random_color(), 
        scale=(1,1,1), 
        position=(
            random.randint(-5,5),
            random.randint(-5,5),
            random.randint(-5,5)),
        texture='white_cube'
    )
    cubes.append(cube)

def update():
    for cube in cubes:
        cube.rotation_x += 2
        cube.rotation_y += 1.5
app.run()
