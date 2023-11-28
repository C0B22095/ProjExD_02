import sys
import pygame as pg
import random


WIDTH, HEIGHT = 1600, 900

def screen_judg(rct:pg.Rect) -> tuple[bool, bool]:
    """
    オブジェクトが画面内or画面外を判定し、真理値タプルを返す関数
    引き数　rct:こうかとんor爆弾SurfaceのRect
    戻り値：横方向、縦方向判定結果（画面内:True/画面外:False）
    """
    width, height = True, True
    if (rct.left < 0) or (rct.right > WIDTH):
        width = False
    elif (rct.top < 0) or (rct.bottom > HEIGHT):
        height = False
    return (width, height)

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_img_dct = {(-5, 0):pg.transform.rotozoom(kk_img, 0, 1), (-5, 5):pg.transform.rotozoom(kk_img, 45, 1), (0, 5):pg.transform.rotozoom(kk_img, 90, 1), (5, 5):pg.transform.rotozoom(kk_img, 135, 1), (5, 0):pg.transform.rotozoom(kk_img, 180, 1), (5, -5):pg.transform.rotozoom(kk_img, 225, 1), (0, -5):pg.transform.rotozoom(kk_img, 270, 1), (-5, -5):pg.transform.rotozoom(kk_img, 315, 1)}
    kk_img_rct = kk_img.get_rect()
    kk_img_rct.center = 900, 400
    enn = pg.Surface((20, 20))
    enn1 = pg.Surface((20, 20))
    enn.set_colorkey((0, 0, 0))
    enn1.set_colorkey((0, 0, 0))
    pg.draw.circle(enn, (255, 0, 0), (10, 10), 10) 
    pg.draw.circle(enn1, (0, 255, 0), (10, 10), 10)
    enn_rct = enn.get_rect()
    enn_rct.center = WIDTH/2, HEIGHT/2
    enn1_rct = enn1.get_rect()
    enn1_rct.center = WIDTH/2, HEIGHT/2
    vx, vy = 5, 5
    vx1, vy1 = 10, 10
    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        if kk_img_rct.colliderect(enn_rct):
            print("Game Over")
            return

        sum_move = [0, 0]
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]: sum_move[1] -= 5
        if key_lst[pg.K_DOWN]: sum_move[1] += 5
        if key_lst[pg.K_LEFT]: sum_move[0] -= 5
        if key_lst[pg.K_RIGHT]: sum_move[0] += 5
        
        screen.blit(bg_img, [0, 0])
        kk_img_rct.move_ip(sum_move[0], sum_move[1]) 
        if screen_judg(kk_img_rct) != (True, True):
            kk_img_rct.move_ip(-sum_move[0], -sum_move[1])
        if sum_move == [0, 0]:
            screen.blit(kk_img, kk_img_rct)
        else:
            screen.blit(kk_img_dct[tuple(sum_move)], kk_img_rct)
            kk_img = kk_img_dct[tuple(sum_move)]
        width, height = screen_judg(enn_rct)
        if not width:
            vx *= -1
        if not height:
            vy *= -1
        enn_rct.move_ip(vx, vy)
        screen.blit(enn, enn_rct)
        if tmr > 50*10:
            width, height = screen_judg(enn1_rct)
            if not width:
                vx1 *= -1
            if not height:
                vy1 *= -1
            enn1_rct.move_ip(vx1, vy1)
            screen.blit(enn1, enn1_rct)
        pg.display.update()
        tmr += 1
        clock.tick(50)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()