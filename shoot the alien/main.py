import pgzrun
import random

TITLE="good shot"

WIDTH=550
HEIGHT=550

message=""
alien=Actor("alien")

def place_alien():
    alien.x=random.randint(50,WIDTH-50)
    alien.y=random.randint(50,HEIGHT-50)

def draw():
    screen.clear()
    screen.fill("cyan")
    alien.draw()
    screen.draw.text(message,center=(200,200),fontsize=30)

def update():
    pass


def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        place_alien()
        message="good shot"
    else:
        message="you missed"

place_alien()
pgzrun.go()