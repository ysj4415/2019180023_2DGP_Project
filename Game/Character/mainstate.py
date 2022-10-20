from Character import CharacterController as CC
import math

def jumprange(jumpradian, jumppower, index):
    return jumppower * math.sin(jumpradian / 360 * 2 * math.pi) * index

frame = None

class MainState:
    def enter(nom, event):
        if event == CC.RIGHT_DOWN:
            nom.dir+=1
        elif event == CC.LEFT_DOWN:
            nom.dir-=1
        elif event ==  CC.RIGHT_UP:
            nom.dir-=1
        elif event == CC.LEFT_UP:
            nom.dir+=1
        nom.dir = CC.clamp(-1, nom.dir, 1)
        global frame
        frame = 0
    def exit(nom):
        pass
    def do(nom):
        global frame
        nom.frame = (frame // 50) % nom.anim[1]
        nom.move(nom.dir)

        frame += 1;
    def draw(nom):
        f_index = (nom.floor_index + 1) % 4
        nom.image.clip_composite_draw(nom.frame*64, nom.anim[0] * 64,
                                        64, 64, nom.rotation_radian, nom.flip,
                                       nom.x + jumprange(nom.jumpradian, nom.jumppower, CC.x_tuple[f_index]),
                                       nom.y + jumprange(nom.jumpradian, nom.jumppower, CC.y_tuple[f_index]), 64, 64)