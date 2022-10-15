import pico2d
import game_framework
import play_state
import window_size

pico2d.open_canvas(window_size.width, window_size.height)
game_framework.run(play_state)
pico2d.close_canvas()