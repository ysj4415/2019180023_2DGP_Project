import pico2d
import charater
import game_framework

nom = None
running = None

# 초기화
def enter():
    global nom
    global running
    nom = charater.Charater()
    running = True

# 종료
def exit_state():
    global nom
    del nom

def update():
    nom.update()

def draw():
    pico2d.clear_canvas()
    nom.draw()
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