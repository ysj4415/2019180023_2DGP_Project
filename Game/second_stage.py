import pico2d
from Object import Nom, spike, firering
from Object.low_floor import Low_Floor
from Object.flower import Flower
import game_framework
import game_world
from UI import Ui
import window_size

nom = None
running = None
image = None
ui = None


map_size = [2000, 2000]
# 초기화
def enter():
    global nom
    global running
    global image
    global ui

    ui = Ui()
    nom = Nom.nom()
    floors = []
    for i in range(66,map_size[0],66):
        floors += [Low_Floor(i,5,0)]
    for i in range(66,map_size[0],66):
        floors += [Low_Floor(i,map_size[1] - 5,2)]
    for i in range(66,map_size[1],66):
        floors += [Low_Floor(5,i,3)]
    for i in range(66,map_size[1],66):
        floors += [Low_Floor(map_size[0] - 5 ,i,1)]

    firerings = [firering.FireRing(600, 60, 2, 0),
                 firering.FireRing(map_size[0] - 60, 600, 2, 1),
                 firering.FireRing(1100, 60, 1, 0)]
    spikes = [spike.Spike(1300, 25, 0),
              spike.Spike(map_size[0] - 25, 400, 1)]

    flowers = [Flower(200, 42, 0)]

    game_world.add_object(nom, 0)
    game_world.add_objects(firerings, 0)
    game_world.add_objects(spikes, 0)
    game_world.add_objects(flowers, 0)
    game_world.add_objects(floors, 0)

    running = True
    image = pico2d.load_image('res/map/map2.png')

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

    ui.update()

    camera_x1, camera_x2, camera_y1, camera_y2 = get_camera()
    for a, b, group in game_world.all_collision_pairs():
        if camera_x1 <= a.position.translate.x <= camera_x2 and camera_y1 <= a.position.translate.y <= camera_y2:
            if camera_x1 <= b.position.translate.x <= camera_x2 and camera_y1 <= b.position.translate.y <= camera_y2:
                if collide(a, b):
                    a.handle_collision(b, group)
                    b.handle_collision(a, group)

# import window_size
def get_camera():
    if nom.floor_index == 0:
        camera_x1 = nom.position.translate.x - window_size.width / 2
        camera_x2 = nom.position.translate.x + window_size.width / 2
        if camera_x1 < 0:
            camera_x1 = 0
            camera_x2 = window_size.width
        elif camera_x2 > map_size[0]:
            camera_x1 = map_size[0] - window_size.width
            camera_x2 = map_size[0]

        camera_y1 = 0
        camera_y2 = window_size.height
    if nom.floor_index == 1:
        camera_x1 = map_size[0] - window_size.width
        camera_x2 = map_size[0]

        camera_y1 = nom.position.translate.y - window_size.height / 2
        camera_y2 = nom.position.translate.y + window_size.height / 2

        if camera_y1 < 0:
            camera_y1 = 0
            camera_y2 = window_size.height
        elif camera_y2 > map_size[1]:
            camera_y1 = map_size[1] - window_size.height
            camera_y2 = map_size[1]


    if nom.floor_index == 2:
        camera_x1 = nom.position.translate.x - window_size.width / 2
        camera_x2 = nom.position.translate.x + window_size.width / 2

        camera_y1 = map_size[1] - window_size.height
        camera_y2 = map_size[1]

        if camera_x1 < 0:
            camera_x1 = 0
            camera_x2 = window_size.width
        elif camera_x2 > map_size[0]:
            camera_x1 = map_size[0] - window_size.width
            camera_x2 = map_size[0]
    if nom.floor_index == 3:
        camera_x1 = 0
        camera_x2 = window_size.width

        camera_y1 = nom.position.translate.y - window_size.height / 2
        camera_y2 = nom.position.translate.y + window_size.height / 2
        if camera_y1 < 0:
            camera_y1 = 0
            camera_y2 = window_size.height
        elif camera_y2 > map_size[1]:
            camera_y1 = map_size[1] - window_size.height
            camera_y2 = map_size[1]


    return camera_x1, camera_x2, camera_y1, camera_y2

def draw_world():
    image.draw(window_size.width / 2,window_size.height / 2)

    # if nom.floor_index == 0:
    # camera_x1 = nom.position.translate.x - window_size.width / 2
    # camera_x2 = nom.position.translate.x + window_size.width / 2
    #
    # camera_y1 = nom.position.translate.y - window_size.height / 2
    # camera_y2 = nom.position.translate.y + window_size.height / 2

    camera_x1, camera_x2, camera_y1, camera_y2 = get_camera()


    for game_object in game_world.all_objects():
        if camera_x1 - 50 <= game_object.position.translate.x <= camera_x2 + 50 and camera_y1 - 50 <= game_object.position.translate.y <= camera_y2 + 50:
            game_object.draw(camera_x1, camera_y1)
    ui.draw()
    # image2 = pico2d.load_image('res/UI/Life.png')
    # image2.clip_composite_draw(0, 0, 40, 40,
    #                                0, '',
    #                                20, window_size.height - 30, 40, 40)

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

