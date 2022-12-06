import pico2d
from Object import Nom, spike, firering
from Object.low_floor import Low_Floor
from Object.high_floor import High_Floor
from Object.high_floor import High_Floor_up

from Object.flower import Flower
import game_framework
import game_world
from UI import Ui
import window_size
from BackGround import Background

import puase_state

import server
import camera

import json


bgm = None
map_size = [2000, 2000]
# 초기화
def enter():
    server.ui = Ui()
    server.nom = Nom.nom()
    server.floors = []
    # server.up_floors = []
    # server.up_floors_step = []

    for i in range(66,map_size[0],66):
        server.floors += [Low_Floor(i,5,0)]
    for i in range(66,map_size[0],66):
        server.floors += [Low_Floor(i,map_size[1] - 5,2)]
    for i in range(66,map_size[1],66):
        server.floors += [Low_Floor(5,i,3)]
    for i in range(66,map_size[1],66):
        server.floors += [Low_Floor(map_size[0] - 5 ,i,1)]
    # for i in range(66,133,66):
    #     server.up_floors += [High_Floor(i + 500,68,0)]
    #     server.up_floors_step += [High_Floor_up(i + 500,68,0)]

    # server.firerings = [firering.FireRing(800, 60, 2, 0),
    #              firering.FireRing(map_size[0] - 60, 600, 2, 1),
    #              firering.FireRing(1100, 60, 1, 0)]
    # server.spikes = [spike.Spike(1300, 25, 0),
    #           spike.Spike(map_size[0] - 25, 400, 1)]

    # server.flowers = [Flower(200, 42, 0)]
    server.background = Background()

    game_world.add_object(server.background, 0)
    game_world.add_object(server.nom, 2)
    # game_world.add_objects(server.firerings, 1)
    # game_world.add_objects(server.spikes, 1)
    # game_world.add_objects(server.flowers, 2)
    game_world.add_objects(server.floors, 1)
    # game_world.add_objects(server.up_floors, 1)
    # game_world.add_objects(server.up_floors_step, 1)

    # server.image = pico2d.load_image('res/map/map3.png')

    # trap = server.spikes + server.firerings
    # game_world.add_collision_pairs(server.nom, trap, 'nom:trap')
    # monster = server.flowers
    # game_world.add_collision_pairs(server.nom, monster, 'nom:monster')
    game_world.add_collision_pairs(server.nom, server.floors, 'nom:floors')
    # game_world.add_collision_pairs(server.nom, server.up_floors, 'nom:up_floors')
    # game_world.add_collision_pairs(server.nom, server.up_floors_step, 'nom:up_floors_step')

    with open('spike_data.json', 'r') as f:
        spike_data_list = json.load(f)
    server.spikes = [spike.Spike(o['x'], o['y'], o['index']) for o in spike_data_list]
    with open('firerings_data.json', 'r') as f:
        firerings_data_list = json.load(f)
    server.firerings = [firering.FireRing(o['x'], o['y'], o['step'], o['index']) for o in firerings_data_list]

    trap = server.spikes + server.firerings
    game_world.add_objects(trap, 1)
    game_world.add_collision_pairs(server.nom, trap, 'nom:trap')




    with open('flower_data.json', 'r') as f:
        flower_data_list = json.load(f)
    server.flowers = [Flower(o['x'], o['y'], o['index']) for o in flower_data_list]

    game_world.add_objects(server.flowers, 2)
    monster = server.flowers
    game_world.add_collision_pairs(server.nom, monster, 'nom:monster')




    with open('up_floors_data.json', 'r') as f:
        up_floors_data_list = json.load(f)
    server.up_floors = [High_Floor(o['x'], o['y'], o['index']) for o in up_floors_data_list]
    server.up_floors_step = [High_Floor_up(o['x'], o['y'], o['index']) for o in up_floors_data_list]

    game_world.add_objects(server.up_floors, 1)
    game_world.add_objects(server.up_floors_step, 1)
    game_world.add_collision_pairs(server.nom, server.up_floors, 'nom:up_floors')
    game_world.add_collision_pairs(server.nom, server.up_floors_step, 'nom:up_floors_step')

    global bgm
    bgm = pico2d.load_music('res/It Was a Time - TrackTribe.mp3')

    bgm.set_volume(32)
    bgm.repeat_play()

# 종료
def exit_state():
    global bgm

    game_world.clear()
    bgm.stop()
def update():
    for game_object in game_world.all_objects():
        game_object.update()

    server.ui.update()

    camera_x1, camera_x2, camera_y1, camera_y2 = camera.get_camera()
    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b):
            a.handle_collision(b, group)
            b.handle_collision(a, group)

# import window_size


def draw_world():
    camera_x1, camera_x2, camera_y1, camera_y2 = camera.get_camera()


    for game_object in game_world.all_objects():
        # if camera_x1 - 50 <= game_object.position.translate.x <= camera_x2 + 50 and camera_y1 - 50 <= game_object.position.translate.y <= camera_y2 + 50:
        game_object.draw()
    server.ui.draw()

def draw():
    pico2d.clear_canvas()
    draw_world()
    pico2d.update_canvas()


def handle_events():
    events = pico2d.get_events()
    for event in events:
        # esc key
        if event.type == pico2d.SDL_KEYDOWN and event.key == pico2d.SDLK_ESCAPE:
            game_framework.push_state(puase_state)
        # left key
        server.nom.handle_event(event)

def pause():
    global bgm
    bgm.pause()
    pass

def resume():
    global bgm
    bgm.resume()
    pass

def collide(a,b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

