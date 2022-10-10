import pico2d
import charater
import Key_Events



pico2d.open_canvas()
character = charater.Charater()

while Key_Events.Ongame:
    Key_Events.key_events()
    character.update()
    pico2d.clear_canvas()
    character.draw()

    pico2d.update_canvas()
    pico2d.delay(0.05)


pico2d.close_canvas()