import pico2d
from Character import character
import firering
import game_framework


nom = None
ring = None
running = None
image = None

# 초기화
def enter():
    global nom
    global ring
    global running
    global image

    nom = character.Character()
    ring = firering.FireRing(600,50)
    running = True
    image = pico2d.load_image('res/map/map1.png')
# 종료
def exit_state():
    global nom
    global ring
    del nom
    del ring
def update(frame_time):
    nom.update(frame_time)
    ring.update()

def draw():
    pico2d.clear_canvas()
    image.draw(400,300)
    nom.draw()
    ring.draw()
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