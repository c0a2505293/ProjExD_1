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
    kk_rect = kk_img.get_rect()#練10-1
    kk_rect.center = (300, 200)#練10-2
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_list = pg.key.get_pressed()#練10-3
        if key_list[pg.K_UP]:
            kk_rect.move_ip(0, -1)
        if key_list[pg.K_DOWN]:
            kk_rect.move_ip(0, +1)
        if key_list[pg.K_LEFT]:
            kk_rect.move_ip(-1, 0)
        if key_list[pg.K_RIGHT]:
            kk_rect.move_ip(+1, 0)
        screen.blit(kk_img, kk_rect)
        x = tmr #練5
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