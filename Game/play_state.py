import pico2d
import charater
import firering
import game_framework


nom = None
ring = None
running = None

# 초기화
def enter():
    global nom
    global ring
    global running
    nom = charater.Charater()
    ring = firering.FireRing(600,50)
    running = True

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