import pygame
import sys

# Pygameの初期化
pygame.init()

# ウィンドウ設定
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# キャラクター設定
player_pos = [400, 300]
player_size = 50
player_color = (0, 0, 255)  # 青色

# ゲームループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # キャラクター移動の処理（ここに実装）

    # 背景を塗りつぶし
    screen.fill((0, 0, 0))  # 黒色で塗りつぶし

    # キャラクターの描画
    pygame.draw.rect(
        screen, player_color, (player_pos[0], player_pos[1], player_size, player_size)
    )

    # 画面の更新
    pygame.display.flip()

pygame.quit()
