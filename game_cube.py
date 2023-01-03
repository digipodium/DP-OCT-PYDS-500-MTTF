# ursina rotating cube
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
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
            random.randint(-10,10),
            random.randint(-10,10),
            random.randint(-5,5)),
        texture='white_cube',
        collider='box'
    )
    cubes.append(cube)

player = FirstPersonController()
ground = Entity(model='plane', scale=(100,10,3), texture='white_cube', color=color.rgb(0,255,255), collider='box', position=(0,0,-1))
ground.texture_scale = (100,100)

# make player stand on ground
player.y = ground.y + 1
# 3d camera
camera.position = (3,3,3)
camera.rotation = (0,0,0)


def input(key):
    if key == 'escape':
        quit()

def update():
    for cube in cubes:
        cube.rotation_x += random.randint(1,5)
        cube.rotation_y += random.randint(1,5)
        cube.rotation_z += random.randint(1,5)
    
app.run()
