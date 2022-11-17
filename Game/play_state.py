import pico2d
from Object import Nom, spike, firering
from Object.low_floor import Low_Floor
from Object.flower import Flower
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
    floors = []
    for i in range(66,800,66):
        floors += [Low_Floor(i,5,0)]


    firerings = [firering.FireRing(600, 60, 2, 0),
                 firering.FireRing(750, 400, 2, 1),
                 firering.FireRing(450, 60, 1, 0)]
    spikes = [spike.Spike(200, 25, 0),
              spike.Spike(785, 200, 1)]

    flowers = [Flower(300, 42, 0)]

    game_world.add_object(nom, 0)
    game_world.add_objects(firerings, 0)
    game_world.add_objects(spikes, 0)
    game_world.add_objects(flowers, 0)
    game_world.add_objects(floors, 0)

    running = True
    image = pico2d.load_image('res/map/map1.png')

    trap = spikes + firerings
    game_world.add_collision_pairs(nom, trap, 'nom:trap')
    monster = flowers
    game_world.add_collision_pairs(nom, monster, 'nom:monster')
    game_world.add_collision_pairs(nom, floors, 'nom:floors')

# 종료
def exit_state():
    game_world.clear()
def update():
    for game_object in game_world.all_objects():
        game_object.update()

    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b):
            a.handle_collision(b, group)
            b.handle_collision(a, group)
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

def collide(a,b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

