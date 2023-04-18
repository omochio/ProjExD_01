import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    kokaton_img = pg.image.load("ex01/fig/3.png")
    fliped_kokaton_img = pg.transform.flip(kokaton_img, True, False)
    kokaton_img_list = [fliped_kokaton_img, pg.transform.rotate(fliped_kokaton_img, 10)]

    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        tmr += 1
        screen.blit(bg_img, [0, 0])
        screen.blit(kokaton_img_list[tmr % 2], [300, 200])
        pg.display.update()
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()