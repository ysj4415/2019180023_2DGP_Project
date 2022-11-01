import pico2d
from Object import Nom
import firering
import spike
import game_framework


nom = None
ring = None
ring2 = None
traps = None
running = None
image = None


# 초기화
def enter():
    global nom
    global ring
    global ring2
    global traps
    global running
    global image

    nom = Nom.nom()
    ring = firering.FireRing(600,50, 2)
    ring2 = firering.FireRing(450,50, 1)
    traps = [spike.Spike(200, 15, 0), spike.Spike(785, 200, 1)]
    running = True
    image = pico2d.load_image('res/map/map1.png')
# 종료
def exit_state():
    global nom
    global ring
    global ring2
    global traps
    del nom
    del ring
    del ring2
    del traps
def update(frame_time):
    nom.update(frame_time)
    ring.update()
    ring2.update()
    for trap in traps : trap.update()
def draw():
    pico2d.clear_canvas()
    image.draw(400,300)
    nom.draw()
    ring.draw()
    ring2.draw()
    for trap in traps : trap.draw()
    pico2d.update_canvas()


def handle_events():
    events = pico2d.get_events()
    for event in events:
        # esc key
        if event.key == pico2d.SDLK_ESCAPE:
            game_framework.quit()
        # left key
        nom.handle_event(event)

def pause():
    pass

def resume():
    pass