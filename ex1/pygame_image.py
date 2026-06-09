import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img_flipped = pg.transform.flip(bg_img, True, False)#練8
    kk_img = pg.image.load("fig/3.png")#練3
    kk_img = pg.transform.flip(kk_img, True, False)
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = x % 3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img, [-x+1600, 0])#練7
        screen.blit(bg_img_flipped, [-x+3200,0])#練9
        screen.blit(kk_img, kk_rect)#練4
        
        pg.display.update()
        tmr += 1        
        clock.tick(200)#練6
        


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()