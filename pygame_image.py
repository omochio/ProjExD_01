import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()

    # Surfaces
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    kokaton_img = pg.image.load("ex01/fig/3.png")
    fliped_kokaton_img = pg.transform.flip(kokaton_img, True, False)
    kokaton_img_list = [fliped_kokaton_img, pg.transform.rotozoom(fliped_kokaton_img, 10, 1.0)]

    # フレームレート
    framerate = 100    
    # こうかとん遷移フレーム数
    transition_frame_count = 50

    # 経過時間
    tmr = 0
    # こうかとんリストインデックス
    kokaton_idx = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        current_frame = tmr % framerate + 1
        tmr += 1
        x = tmr % 1600
        fliped_bg_img = pg.transform.flip(bg_img, True, False)
        if (tmr % (1600 * 2) < 1600):
            screen.blit(bg_img, [-x, 0])
            screen.blit(fliped_bg_img, [1600 - x, 0])
        else:
            screen.blit(fliped_bg_img, [-x, 0])
            screen.blit(bg_img, [1600 - x, 0])
            
        screen.blit(kokaton_img_list[kokaton_idx], [300, 200])

        if (current_frame % transition_frame_count == 0):
            kokaton_idx = (kokaton_idx + 1) % 2
        pg.display.update()
        clock.tick(framerate)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()