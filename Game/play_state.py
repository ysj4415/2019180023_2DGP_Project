import pico2d
from Object import Nom
import firering
import spike
import game_framework


nom = None
ring = None
trap = None
running = None
image = None


# 초기화
def enter():
    global nom
    global ring
    global trap
    global running
    global image

    nom = Nom.nom()
    ring = firering.FireRing(600,50, 1)
    trap = spike.Spike(200, 15)
    running = True
    image = pico2d.load_image('res/map/map1.png')
# 종료
def exit_state():
    global nom
    global ring
    global trap
    del nom
    del ring
    del trap
def update(frame_time):
    nom.update(frame_time)
    ring.update()
    trap.update()
def draw():
    pico2d.clear_canvas()
    image.draw(400,300)
    nom.draw()
    ring.draw()
    trap.draw()
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