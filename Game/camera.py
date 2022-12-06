import server
import window_size
from pico2d import *
map_size = [2000, 2000]

def get_camera():
    camera_x1 = clamp(0, server.nom.position.translate.x - window_size.width / 2, map_size[0] - window_size.width)
    camera_x2 = clamp(0, server.nom.position.translate.x + window_size.width / 2, map_size[0])
    camera_y1 = clamp(0, server.nom.position.translate.y - window_size.height / 2, map_size[1] - window_size.height)
    camera_y2 = clamp(0, server.nom.position.translate.y + window_size.height / 2, map_size[1])

    return camera_x1, camera_x2, camera_y1, camera_y2