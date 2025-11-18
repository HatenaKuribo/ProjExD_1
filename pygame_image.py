import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img1 = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img2, True, False)
    player_img = pg.image.load("fig/3.png")
    player_img = pg.transform.flip(player_img, True, False)
    tmr = 0
    x = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img1, [-x, 0])
        screen.blit(bg_img2, [-x+1600, 0])
        screen.blit(bg_img1, [-x+3200, 0])
        screen.blit(player_img, [300,200])
        pg.display.update()
        tmr += 1 
        x += 1
        if x == 3200:
            x = 0
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()