import pgzrun

HEIGHT = 600
WIDTH = 1200

p = Actor('ironman',center=(WIDTH//2, HEIGHT//2))

title = "IRON-MAN GAME"

def draw():
    screen.fill('white')
    screen.draw.text(title, center=(WIDTH//2,30),fontsize=60,
        color='black', align='center',shadow=(.2,1),scolor="red")
    p.draw()

def p_move():
    if keyboard.right and p.right < WIDTH:
        p.x += 3
    if keyboard.left and p.left > 0:
        p.x -= 3
    if keyboard.up and p.top > 0:
        p.y -= 3
    if keyboard.down and p.bottom < HEIGHT:
        p.y += 3

def update():
    p_move() # function call

    print(p.x, p.y, p.angle)

pgzrun.go()