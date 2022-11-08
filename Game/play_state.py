import pico2d
from Object import Nom
import firering
import spike
import game_framework
import game_world

nom = None
running = None
image = None


# 초기화
def enter():
    global nom
    global running
    global image

    nom = Nom.nom()
    monster = (firering.FireRing(600,50, 2),
               firering.FireRing(450,50, 1),
               spike.Spike(200, 15, 0),
               spike.Spike(785, 200, 1))
    game_world.add_object(nom, 0)
    game_world.add_objects(monster, 0)

    running = True
    image = pico2d.load_image('res/map/map1.png')
# 종료
def exit_state():
    game_world.clear()
def update(frame_time):
    for game_object in game_world.all_objects():
        game_object.update(frame_time)
def draw_world():
    image.draw(400,300)
    for game_object in game_world.all_objects():
        game_object.draw()

def draw():
    pico2d.clear_canvas()
    draw_world()
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